from odoo.http import Controller, route, request


class ControllerVisuraCamerale(Controller):

    @route("/visure-camerali/refresh", type='json', auth="none", csrf=False)
    def refresh_visure_camerali(self):
        openapi_engine = request.env.ref('huroos_openapi.openapi_engine_main').sudo()
        data = openapi_engine.endpoint("/ordinaria-societa-capitale").call()
        if data and data.get('data') and data.get('success'):
            visure_camerali = data['data']
        else:
            raise Exception(data.get('message', "Qualcosa è andato storto durante la raccolta dati delle visure."))

        existing_visure_camerali = request.env['res.partner.visura.camerale'].sudo().search([('active', 'in', (True, False))])
        visure_to_create = list()
        for visura in visure_camerali:
            visura_vals = {
                'name': visura['id'],
                'type': visura['tipo'],
                'state': visura['stato_richiesta'],
                'cf_piva_id': visura['cf_piva_id']
            }
            if visura['id'] not in existing_visure_camerali.mapped("name"):
                visure_to_create.append(visura_vals)
            else:
                visura_vals.pop("name")
                existing_visure_camerali.filtered(lambda v: v.name == visura['id'] and v.active).write(visura_vals)

        if visure_to_create:
            request.env['res.partner.visura.camerale'].sudo().create(visure_to_create)
