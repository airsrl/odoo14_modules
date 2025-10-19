from odoo import fields, models, api
import math

class ReportProforma(models.AbstractModel):
    _name = 'report.huroos_shippypro_connector.etichette_consegna_report'
    _description = 'stampa pro-forma Report'

    def divide_line(self,reports):
        list_rep=[]
        prov_reports = reports.copy()
        for rep in reports:
            if len(list_rep)==2:
                continue
            else:
                rep_object= self.env['stock.picking'].browse(rep)
                list_rep.append(rep_object)
                prov_reports.remove(rep)
                if len(prov_reports) == 0:
                    return list_rep, []
        return list_rep, prov_reports



    def _get_report_values(self, docids, data=None):
        docs = self.env['stock.picking'].browse(docids)

        reports = [doc.id for doc in docs]
        list_report=[]
        le_righe=len(docs)/2 if len(docs) >= 2 else len(docs)
        le_righe = int(math.ceil(le_righe))
        for i in range(le_righe):
                righe,report_provv=self.divide_line(reports)
                reports =report_provv
                if len(righe)>0:
                    list_report.append(righe)
                if not reports:
                    continue



        data_dict = {'righe':righe,'list_report':list_report}

        return {
            'doc_ids': docs.ids,
            'doc_model': 'stock.picking',
            'docs': docs,
            'data_dict': data_dict,

        }
