from odoo import api, models
import copy


class ReportRegistroIva(models.AbstractModel):
    _inherit = "report.l10n_it_vat_registries.report_registro_iva"

    @api.model
    def _get_report_values(self, docids, data=None):
        """Inherit per aggiungere ai docargs una mappatura dei totali imposta divisa per registro"""

        docargs = super(ReportRegistroIva, self)._get_report_values(docids, data=data)

        tax_totals_mapped_by_journal = dict()

        # Fetch di tutte le imposte usate nel report
        total_used_taxes = self.env['account.tax']
        for move in docargs['docs']:
            total_used_taxes |= self._get_tax_lines(move, docargs['data'])[1]

        registry_type = docargs['data'].get("registry_type", "customer")
        sign = 1 if registry_type == "customer" else -1

        # Mappatura subtotali imposte per registro
        for journal in docargs['docs'].journal_id:
            tax_totals = list()
            ctx = {
                "from_date": docargs['data']["from_date"],
                "to_date": docargs['data']["to_date"],
                "vat_registry_journal_ids": [journal.id]
            }

            for tax in total_used_taxes:
                if tax.id not in docargs['docs'].filtered(lambda m: m.journal_id == journal).invoice_line_ids.tax_ids.ids:
                    continue

                tax = tax.with_context(**ctx)
                account_ids = (
                        tax.mapped("invoice_repartition_line_ids.account_id") |
                        tax.mapped("refund_repartition_line_ids.account_id")
                ).ids

                # Calcolo dei valori di imponibile e imposta
                # NB: Non è usato il flusso regolare di Odoo perchè per un motivo sconosciuto si perdono le
                #     informazioni del context tra una classe e l'altra (forse a causa della natura astratta
                #     della classa del report), quindi svolgo tutti i calcoli in questa classe
                tax.balance_regular = tax.compute_balance(tax_or_base="tax", financial_type="regular")
                tax.base_balance_regular = tax.compute_balance(tax_or_base="base", financial_type="regular")
                tax.balance_refund = tax.compute_balance(tax_or_base="tax", financial_type="refund")
                tax.base_balance_refund = tax.compute_balance(tax_or_base="base", financial_type="refund")
                tax.balance = tax.balance_regular + tax.balance_refund
                tax.base_balance = tax.base_balance_regular + tax.base_balance_refund

                tax_name = tax._get_tax_name()
                base_balance = sign * tax.base_balance
                balance = sign * tax.balance

                # Calcolo dei valori detraibili e indetraibili
                balance_regular = tax.compute_balance(
                    tax_or_base="tax", financial_type="regular", account_ids=account_ids
                )
                balance_refund = tax.compute_balance(
                    tax_or_base="tax", financial_type="refund", account_ids=account_ids
                )
                deductible_balance = sign * (balance_regular + balance_refund)

                balance_regular = tax.compute_balance(
                    tax_or_base="tax", financial_type="regular", exclude_account_ids=account_ids
                )
                balance_refund = tax.compute_balance(
                    tax_or_base="tax", financial_type="refund", exclude_account_ids=account_ids
                )
                undeductible_balance = sign * (balance_regular + balance_refund)

                tax_totals.append((tax_name, base_balance, balance, deductible_balance, undeductible_balance))

            tax_totals_mapped_by_journal[journal.id] = tax_totals

        # Infine aggiungo al dizionario di mappatura un'ultima chiave 'totals' con i totali
        totals = dict()
        for journal_id, tax_totals in tax_totals_mapped_by_journal.items():
            for tax_tuple in tax_totals:
                if tax_tuple[0] not in totals:
                    totals[tax_tuple[0]] = tax_tuple
                else:
                    totals[tax_tuple[0]] = list(totals[tax_tuple[0]])
                    totals[tax_tuple[0]][1] += tax_tuple[1]
                    totals[tax_tuple[0]][2] += tax_tuple[2]
                    totals[tax_tuple[0]][3] += tax_tuple[3]
                    totals[tax_tuple[0]][4] += tax_tuple[4]
                    totals[tax_tuple[0]] = tuple(totals[tax_tuple[0]])

        tax_totals_mapped_by_journal['totals'] = list(totals.values())

        docargs['journal_tax_map'] = tax_totals_mapped_by_journal
        return docargs
