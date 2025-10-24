from odoo.exceptions import ValidationError
#from odoo.addons.gls_italy_odoo_integration.models.gls_italy_response import Response
from .gls_italy_response import Response
from odoo import fields, models, api, _
import xml.etree.ElementTree as etree
from requests import request
import binascii
import logging
import base64
import time
import re
_logger = logging.getLogger("GLS Italy")

class StockPicking(models.Model):
    _inherit = "stock.picking"

    def automated_close_workday(self):

        pickings= self.env.search([('gls_state','=','inviato')])
        for picking in pickings:
            picking.gls_close_workday()

    def gls_close_workday(self):
        request_data = self.carrier_id.gls_italy_create_order_request_workday_data(self)
        # note = '%s' % (request_data)
        # self.message_post(body=note)
       #self.gls_state = 'inviato'
        if self.carrier_id.prod_environment is True:
            try:

                url = "{}".format(self.company_id and self.company_id.gls_italy_api_url)
                headers = {'SOAPAction': 'https://labelservice.gls-italy.com/CloseWorkDayByShipmentNumber',
                           'Content-Type': 'text/xml; charset="utf-8"'}
                _logger.info("::: sending request to {0} \n request data {1}".format(url, request_data))
                response_data = request(method="POST", url=url, headers=headers, data=request_data)
                if response_data.status_code in [200, 201]:
                    _logger.info("[success] Getting Successfully response from {}".format(url))
                    response_data = Response(response_data)
                    try:
                        result = response_data.dict()
                    except Exception as error:
                        raise ValidationError(error)
                    parcel_response = Response(response_data).dict()
                    parcel_response = parcel_response.get('Envelope').get('Body').get('CloseWorkDayByShipmentNumberResponse').get('CloseWorkDayByShipmentNumberResult').get('CloseWorkDayByShipmentNumberResult').get('DescrizioneErrore')
                    if parcel_response == 'OK':
                        parcel_response =f"Numero spedizione confermata: { result.get('Envelope').get('Body').get('CloseWorkDayByShipmentNumberResponse').get('CloseWorkDayByShipmentNumberResult').get('CloseWorkDayByShipmentNumberResult').get('Parcel').get('NumeroDiSpedizioneGLSDaConfermare')}\
                                         Esito : {result.get('Envelope').get('Body').get('CloseWorkDayByShipmentNumberResponse').get('CloseWorkDayByShipmentNumberResult').get('CloseWorkDayByShipmentNumberResult').get('Parcel').get('esito')}"
                        self.gls_shippment_status='close'

                    if not parcel_response:
                        raise ValidationError(_(result))

                    else:
                        message = (_("Shipping sent to Gls, Close work-day result :%s" % parcel_response))
                        self.message_post(body=message,
                                         )




                else:
                    raise ValidationError(
                        "Getting Some Error From {} \n response data {}".format(url, response_data.text))
            except Exception as error:
                raise ValidationError(error)
        else:
            data = request_data
            xml_filename = (f'{self.partner_id.name}-{self.name}.xml').lower()
            return self.write({'gentextfile': base64.b64encode(data), 'xml_filename': xml_filename,
                               'carrier_tracking_ref': f'0000000'})
class DeliveryCarrier(models.Model):
    _inherit = 'delivery.carrier'


    def gls_italy_create_order_request_workday_data(self, pickings):
        """
        :parameter pickings
        :return request data for CloseWorkDay API

        """
        sede_gls = pickings.company_id and pickings.company_id.gls_italy_sede
        customer_code = pickings.company_id and pickings.company_id.gls_italy_customer_code
        password_gls = pickings.company_id and pickings.company_id.gls_italy_password


        if pickings.package_ids:
            parcel_info = ""
            for package_data in pickings.package_ids:

                if package_data.shipping_weight == 0:

                    raise ValidationError(_('package weight must be greater than 0'))
                for number in pickings.carrier_tracking_ref.split(','):
                    parcel_data = """
                                  <Parcel>
                                  <NumeroDiSpedizioneGLSDaConfermare>{0}</NumeroDiSpedizioneGLSDaConfermare>
                               </Parcel>""".format(number)
                    parcel_info += parcel_data
        else:
            for number in pickings.carrier_tracking_ref.split(','):
                parcel_info = """
                              <Parcel>
                                  <NumeroDiSpedizioneGLSDaConfermare>{0}</NumeroDiSpedizioneGLSDaConfermare>
                               </Parcel>""".format(number)
        data = """
                <Info>
                   <SedeGls>{0}</SedeGls>
                   <CodiceClienteGls>{1}</CodiceClienteGls>
                   <PasswordClienteGls>{2}</PasswordClienteGls>
                   {3}
                </Info>
           """.format(sede_gls, customer_code, password_gls, parcel_info)

        # __ creating main xml format for call xml api(CloseWorkDay)
        data=re.sub(r"\s+", "", data)
        Envelope = etree.Element("Envelope")
        Envelope.attrib['xmlns'] = 'http://schemas.xmlsoap.org/soap/envelope/'
        Body = etree.SubElement(Envelope, "Body")
        CloseWorkDay = etree.SubElement(Body, "CloseWorkDayByShipmentNumber")
        CloseWorkDay.attrib['xmlns'] = 'https://labelservice.gls-italy.com/'
        etree.SubElement(CloseWorkDay, "_xmlRequest").text = data
        return etree.tostring(Envelope)
#schema
# <Info>
# <SedeGls></SedeGls>
# <CodiceClienteGls></CodiceClienteGls>
# <PasswordClienteGls></PasswordClienteGls>
# <Parcel>
# <NumeroDiSpedizioneGLSDaConfermare></NumeroDiSpedizioneGLSDaConfermare>
# …
# </Parcel>
# <Parcel>
# <NumeroDiSpedizioneGLSDaConfermare></NumeroDiSpedizioneGLSDaConfermare>
# …
# </Parcel>
# </Info>