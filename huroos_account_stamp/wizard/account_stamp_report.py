from odoo import api, fields, models
import calendar


TODAY = fields.date.today()
LAST_DAY_IN_MONTH = calendar.monthrange(TODAY.year, TODAY.month)[1]


class AccountStampReport(models.TransientModel):
    _name = "account.stamp.report"
    _description = "Wizard report imposte di bollo"

    name = fields.Char(
        string="Nome",
        default="Report imposte di bollo",
        readonly=True
    )
    stamp_number = fields.Integer(
        string="Numero bolli",
        readonly=True
    )
    stamp_amount = fields.Float(
        string="Importo da pagare",
        readonly=True
    )
    date_start = fields.Date(
        string="Dal",
        default=fields.date(TODAY.year, TODAY.month, 1),
        required=True
    )
    date_end = fields.Date(
        string="al",
        default=fields.date(TODAY.year, TODAY.month, LAST_DAY_IN_MONTH),
        required=True
    )
    invoice_ids = fields.Many2many(
        comodel_name="account.move",
        string="Registrazioni",
        readonly=True
    )
    include_draft = fields.Boolean(
        string="Includi registrazioni in bozza"
    )
    computed = fields.Boolean(
        help="Campo tecnico per capire se il report è stato calcolato almeno una volta.",
        compute="_compute_computed"
    )

    @api.depends('stamp_number')
    def _compute_computed(self):
        for wizard in self:
            if wizard.stamp_number > 0:
                wizard.computed = True
            else:
                wizard.computed = False

    def compute_report(self):

        domain = [
            ("invoice_date", ">=", self.date_start),
            ("invoice_date", "<=", self.date_end),
            ("company_id", "=", self.env.company.id),
            ("tax_stamp", "=", True)
        ]
        if self.include_draft:
            domain.append(("state", "in", ("draft", "posted")))
        else:
            domain.append(("state", "=", "posted"))

        self.invoice_ids = self.env["account.move"].search(domain)

        # Calcolo il numero di bolli e l'importo (ogni bollo costa 2€)
        self.stamp_number = len(self.invoice_ids)
        self.stamp_amount = self.stamp_number * 2

        return {
            "type": "ir.actions.act_window",
            "view_mode": "form",
            "res_model": "account.stamp.report",
            "target": "new",
            "res_id": self.id
        }
