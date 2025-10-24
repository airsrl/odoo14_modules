from odoo.exceptions import ValidationError
# from odoo.addons.gls_italy_odoo_integration.models.gls_italy_response import Response
from .gls_italy_response import Response
from odoo import fields, models, api, _
import xml.etree.ElementTree as etree
from requests import request
import binascii
import logging
import base64
import time

_logger = logging.getLogger("GLS Italy")


class StockPicking(models.Model):
    _inherit = "stock.picking"
    gls_state = fields.Selection([('to_send', 'Da inviare'), ('inviato', 'Inviato'), ('annullato', 'Annullato')],
                                 default='to_send', string='Stato gls')
    gentextfile = fields.Binary('xml esempio', readonly=True)
    xml_filename = fields.Char('nome file')
    gls_shippment_status=fields.Selection([('open','Aperto'),('close','Chiuso')],string='Stato pacco')
    integrative_insurance = fields.Selection([('vuoto',''),('A', 'All-in'), ('F', '10/10')], default='vuoto', compute='get_insurance', inverse='_inverse_manual_insurance',store=True)
    @api.depends('sale_id')
    def get_insurance(self,manual=False):
        for rec in self:
            if rec.sale_id.amount_total > 200:
                rec.integrative_insurance='A'
            else:
                rec.integrative_insurance = 'vuoto'

    def _inverse_manual_insurance(self):
        for rec in self:
            priority = rec.integrative_insurance

    def gls_italy_cancel_shipment(self):
        return self.carrier_id.gls_italy_cancel_shipment(self)

    def gls_italy_send(self):
        request_data = self.carrier_id.gls_itlay_create_order_request_data(self)

        if self.carrier_id.prod_environment is True:
            try:

                url = "{}".format(self.company_id and self.company_id.gls_italy_api_url)
                headers = {'SOAPAction': 'https://labelservice.gls-italy.com/AddParcel',
                           'Content-Type': 'application/soap+xml; charset="utf-8"'}
                _logger.info("::: sending request to {0} \n request data {1}".format(url, request_data))
                response_data = request(method="POST", url=url, headers=headers, data=request_data)
                if response_data.status_code in [200, 201]:
                    _logger.info("[success] Getting Successfully response from {}".format(url))
                    response_data = Response(response_data)
                    try:
                        result = response_data.dict()
                    except Exception as error:
                        raise ValidationError(error)
                    parcel_response = result.get('Envelope') and result.get('Envelope').get('Body') and result.get(
                        'Envelope').get('Body').get('AddParcelResponse') and result.get('Envelope').get('Body').get(
                        'AddParcelResponse').get('AddParcelResult') and result.get('Envelope').get('Body').get(
                        'AddParcelResponse').get('AddParcelResult').get('InfoLabel') and result.get('Envelope').get(
                        'Body').get('AddParcelResponse').get('AddParcelResult').get('InfoLabel').get('Parcel')
                    if not parcel_response:
                        raise ValidationError(_(result))
                    if isinstance(parcel_response, list):
                        shipping_number_lst = []
                        for parcel_data in parcel_response:
                            label_number = parcel_data.get('TotaleColli')
                            shipping_number = parcel_data.get('NumeroSpedizione')
                            label_data = parcel_data.get('PdfLabel')
                            if not shipping_number and label_data:
                                raise ValidationError(
                                    _('shipping number and label data not foun in response \n response '
                                      'data {}').format(result))
                            binary_data = binascii.a2b_base64(str(label_data))
                            shipping_number_lst.append(shipping_number)
                            ship_number = "%s_%s" % (shipping_number, label_number)
                            message = (_("Label created!<br/> <b>Shipping  Number : </b>%s<br/>") % (ship_number,))
                            self.message_post(body=message,
                                              attachments=[('Label-%s.%s' % (shipping_number, "pdf"), binary_data)])

                        shipping_data = {'exact_price': 0.0,
                            'tracking_number': ",".join(list(set(shipping_number_lst)))}
                        response = []
                        response += [shipping_data]
                        if self.carrier_tracking_ref:
                            self.carrier_tracking_ref += shipping_data['tracking_number']
                        else:
                            self.carrier_tracking_ref = shipping_number

                        self.gls_state = 'inviato'
                        self.gls_shippment_status ='open'
                        return response
                    else:
                        shipping_number = result.get('Envelope') and result.get('Envelope').get('Body') and result.get(
                            'Envelope').get('Body').get('AddParcelResponse') and result.get('Envelope').get('Body').get(
                            'AddParcelResponse').get('AddParcelResult') and result.get('Envelope').get('Body').get(
                            'AddParcelResponse').get('AddParcelResult').get('InfoLabel') and result.get('Envelope').get(
                            'Body').get('AddParcelResponse').get('AddParcelResult').get('InfoLabel').get(
                            'Parcel') and result.get('Envelope').get('Body').get('AddParcelResponse').get(
                            'AddParcelResult').get('InfoLabel').get('Parcel').get('NumeroSpedizione')
                        if shipping_number:
                            label_data = result.get('Envelope').get('Body').get('AddParcelResponse').get(
                                'AddParcelResult').get('InfoLabel').get('Parcel').get('PdfLabel')
                            if not shipping_number and label_data:
                                raise ValidationError(
                                    _('shipping number and label not found in response \n respnse data {}').format(
                                        result))
                            binary_data = binascii.a2b_base64(str(label_data))
                            message = (_("Label created!<br/> <b>Shipping  Number : </b>%s<br/>") % (shipping_number,))
                            self.message_post(body=message,
                                              attachments=[('Label-%s.%s' % (shipping_number, "pdf"), binary_data)])

                            shipping_data = {'exact_price': 0.0, 'tracking_number': shipping_number}
                            response = []
                            response += [shipping_data]
                            if self.carrier_tracking_ref:
                                self.carrier_tracking_ref += shipping_data['tracking_number']
                            else:
                                self.carrier_tracking_ref = shipping_number

                            self.gls_state = 'inviato'
                            self.gls_shippment_status = 'open'
                            return response
                        else:
                            raise ValidationError(_(result))

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

    def send_to_shipper(self):
        if self.carrier_id and self.carrier_id.delivery_type:
            if self.carrier_id.delivery_type == 'gls_italy':
                return True
            else:
                return super(StockPicking, self).send_to_shipper()
        return super(StockPicking, self).send_to_shipper()


