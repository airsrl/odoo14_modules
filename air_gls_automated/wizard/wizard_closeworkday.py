from odoo import fields, models, api,_
from odoo.exceptions import (
    AccessDenied,
    AccessError,
    MissingError,
    UserError,
    ValidationError,
)
class WizardCloseDay(models.TransientModel):
    _name = 'wizard.close.day'

    name = fields.Selection([('close','Chiudi spedizioni'),('send','Invia a GLS')],default='send',string='Tipo operazione',required=True)
    picking_ids=fields.Many2many('stock.picking')

    @api.onchange('name')
    def get_domain(self):
        self.picking_ids=[(6,0,[])]
        res={}
        if self.name == 'close':
            domain=[('gls_state','=','inviato'),('carrier_id.delivery_type','=', 'gls_italy'),('gls_shippment_status','!=','close')]
        else:
            domain=[('gls_state', '!=', 'inviato'), ('carrier_id.delivery_type', '=', 'gls_italy'), (
            'gls_shippment_status', '!=', 'close')]
        res['domain'] ={'picking_ids':domain}
        return res
    def button_close_work_day(self):
        for picking in self.picking_ids:
            try:
                picking.gls_close_workday()
            except Exception as ex:
                raise UserError('La spedizione {} non è stata chiusa per {}.'.format(picking.name,_(ex)))
    def button_send_gls(self):
        for picking in self.picking_ids:
            try:
                picking.gls_italy_send()
            except Exception as ex:
                raise UserError('La spedizione {} non è stata inviata per {}.'.format(picking.name,_(ex)))
    # def request_workday_data(self,pickings):
    #
    #         """
    #         :return request data for CloseWorkDay API
    #
    #         """
    #
    #         sede_gls = pickings.company_id and pickings.company_id.gls_italy_sede
    #         customer_code = pickings.company_id and pickings.company_id.gls_italy_customer_code
    #         password_gls = pickings.company_id and pickings.company_id.gls_italy_password
    #
    #         parcel_info = ""
    #         for picking in pickings:
    #
    #             if picking.package_ids:
    #
    #                 for package_data in picking.package_ids:
    #
    #                     if package_data.shipping_weight == 0:
    #                         raise ValidationError(_('package weight must be greater than 0'))
    #                     for number in picking.carrier_tracking_ref.split(','):
    #                         parcel_data = """
    #                                       <Parcel>
    #                                       <NumeroDiSpedizioneGLSDaConfermare>{0}</NumeroDiSpedizioneGLSDaConfermare>
    #                                    </Parcel>""".format(number)
    #                         parcel_info += parcel_data
    #             else:
    #                 for number in picking.carrier_tracking_ref.split(','):
    #                     parcel_data = """ <Parcel>
    #                                             <NumeroDiSpedizioneGLSDaConfermare>{0}</NumeroDiSpedizioneGLSDaConfermare>
    #                                     </Parcel>""".format(number)
    #                     parcel_info += parcel_data
    #         data = """
    #                 <Info>
    #                    <SedeGls>{0}</SedeGls>
    #                    <CodiceClienteGls>{1}</CodiceClienteGls>
    #                    <PasswordClienteGls>{2}</PasswordClienteGls>
    #                    {3}
    #                 </Info>
    #            """.format(sede_gls, customer_code, password_gls, parcel_info)
    #
    #         # __ creating main xml format for call xml api(CloseWorkDay)
    #         data = re.sub(r"\s+", "", data)
    #         Envelope = etree.Element("Envelope")
    #         Envelope.attrib['xmlns'] = 'http://schemas.xmlsoap.org/soap/envelope/'
    #         Body = etree.SubElement(Envelope, "Body")
    #         CloseWorkDay = etree.SubElement(Body, "CloseWorkDayByShipmentNumber")
    #         CloseWorkDay.attrib['xmlns'] = 'https://labelservice.gls-italy.com/'
    #         etree.SubElement(CloseWorkDay, "_xmlRequest").text = data
    #         return etree.tostring(Envelope)
