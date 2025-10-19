from odoo import fields, models
from odoo.tools.misc import format_date
from odoo.exceptions import UserError
import json


class ResPartnerDataFecth(models.TransientModel):
    _name = "res.partner.data.fetch"
    _description = "Wizard to fetch partner data from OpenAPI"

    mode = fields.Selection(
        # Ogni valore della selection deve avere una funzione col medesimo nome
        selection=[
            ('vat_validation', 'Validazione Partita IVA'),
            ('fiscalcode_validation', 'Validazione Codice Fiscale'),
            ('address_from_vat', 'Ottieni ragione sociale e indirizzo'),
            ('company_info', 'Ottieni informazioni di base di un\'azienda italiana'),
            ('company_complete_info', 'Ottieni informazioni avanzate di un\'azienda italiana (codice ateco, bilancio, pec, ecc...)'),
            ('sdi_code', 'Ottieni codice SDI'),
            ('foreign_data', 'Ottieni dati azienda da Partita IVA estera')
        ],
        string="Cosa vuoi fare?",
        required=True
    )
    save_mode = fields.Selection(
        string="Modalità di salvataggio dati",
        selection=[
            ('new', 'Crea nuovo contatto'),
            ('edit_existing', 'Aggiorna esistente')
        ]
    )
    code = fields.Char(
        required=True,
        help="Codice Fiscale, Partita IVA o identificativo dell'azienda."
    )
    display_message = fields.Text(
        string="Messaggio da visualizzare",
        readonly=True
    )
    data_table = fields.Html(
        string="Tabella dei partner già validati",
        readonly=True
    )
    active_partner_id = fields.Many2one(
        comodel_name="res.partner",
        string="Partner attualmente attivo"
    )
    update_partner_id = fields.Many2one(
        comodel_name="res.partner",
        string="Contatto da aggiornare"
    )

    @staticmethod
    def action_success(message):
        return {
            'effect': {
                'fadeout': 'slow',
                'message': message,
                'img_url': '/web/static/src/img/smile.svg',
                'type': 'rainbow_man',
            }
        }

    def default_get(self, fields_list):
        result = super(ResPartnerDataFecth, self).default_get(fields_list)
        if self._context.get('active_id') and self._context.get('active_model') == "res.partner":
            # Se c'è un partner attivo compilo in automatico la Partita IVA o il Codice Fiscale
            active_partner = self.env['res.partner'].browse(self._context['active_id'])
            result.update({
                'active_partner_id': active_partner.id,
                'update_partner_id': active_partner.id,
                'save_mode': 'edit_existing' if active_partner else False
            })
            if active_partner and active_partner.company_type == "company":
                result['code'] = active_partner.vat or active_partner.fiscalcode
            elif active_partner and active_partner.company_type == "person":
                result['code'] = active_partner.fiscalcode or active_partner.vat

        return result

    def proceed_anyway(self):
        return getattr(self, self.mode)(force=True)

    def execute_action(self):
        try:
            method = getattr(self, self.mode)

        except AttributeError:
            raise UserError(f"Funzionalità {self.mode} non ancora implementata nel codice.")

        else:
            return method()

    def fetch_existing_code(self, field="vat") -> dict:
        """
        Metodo che ritorna sempre un dizionario contenente i record res.partner che risultano già validati col codice
        (P.IVA o CF) passato come parametro. Se non trova nulla ritorna dei recordset vuoti.
        """

        if field not in ("vat", "fiscalcode", "openapi_id"):
            raise SyntaxError(f"Field {field} not supported by fetch_existing_code() method. "
                              f"Try with 'vat' or 'fiscalcode'.")

        found_data = {'active_partner_id': self.env['res.partner'], 'partner_ids': self.env['res.partner']}
        openapi_field = "vatCode" if field == "vat" else "taxCode" if field == "fiscalcode" else "id"

        # Prima erifico se è presente un contatto sulla schermata
        if self.active_partner_id and self.active_partner_id.openapi_data:
            # Se esiste ed è già stato sincronizzato con OpenAPI in passato provo
            # a vedere se i dati sono ancora validi
            openapi_data = json.loads(self.active_partner_id.openapi_data)
            if openapi_data and openapi_data.get(openapi_field) == self.code:
                found_data['active_partner_id'] = self.active_partner_id

        # Poi cerco globalmente per P.IVA o CF
        already_synchronized_partners = self.env['res.partner'].search([(field, 'ilike', self.code), ('openapi_data', '!=', False)])
        for partner in already_synchronized_partners:
            openapi_data = json.loads(partner.openapi_data)
            if openapi_data and openapi_data.get(openapi_field) == self.code:
                found_data['partner_ids'] |= partner

        return found_data

    def build_existing_data_table(self, data: dict) -> str:
        if not data.get('partner_ids'):
            return ""

        table = """
        <table class="table table-sm o_main_table">
            <thead>
                <tr>
                    <th>Contatto</th>
                    <th>Data ultima sincronizzazione dati</th>
                </tr>
            </thead>
            <tbody>
        """
        for partner in data['partner_ids']:
            table += f"""
            <tr>
                <td>{partner.name}</td>
                <td>{format_date(self.env, partner.openapi_last_fetch_date.date())}</td>
            </tr>
            """

        table += "</tbody></table>"
        return table

    def sanitize_json_data(self, json_data: dict):
        """
        Metodo che rende leggibile da Odoo un json, mappando correttamente le chiavi e i valori.
        (Valido solo per Partite IVA italiane)
        """
        address = json_data.get('address', {}).get('registeredOffice', {})
        country = self.env['res.country'].search([('code', '=', json_data.get('countryCode'))]) if json_data.get('countryCode') else self.env.ref('base.it')
        sanitized_data = {
            'company_type': 'company',
            'name': json_data.get('companyName'),
            'country_id': country.id,
            'fiscalcode': json_data.get('taxCode'),
            'vat': json_data.get('vatCode'),
            'street': address.get('streetName') or address.get('street') or json_data.get('companyAddress'),
            'city': address.get('town'),
            'zip': address.get('zipCode'),
            'state_id': self.env['res.country.state'].search([
                ('country_id', '=', country.id),
                ('code', '=', address.get('province'))
            ], limit=1).id if address.get('province') else False,
            'codice_destinatario': json_data.get('sdiCode'),
            'electronic_invoice_subjected': True if json_data.get('sdiCode') else False,
            'electronic_invoice_obliged_subject': True if json_data.get('sdiCode') else False,
            'pec_mail': json_data.get('pec')
        }
        # Rimuovo le chiavi del dizionario che hanno valori nulli
        return {k: v for k, v in sanitized_data.items() if v}

    def _prepare_dict_for_table(self, data: dict) -> dict:
        country = self.env['res.country'].search([('code', '=', data.get('countryCode'))]) if data.get('countryCode') else self.env.ref('base.it')
        return {
            k: v for k, v in {
                'Ragione sociale': data.get('name'),
                'Partita IVA': data.get('vat'),
                'Codice Fiscale': data.get('fiscalcode'),
                'Indirizzo': data.get('street'),
                'CAP': data.get('zip'),
                'Città': data.get('city'),
                'Provincia': self.env['res.country.state'].browse(data['state_id']).name if data.get('state_id') else None,
                'Nazione': country.name if country else None,
                'Codice SDI': data.get('codice_destinatario'),
                'Email PEC': data.get('pec_mail')
            }.items() if v
        }

    def build_confirm_data_table(self, data: dict) -> str:
        table = "<table class='table table-sm o_main_table'>"
        for key, value in self._prepare_dict_for_table(data).items():
            table += f"<tr><th>{key}</th><td>{value}</td></tr>"
        table += "</table>"
        return table

    def save_data(self):
        try:
            # Json grezzo
            openapi_data = json.loads(self.display_message)

            # Json formattato per essere leggibile da Odoo
            vals = self.sanitize_json_data(json_data=openapi_data)

            # Metto nei vals il display_message, che dovrebbe contenere un dizionario in stringa
            vals['openapi_data'] = self.display_message

            # Divido il fiscalcode e me lo tengo da parte perchè durante la creazione, vedendo che sto
            # assegnando il fiscalcode, mi crea un contatto di tipo persona, ignorando il company_type = 'company'
            fiscalcode = vals.pop('fiscalcode') if 'fiscalcode' in vals else False

            action = {
                "type": "ir.actions.act_window",
                "view_mode": "form",
                "view_id": self.env.ref('base.view_partner_form').id,
                "res_model": "res.partner",
                "target": "current"
            }

            if self.save_mode == "new":
                partner = self.env['res.partner'].create(vals)
                partner.fiscalcode = fiscalcode
                action['res_id'] = partner.id

            elif self.save_mode == "edit_existing" and self.update_partner_id:
                self.update_partner_id.write(vals)
                self.update_partner_id.fiscalcode = fiscalcode
                # Se il contatto attivo è uguale a quello da aggiornare non serve che cambi finestra
                if self.active_partner_id and self.update_partner_id.id == self.active_partner_id.id:
                    return True
                action['res_id'] = self.update_partner_id.id

        except Exception as ex:
            raise UserError(str(ex))

        else:
            if action.get('res_id'):
                return action
            else:
                raise UserError("Qualcosa è andato storto durante il salvataggio dei dati.")

    def vat_validation(self, force=False):
        self.code = self.code.strip().lower().replace("it", "")
        if not force:
            existing_data = self.fetch_existing_code(field="vat")
            if existing_data.get('active_partner_id'):
                self.display_message = (f"Risulta che il contatto {self.active_partner_id.name} "
                                        f"abbia già una Partita IVA validata risalente al "
                                        f"{format_date(self.env, self.active_partner_id.openapi_last_fetch_date.date())}. "
                                        f"Procedere comunque con la validazione?")
                return {
                    "type": "ir.actions.act_window",
                    "view_mode": "form",
                    "view_id": self.env.ref('huroos_openapi.res_partner_data_fetch_message').id,
                    "res_model": "res.partner.data.fetch",
                    "target": "new",
                    "res_id": self.id
                }
            elif not existing_data.get('active_partner_id') and existing_data.get('partner_ids'):
                self.display_message = ("Risulta che i seguenti contatti abbiano già una Partita IVA validata uguale a "
                                        "quella inserita. Procedere comunque?")
                self.data_table = self.build_existing_data_table(existing_data)
                return {
                    "type": "ir.actions.act_window",
                    "view_mode": "form",
                    "view_id": self.env.ref('huroos_openapi.res_partner_data_fetch_message_with_table').id,
                    "res_model": "res.partner.data.fetch",
                    "target": "new",
                    "res_id": self.id
                }

        openapi_engine = self.env.ref('huroos_openapi.openapi_engine_main')
        data = openapi_engine.endpoint("/IT-start").call(code=self.code)
        if data['success'] and data['data']:
            return self.action_success("La Partita IVA è valida!")
        else:
            raise UserError(data['message'])

    def fiscalcode_validation(self):
        openapi_engine = self.env.ref('huroos_openapi.openapi_engine_main')
        data = openapi_engine.endpoint("/IT-verifica_cf").call(code=self.code)
        if data['success'] and data['data']:
            return self.action_success("Il codice fiscale è valido!")
        else:
            raise UserError(data['message'])

    def address_from_vat(self):
        openapi_engine = self.env.ref('huroos_openapi.openapi_engine_main')
        data = openapi_engine.endpoint("/IT-address").call(code=self.code)
        if data['success'] and data['data']:
            self.display_message = json.dumps(data['data'][0], indent=4)
            self.data_table = self.build_confirm_data_table(self.sanitize_json_data(data['data'][0]))
            return {
                "type": "ir.actions.act_window",
                "view_mode": "form",
                "view_id": self.env.ref('huroos_openapi.res_partner_data_fetch_confirm_data').id,
                "res_model": "res.partner.data.fetch",
                "target": "new",
                "res_id": self.id
            }
        else:
            raise UserError(data['message'])

    def company_info(self):
        openapi_engine = self.env.ref('huroos_openapi.openapi_engine_main')
        data = openapi_engine.endpoint("/IT-start").call(code=self.code)
        if data['success'] and data['data']:
            self.display_message = json.dumps(data['data'][0], indent=4)
            self.data_table = self.build_confirm_data_table(self.sanitize_json_data(data['data'][0]))
            return {
                "type": "ir.actions.act_window",
                "view_mode": "form",
                "view_id": self.env.ref('huroos_openapi.res_partner_data_fetch_confirm_data').id,
                "res_model": "res.partner.data.fetch",
                "target": "new",
                "res_id": self.id
            }
        else:
            raise UserError(data['message'])

    def company_complete_info(self):
        openapi_engine = self.env.ref('huroos_openapi.openapi_engine_main')
        data = openapi_engine.endpoint("/IT-advanced").call(code=self.code)
        if data['success'] and data['data']:
            self.display_message = json.dumps(data['data'][0], indent=4)
            self.data_table = self.build_confirm_data_table(self.sanitize_json_data(data['data'][0]))
            return {
                "type": "ir.actions.act_window",
                "view_mode": "form",
                "view_id": self.env.ref('huroos_openapi.res_partner_data_fetch_confirm_data').id,
                "res_model": "res.partner.data.fetch",
                "target": "new",
                "res_id": self.id
            }
        else:
            raise UserError(data['message'])

    def sdi_code(self, force=False):
        self.code = self.code.strip().lower().replace("it", "")
        if not force:
            existing_data = self.fetch_existing_code(field="vat")
            if existing_data.get('active_partner_id'):
                self.display_message = (f"Risulta che il contatto {self.active_partner_id.name} "
                                        f"abbia già un codice SDI nella cache risalente al "
                                        f"{format_date(self.env, self.active_partner_id.openapi_last_fetch_date.date())}. "
                                        f"Procedere comunque?")
                return {
                    "type": "ir.actions.act_window",
                    "view_mode": "form",
                    "view_id": self.env.ref('huroos_openapi.res_partner_data_fetch_message').id,
                    "res_model": "res.partner.data.fetch",
                    "target": "new",
                    "res_id": self.id
                }
            elif not existing_data.get('active_partner_id') and existing_data.get('partner_ids'):
                self.display_message = ("Risulta che i seguenti contatti con la Partita IVA inserita abbiano già un "
                                        "codice SDI nella cache. Procedere comunque?")
                self.data_table = self.build_existing_data_table(existing_data)
                return {
                    "type": "ir.actions.act_window",
                    "view_mode": "form",
                    "view_id": self.env.ref('huroos_openapi.res_partner_data_fetch_message_with_table').id,
                    "res_model": "res.partner.data.fetch",
                    "target": "new",
                    "res_id": self.id
                }

        openapi_engine = self.env.ref('huroos_openapi.openapi_engine_main')
        data = openapi_engine.endpoint("/IT-sdicode").call(code=self.code)
        if data['success'] and data['data']:
            self.display_message = json.dumps(data['data'][0], indent=4)
            self.data_table = self.build_confirm_data_table(self.sanitize_json_data(data['data'][0]))
            return {
                "type": "ir.actions.act_window",
                "view_mode": "form",
                "view_id": self.env.ref('huroos_openapi.res_partner_data_fetch_confirm_data').id,
                "res_model": "res.partner.data.fetch",
                "target": "new",
                "res_id": self.id
            }
        else:
            raise UserError(data['message'])

    def foreign_data(self):
        openapi_engine = self.env.ref('huroos_openapi.openapi_engine_main')
        data = openapi_engine.endpoint("/EU-start").call(code=self.code)
        if data['success'] and data['data']:
            self.display_message = json.dumps(data['data'][0], indent=4)
            self.data_table = self.build_confirm_data_table(self.sanitize_json_data(data['data'][0]))
            return {
                "type": "ir.actions.act_window",
                "view_mode": "form",
                "view_id": self.env.ref('huroos_openapi.res_partner_data_fetch_confirm_data').id,
                "res_model": "res.partner.data.fetch",
                "target": "new",
                "res_id": self.id
            }
        else:
            raise UserError(data['message'])