class DeliveryCarrier(models.Model):
    _inherit = 'delivery.carrier'

    delivery_type = fields.Selection(selection_add=[("gls_italy", "GLS Italy")], ondelete={'gls_italy': 'set default'})

    gls_italy_contract_code = fields.Selection([('1', 'Contract Code base'),
                                                ('2', 'Contract Code 2'),
                                                ('3', 'Contract Code 3'),
                                                ('4', 'Contract Code 4'),
                                                ('5', 'Contract Code 5')], default='1', required=True, string='Contract code')

    gls_italy_modalitaIncasso = fields.Selection([('CONT', 'CONT , Contante'),
                                                  ('AC', 'AC, Assegno circolare'), ('AB', 'AB, Assegno bancario'),
                                                  ('AP', 'AP, Assegno postale'),
                                                  ('ASS', 'ASS, Ass postale/bancario/circolare'),
                                                  ('ABP', 'ABP, Ass. bancario/postale'),
                                                  ('ASR', 'ASR, Ass. come rilasciato'),
                                                  ('ARM', 'ARM, Ass. come rilasciato int. Mittente'),
                                                  ('ABC', 'ABC, Ass. bancario/circolare - no postale'),
                                                  ('ASRP', 'ASRP,Ass. come rilasciato - no postale'),
                                                  ('ARMP', 'ARMP, Ass. come rilasciato int. Mittente – no postale ')], string='Modalità incasso')

    gls_italy_port_type = fields.Selection([('F', 'F, Franco'), ('A', 'A, Assegnato')], string="Port Type",
                                           help="Select GLS Port Type")

    gls_italy_shipping_type = fields.Selection([('N', 'N, Nazionale'), ('P', 'P, Parcel Europa e Extracee')],
                                               string="Shipping Type", help="Choose Shipping Type",
                                               default="N")
    gls_packaging_id = fields.Many2one('product.packaging', string="Default Package Type")


    def gls_italy_rate_shipment(self, order):
        return {'success': True, 'price': 0.0, 'error_message': False, 'warning_message': False}

    def gls_itlay_create_order_request_data(self, pickings):
        """
        :parameter pickings
        :return request data for AddParcel API

        """
        sede_gls = pickings.company_id and pickings.company_id.gls_italy_sede
        customer_code = pickings.company_id and pickings.company_id.gls_italy_customer_code
        password_gls = pickings.company_id and pickings.company_id.gls_italy_password
        receiver_id = pickings.partner_id
        contract_code = pickings.company_id and pickings.company_id.gls_italy_contract_code

        # Multi contract code
        if self.gls_italy_contract_code == '2':
            contract_code = pickings.company_id and pickings.company_id.gls_italy_contract_code_2
        if self.gls_italy_contract_code == '3':
            contract_code = pickings.company_id and pickings.company_id.gls_italy_contract_code_3
        if self.gls_italy_contract_code == '4':
            contract_code = pickings.company_id and pickings.company_id.gls_italy_contract_code_4
        if self.gls_italy_contract_code == '5':
            contract_code = pickings.company_id and pickings.company_id.gls_italy_contract_code_5

        if pickings.package_ids:
            parcel_info = ""
            for package_data in pickings.package_ids:
                if package_data.shipping_weight == 0:
                    raise ValidationError(_('package weight must be greater than 0'))
                parcel_data = """<CodiceContrattoGls>{0}</CodiceContrattoGls><RagioneSociale>{1}</RagioneSociale><Indirizzo>{2}</Indirizzo><Localita>{3}</Localita><Zipcode>{4}</Zipcode><Provincia>{5}</Provincia><Bda></Bda><Colli>1</Colli><PesoReale>{6}</PesoReale><TipoPorto>{7}</TipoPorto><CodiceClienteDestinatario /><Email>{8}</Email><ModalitaIncasso>{9}</ModalitaIncasso><DataPrenotazioneGDO /><OrarioNoteGDO /><GeneraPdf>4</GeneraPdf><FormatoPdf /><ContatoreProgressivo>{10}</ContatoreProgressivo><NumDayListSped /><IdentPIN /><TipoSpedizione>{11}</TipoSpedizione><ValoreDichiarato /><PersonaRiferimento /><Contenuto /><TelefonoDestinatario /><CategoriaMerceologica /><FatturaDoganale /><DataFatturaDoganale /><PezziDichiarati /><NazioneOrigine /><TelefonoMittente /><NumeroFatturaCOD /><DataFatturaCOD /><Notespedizione>{12}</Notespedizione><NoteAggiuntive>{12}</NoteAggiuntive><NoteIncoterm />"""
                parcel_data = parcel_data.format(contract_code, receiver_id.name, receiver_id.street, receiver_id.city,
                                                 receiver_id.zip, receiver_id.state_id.code,
                                                 package_data.shipping_weight, self.gls_italy_port_type,
                                                 receiver_id.email or " ", self.gls_italy_modalitaIncasso,
                                                 time.strftime("%d%m%M%S"), self.gls_italy_shipping_type,pickings.note or "")
                if pickings.integrative_insurance !='vuoto':
                    parcel_data += """<AssicurazioneIntegrativa>{0}</AssicurazioneIntegrativa>""".format(pickings.integrative_insurance)
                parcel_info += '<Parcel>'+parcel_data+'</Parcel>'
        else:
            parcel_info = """<CodiceContrattoGls>{0}</CodiceContrattoGls><RagioneSociale>{1}</RagioneSociale><Indirizzo>{2}</Indirizzo><Localita>{3}</Localita><Zipcode>{4}</Zipcode><Provincia>{5}</Provincia><Bda>1</Bda><Colli>1</Colli><Incoterm>0</Incoterm><PesoReale>{6}</PesoReale><TipoPorto>{7}</TipoPorto><CodiceClienteDestinatario /><Email>{8}</Email><ModalitaIncasso>{9}</ModalitaIncasso><DataPrenotazioneGDO /><OrarioNoteGDO /><GeneraPdf>4</GeneraPdf><FormatoPdf /><ContatoreProgressivo>{10}</ContatoreProgressivo><NumDayListSped /><IdentPIN /><TipoSpedizione>{11}</TipoSpedizione><ValoreDichiarato /><PersonaRiferimento /><Contenuto /><TelefonoDestinatario /><CategoriaMerceologica /><FatturaDoganale /><DataFatturaDoganale /><PezziDichiarati /><NazioneOrigine /><TelefonoMittente /><NumeroFatturaCOD /><DataFatturaCOD /><NoteIncoterm /><Notespedizione>{12}</Notespedizione><NoteAggiuntive>{12}</NoteAggiuntive>"""
            parcel_info = parcel_info.format(contract_code, receiver_id.name, receiver_id.street, receiver_id.city,
                                             receiver_id.zip, receiver_id.state_id.code,
                                             self.gls_packaging_id.max_weight, self.gls_italy_port_type,
                                             receiver_id.email or " ", self.gls_italy_modalitaIncasso,
                                             time.strftime("%d%m%M%S"), self.gls_italy_shipping_type,pickings.note or "")
            if pickings.integrative_insurance != 'vuoto':
                parcel_info += """<AssicurazioneIntegrativa>{0}</AssicurazioneIntegrativa>""".format(
                    pickings.integrative_insurance)

            parcel_info += '<Parcel>' + parcel_info + '</Parcel>'
        data = """<Info><SedeGls>{0}</SedeGls><CodiceClienteGls>{1}</CodiceClienteGls><PasswordClienteGls>{2}</PasswordClienteGls>{3}</Info>""".format(
            sede_gls, customer_code, password_gls, parcel_info)

        # __ creating main xml format for call xml api(AddParcel)
        Envelope = etree.Element("Envelope")
        Envelope.attrib['xmlns'] = 'http://www.w3.org/2003/05/soap-envelope'
        Body = etree.SubElement(Envelope, "Body")
        AddParcel = etree.SubElement(Body, "AddParcel")
        AddParcel.attrib['xmlns'] = 'https://labelservice.gls-italy.com/'
        etree.SubElement(AddParcel, "XMLInfoParcel").text = data
        return etree.tostring(Envelope)



    def gls_italy_cancel_shipment(self, picking):
        """
        :return this method cancel the shipment
        """
        SedeGls = picking and picking.company_id and picking.company_id.gls_italy_sede
        CodiceClienteGls = picking and picking.company_id and picking.company_id.gls_italy_customer_code
        PasswordClienteGls = picking and picking.company_id and picking.company_id.gls_italy_password
        if picking.carrier_tracking_ref:
            #to-do correggere numeri di spedizione
            number_list = list(picking.carrier_tracking_ref.split(','))
            for number in picking.carrier_tracking_ref.split(','):
                root_node = etree.Element('soap:Envelope')
                root_node.attrib['xmlns:soap'] = 'http://schemas.xmlsoap.org/soap/envelope/'
                root_node.attrib['xmlns:xsi'] = 'http://www.w3.org/2001/XMLSchema-instance'
                root_node.attrib['xmlns:xsd'] = 'http://www.w3.org/2001/XMLSchema'
                soap_body = etree.SubElement(root_node, 'soap:Body')
                DeleteSped = etree.SubElement(soap_body, 'DeleteSped')
                DeleteSped.attrib['xmlns'] = 'https://labelservice.gls-italy.com/'
                etree.SubElement(DeleteSped, 'SedeGls').text = "{}".format(SedeGls)
                etree.SubElement(DeleteSped, 'CodiceClienteGls').text = "{}".format(CodiceClienteGls)
                etree.SubElement(DeleteSped, 'PasswordClienteGls').text = "{}".format(PasswordClienteGls)
                etree.SubElement(DeleteSped, 'NumSpedizione').text = "{}".format(number)
                request_data = etree.tostring(root_node)
                if self.prod_environment is True:
                    try:
                        url = "{}".format(picking.company_id and picking.company_id.gls_italy_api_url)
                        headers = {'Content-Type': 'text/xml; charset=utf-8',
                                   'SOAPAction': 'https://labelservice.gls-italy.com/DeleteSped'}
                        response_data = request(method="POST", url=url, data=request_data, headers=headers)
                        if response_data.status_code in [200, 201, 202]:
                            _logger.info(":: get successfully response from {}".format(url))
                            response_data = Response(response_data).dict()
                            # response_data = response_data.get('Envelope').get('Body').get('DeleteSpedResponse').get('DeleteSpedResult').get('DescrizioneErrore')
                            _logger.info("successfully delete the shipment")
                            number_list.pop(number_list.index(number))
                            message = (_("Successfully delete the shipment:%s" % number))
                            picking.message_post(body=message,
                                              )


                        else:
                            raise ValidationError(
                                _('getting some error from %s \n response data %s') % (url, response_data.text))
                    except Exception as error:
                        raise ValidationError(_(error))
                else:
                    number_list.pop(number_list.index(number))
                    data = request_data
                    xml_filename = 'annullato.xml'
                    picking.write(
                        {'gentextfile': base64.b64encode(data), 'xml_filename': xml_filename, 'gls_state': 'annullato'})
            tracking_ref= ' '.join([str(elem) for elem in number_list])
            picking.write({'gls_state': 'annullato','carrier_tracking_ref':tracking_ref})
    def gls_italy_get_tracking_link(self, pickings):
        url = "https://www.gls-italy.com/?option=com_gls&view=track_e_trace&mode=search&numero_spedizione=%s" % pickings.carrier_tracking_ref
        return url
