from odoo import api, fields, models
from odoo.exceptions import UserError
import requests
import json


class OpenapiEngine(models.Model):
    _name = "openapi.engine"
    _description = "Engine of the interaction between openapi and Odoo"

    name = fields.Char(
        string="Nome",
        default="OpenAPI Engine"
    )
    token = fields.Char(
        string="Token",
        compute="_fetch_tokens_from_settings"
    )
    sandbox_token = fields.Char(
        string="Token sandbox",
        compute="_fetch_tokens_from_settings"
    )
    production = fields.Boolean(
        string="Credenziali di produzione attive",
        compute="_compute_production"
    )
    endpoint_ids = fields.One2many(
        comodel_name="openapi.engine.endpoint",
        inverse_name="engine_id",
        string="Endpoints"
    )

    @property
    def headers(self) -> dict:
        return {"Authorization": f"Bearer {self.token if self.production else self.sandbox_token}"}

    def _compute_production(self):
        prod_param = self.env['ir.config_parameter'].sudo().get_param('account_online_synchronization.proxy_mode')
        force_credentials = self.env['ir.config_parameter'].sudo().get_param('huroos_openapi.openapi_force_credentials')
        production = True if prod_param == "production" else False
        for engine in self:
            engine.production = production if not force_credentials else not production

    def _fetch_tokens_from_settings(self):
        token = self.env['ir.config_parameter'].sudo().get_param('huroos_openapi.openapi_token')
        sandbox_token = self.env['ir.config_parameter'].sudo().get_param('huroos_openapi.openapi_sandbox_token')
        for engine in self:
            engine.token = token
            engine.sandbox_token = sandbox_token

    def endpoint(self, endpoint: str) -> models.Model:
        endpoint = self.endpoint_ids.filtered(lambda x: x.name == endpoint)
        if endpoint:
            return endpoint[0]
        else:
            raise UserError(f"Endpoint {endpoint} non trovato. È sicuramente un problema di configurazione, "
                            f"contattare l'amministratore di sistema per risolvere.")


class OpenapiEngineEndpoint(models.Model):
    _name = "openapi.engine.endpoint"
    _description = "Endpoint of an OpenAPI function"

    engine_id = fields.Many2one(
        comodel_name="openapi.engine",
        string="OpenAPI Engine"
    )
    sequence = fields.Integer(
        string="Sequenza",
        help="Attualmente inutilizzata, serve solo per un ordine visivo."
    )
    name = fields.Char(
        string="Endpoint",
        required=True
    )
    library = fields.Char(
        string="Libreria API",
        required=True,
        help="Es: company, risk, visurecamerali, ecc..."
    )
    numbercall = fields.Integer(
        string="N° di chiamate",
        compute="_compute_numbercall"
    )
    success = fields.Integer(
        string="N° di successi"
    )
    errors = fields.Integer(
        string="N° di errori"
    )
    func = fields.Char(
        string="Metodo",
        required=True,
        help="Metodo eseguito quando viene chiamato l'endpoint. Bisogna inserire solo l'oggetto del metodo, "
             "non chiamarlo (es: metodo_test -> senza parentesi)."
    )

    _sql_constraints = [
        ('endpoint_unique', 'UNIQUE(name)', "L'endpoint deve essere univoco.")
    ]

    @property
    def base_url(self) -> str:
        self.ensure_one()
        domain = "it" if self.library == "visurecamerali" else "com"
        if self.engine_id.production:
            return f"https://{self.library}.openapi.{domain}{self.name}"
        else:
            return f"https://test.{self.library}.openapi.{domain}{self.name}"

    @api.constrains('name')
    def _check_endpoint_name(self):
        for endpoint in self:
            if not endpoint.name.startswith("/"):
                raise UserError(f"Il nome dell'endpoint {endpoint.name} deve iniziare con '/'.")

    @api.depends('success', 'errors')
    def _compute_numbercall(self):
        for endpoint in self:
            endpoint.numbercall = endpoint.success + endpoint.errors

    def call(self, **kwargs):
        self.ensure_one()

        try:
            response = getattr(self, self.func)(**kwargs)
            if response and isinstance(response, dict) and response.get("success", False):
                self.success += 1
            else:
                self.errors += 1

        except Exception as ex:
            raise UserError(f"Qualcosa è antato storto durante l'esecuzione del metodo {self.func} "
                            f"per l'endpoint {self.name}:\n{ex}")

        else:
            return response

    def fetch_data_from_vat_or_cf(self, code: str):
        response = requests.get(f"{self.base_url}/{code}", headers=self.engine_id.headers)
        return json.loads(response.text)

    def manage_ordinaria_societa_capitale(self, payload: dict = None, request_id: str = None, get_attachment: bool = False):
        # Se non passo nulla significa che voglio ottenere un elenco di mie richieste di visure camerali
        if not payload and not request_id and not get_attachment:
            response = requests.get(self.base_url, headers=self.engine_id.headers)
            return json.loads(response.text)

        # Se c'è il payload significa che voglio fare la POST del C.F./P.IVA per ottenere l'id della richiesta
        elif payload is not None and isinstance(payload, dict) and payload.get('cf_piva_id'):
            headers = self.engine_id.headers
            headers["content-type"] = "application/json"
            response = requests.post(self.base_url, json=payload, headers=headers)
            return json.loads(response.text)

        # Se c'è l'id della richiesta ma non il nome del file significa che voglio ottenere il file tramite id
        elif request_id is not None and not get_attachment:
            response = requests.get(f"{self.base_url}/{request_id}", headers=self.engine_id.headers)
            return json.loads(response.text)

        # Se c'è sia l'id che il nome del file voglio ottenere i bytes del file
        elif request_id is not None and get_attachment:
            response = requests.get(f"{self.base_url}/{request_id}/allegati", headers=self.engine_id.headers)
            return json.loads(response.text)

        else:
            raise Exception(f"Parametri del metodo non corretti.\npayload = {str(payload)}\nrequest_id = {request_id}"
                            f"\nget_attachment = {get_attachment}")
