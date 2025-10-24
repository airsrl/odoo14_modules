
import pandas as pd
from odoo import models, api, _, fields
from ..Utilities import LoggingUtils as lu
from odoo.exceptions import ValidationError, UserError
import logging
# import config
import base64
import io
import sys

if sys.version_info >= (3, 6):
    import zipfile
else:
    import zipfile36 as zipfile

# v12
# lista_campi = {'Sku_Padre': 0, 'Sku_Prodotto': 1, 'Nome': 2, 'Categoria': 3,
#                'Barcode': 4, 'Descrizione_vendite': 5, 'Note_interne': 6,
#                'Può_essere_venduto': 7, 'Può_essere_acquistato': 8,
#                'Attributo_1': 9, 'Varianti_attr._1': 10, 'Attributo_2': 11,
#                'Varianti_attr._2': 12, 'Attributo_3': 13,
#                'Varianti_attr._3': 14, 'Attributo_4': 15,
#                'Varianti_attr._4': 16, 'Attributo_5': 17,
#                'Varianti_attr._5': 18, 'Prezzo_vendita': 19,
#                'Iva_%': 20,
#                'Forn._Codice': 21,
#                'Forn._Nome': 22, 'Forn._Costo': 23, 'Forn._Tempo_cons._(gg)': 24,
#                'Politica_fatturazione': 25, 'Qtà_in_magazzino': 26, 'Unità_di_misura': 27, 'Marchio': 28,
#                'Categoria_e-commerce': 29, 'Brochure': 30, 'Manuale': 31, 'Produttore': 32, 'Desc_ecommerce': 33,
#                'Variante_default': 34}
# V14
_logger = logging.getLogger(__name__)

lista_campi = {'Sku_Padre': 0,
               'Sku_Prodotto': 1,
               'Nome': 2,
               'Categoria': 3,
               'Barcode': 4,
               'Descrizione_vendite': 5,
               'Note_interne': 6,
               'Può_essere_venduto': 7,
               'Può_essere_acquistato': 8,
               'Attributo_1': 9,
               'Varianti_attr._1': 10,
               'Attributo_2': 11,
               'Varianti_attr._2': 12,
               'Attributo_3': 13,
               'Varianti_attr._3': 14,
               'Attributo_4': 15,
               'Varianti_attr._4': 16,
               'Attributo_5': 17,
               'Varianti_attr._5': 18,
               'Prezzo_vendita': 19,
               'Iva_%': 20,
               'Forn._Codice': 21,
               'Forn._Nome': 22,
               'Forn._Costo': 23,
               'Forn._Tempo_cons._(gg)': 24,
               'Politica_fatturazione': 25,
               'Qtà_in_magazzino': 26,
               'Unità_di_misura': 27}

lista_extra_tmpl = {}  # campi produc.template
lista_extra = {}  # tutti i campi product.product


class ImportProductWizard(models.TransientModel):
    _name = 'product.import.wizard'
    _description = 'Wizard importazione prodotti da file Excel'

    import_file = fields.Binary(
        string='Import File (*.xls)', attachment=True
    )
    file_name = fields.Char("File Name")
    res_id = fields.Integer(
        string='Resource ID',
        readonly=True,
    )
    res_model = fields.Char(
        string='Resource Model',
        readonly=True,
        size=500,
    )
    error = fields.Text('Errori')
    check_column = fields.Boolean('Controllo colonne')

    def get_decimal_from_string(self, string_value):
        if not string_value or str(string_value) == '':
            return 0
        else:
            string_value = str(string_value).replace(',', '.')
            return float(string_value)

    def check_data_columns(self):
        if not self.import_file:
            raise UserError('Nessun file Excel caricato.')

        lu.LogInfo('check_data_columns')

        # CONTROLLA? E SALVA LE COLONNE PER ESSERE UTILIZZATE SUCCESSIVAMENTE
        global lista_extra_tmpl
        global lista_extra
        decoded_data = base64.decodebytes(self.import_file)
        data = pd.read_excel(io=decoded_data, parse_dates=True,
                             keep_default_na=False)  # keep_default_na= False serve per rimuovere i nan
        columns = data.columns
        titoli = list(columns)
        ultima_key = list(lista_campi.keys())[-1]
        ultimo_index = lista_campi[ultima_key] + 1
        num_colonne = len(columns)
        if num_colonne > ultimo_index:
            # todo continue
            differenza = list(range(ultimo_index, num_colonne))
            for diff in differenza:
                field_name = titoli[diff]
                if field_name in self.env['product.template']._fields:
                    lista_extra_tmpl[field_name] = diff

        self.check_column = True
        wiz_id = self.env.ref('import_products_excel.import_product_xls').id

        return {
            'name': _('Continua'),
            # 'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'product.import.wizard',
            'res_id': self.id,
            'views': [(wiz_id, 'form')],
            'type': 'ir.actions.act_window',
            'target': 'new'
        }

    def log(self, message, level="info", action_name=None):
        with self.pool.cursor() as cr:
            cr.execute("""
                INSERT INTO ir_logging(create_date, create_uid, type, dbname, name, level, message, path, line, func)
                VALUES (NOW() at time zone 'UTC', %s, %s, %s, %s, %s, %s, %s,'0',  %s)
            """, (self.env.uid, 'server', self._cr.dbname, __name__, level, message, "action", action_name)) # %s,#action.id,

    def ImportExcelProdottiRettificata(self):
        global lista_extra
        global lista_extra_tmpl

        lu.LogInfo(f'Leggo file excel')
        error = []
        productName = ''
        codice = ''

        self.GetFieldType("product.template", 'collezione')

        try:
            decoded_data = base64.decodebytes(self.import_file)
            data = pd.read_excel(io=decoded_data, parse_dates=True, keep_default_na=False)  # keep_default_na= False serve per rimuovere i nan
            data.columns = [column.strip().replace(" ", "_") for column in data.columns]
            self.check_data_columns()
            # recupero modelli
            m_product_template = self.env['product.template'].sudo()
            m_product_product = self.env['product.product'].sudo()

            recordsPadre = data.query("Sku_Padre == Sku_Prodotto | Sku_Padre == '' | Sku_Padre == ' ' ")
            recordsFiglio = data.query(" Sku_Padre != Sku_Prodotto & Sku_Padre != ['',' '] ")

            lu.LogInfo(f'Num righe nel file: {len(data.values)}. Num prodotti: {len(recordsPadre.values)} Varianti: {len(recordsFiglio.values)}')
            self.log(level=logging.INFO, message=f'Num righe nel file: {len(data.values)}. Num prodotti: {len(recordsPadre.values)} Varianti: {len(recordsFiglio.values)}', action_name='ImportExcelProdottiRettificata')
            numElaborati = 0
        except Exception as e:
            lu.LogError(f'Errore: {e}')
            info = f'Errore nella lettura del file:{_(e)}'

            if info:
                error.append(info)
            raise UserError(info)

        # * =======================================================
        # * ================ RIGHE PRODOTTI PADRE =================
        # * =======================================================
        lu.LogInfo(f'Elaboro i prodotti padre')
        for record in recordsPadre.values:
            try:
                # Leggo i valori della riga
                listPrice = self.get_decimal_from_string(record[lista_campi['Prezzo_vendita']]) if record[lista_campi['Prezzo_vendita']] else 1
                productName = str(record[lista_campi['Nome']]).strip()
                codice = str(record[lista_campi['Sku_Prodotto']]).strip()
                nomeFornitore = str(record[lista_campi['Forn._Nome']]).strip()
                codiceFornitore = record[lista_campi['Forn._Codice']]
                prezzoAcquisto = self.get_decimal_from_string(record[lista_campi['Forn._Costo']])
                note = record[lista_campi['Note_interne']]
                categoria = record[lista_campi['Categoria']]
                barcode = record[lista_campi['Barcode']]
                descrizioneVendite = record[lista_campi['Descrizione_vendite']]
                uom = str(record[lista_campi['Unità_di_misura']]).strip()
                iva = self.get_decimal_from_string(record[lista_campi['Iva_%']]) if record[lista_campi['Iva_%']] else False
                isSaleable = str(record[lista_campi['Può_essere_venduto']]).strip()
                isSaleable = isSaleable and isSaleable.lower() != 'no'
                isPurchasable = str(record[lista_campi['Può_essere_acquistato']]).strip()
                isPurchasable = isPurchasable and isPurchasable.lower() != 'no'
                fornTempoconsegna = int(record[lista_campi['Forn._Tempo_cons._(gg)']]) if record[lista_campi['Forn._Tempo_cons._(gg)']] else 0

                # Attributi/varianti
                attributeOne = str(record[lista_campi['Attributo_1']]).strip()
                variantOne = str(record[lista_campi['Varianti_attr._1']]).strip()
                attributeTwo = str(record[lista_campi['Attributo_2']]).strip()
                variantTwo = str(record[lista_campi['Varianti_attr._2']]).strip()
                attributeThree = str(record[lista_campi['Attributo_3']]).strip()
                variantThree = str(record[lista_campi['Varianti_attr._3']]).strip()
                attributeFourth = str(record[lista_campi['Attributo_4']]).strip()
                variantFourth = str(record[lista_campi['Varianti_attr._4']]).strip()
                attributeFifth = str(record[lista_campi['Attributo_5']]).strip()
                variantFifth = str(record[lista_campi['Varianti_attr._5']]).strip()

                # Quantità magazzino
                qtyDisponibile = self.get_decimal_from_string(record[lista_campi['Qtà_in_magazzino']])
                invoice_policy = str(record[lista_campi['Politica_fatturazione']]).strip().lower()

                if 'consegnate' in invoice_policy:
                    invoice_policy = 'delivery'
                elif 'ordinate' in invoice_policy:
                    invoice_policy = 'order'
                else:
                    invoice_policy = None

                product = {'name': productName, 'default_code_import': codice, 'default_code': codice}

                lu.LogInfo(f'lista_extra_tmpl {lista_extra_tmpl}')
                lu.LogInfo(f'lista_extra {lista_extra}')

                if lista_extra_tmpl:
                    for item, values in lista_extra_tmpl.items():
                        field_type, relation = self.GetFieldType("product.template", item)
                        lu.LogInfo(f'field_type: {str(field_type)} relation: {str(relation)}')

                        if field_type == 'many2one':
                            product[item] = self.GetOrCreateMany2one(relation, str(record[values]).strip())
                        elif field_type == 'many2many':
                            product[item] = self.GetOrCreateMany2many(relation, str(record[values]).strip())
                        else:
                            product[item] = str(record[values]).strip()

                if invoice_policy:
                    product['invoice_policy'] = invoice_policy

                product['type'] = 'product'
                if categoria:
                    categoria = self.GetOrCreateCategory(categoria)
                    product['categ_id'] = categoria.id

                product['list_price'] = listPrice
                costo_acquisto = prezzoAcquisto if prezzoAcquisto else 0

                product['standard_price'] = costo_acquisto
                product['description'] = note
                product['description_sale'] = descrizioneVendite
                product['sale_ok'] = isSaleable
                product['purchase_ok'] = isPurchasable
                if iva:
                    taxes_id = self.GetIva(iva)
                    if taxes_id:
                        product['taxes_id'] = [(6, 0, taxes_id.ids)]
                    supplier_taxes_id = self.GetIva(iva, 'purchase')
                    if supplier_taxes_id:
                        product['supplier_taxes_id'] = [(6, 0, supplier_taxes_id.ids)]
                if uom:
                    uom_id = self.GetUom(uom)
                    product['uom_id'] = uom_id
                    product['uom_po_id'] = uom_id

                # Cerco il prodotto per codice, e poi per nome
                product_id = m_product_template.search([('default_code_import', '=', product['default_code'])], limit=1)
                # if not product_id:
                #     product_id = m_product_template.search([('name', '=', productName)], limit=1)

                lu.LogInfo(f'product_id per codice  {product_id}')
                if not product_id:
                    product_id = self.env['product.product'].search([('default_code', '=', product['default_code'])], limit=1)
                    if product_id:
                        product_id = product_id.product_tmpl_id
                if not product_id:
                    if barcode:
                        if barcode:
                            existing_bc = m_product_product.search([('barcode', '=', barcode)], limit=1)
                            if existing_bc:
                                lu.LogWarn(
                                    f'Esiste già un prodotto con barcode {barcode}: {existing_bc.id} - {existing_bc.name}')
                                sike = f'Esiste già un prodotto con barcode {barcode}: {existing_bc.id} - {existing_bc.name}'
                                error.append(sike)
                            else:
                                product['barcode'] = barcode

                if not product_id:
                    try:
                        product_id = m_product_template.sudo().create(product)
                        lu.LogInfo(f'create {product["default_code"]} {product["name"][0:10]}: {product_id.id}')
                    except Exception as e:
                        lu.LogError(f'Errore INS prodotto {product} {e}')
                        info = f'Errore INS prodotto {product} {e}'
                        if info:
                            error.append(info)
                else:
                    try:
                        product_id.sudo().write(product)
                        lu.LogInfo(f'write {product["default_code"]}  {product["name"][0:10]}: {product_id.id}')
                    except Exception as e:
                        lu.LogError(f'Errore UPD prodotto {product} {e}')

                proPrd = m_product_product.search([('product_tmpl_id', '=', product_id.id)])
                if len(proPrd) == 1:
                    if lista_extra:
                        for item, values in lista_extra.items():
                            field_type, relation = self.GetFieldType("product.template", item)
                            lu.LogInfo(f'field_type: {str(field_type)} relation: {str(relation)}')

                            if field_type == 'many2one':
                                product[item] = self.GetOrCreateMany2one(relation, str(record[values]).strip())
                            elif field_type == 'many2many':
                                product[item] = self.GetOrCreateMany2many(relation, str(record[values]).strip())
                            else:
                                product[item] = str(record[values]).strip()
                    if float(qtyDisponibile) > 0.0:
                        wiz_qty = self.env['stock.change.product.qty'].sudo().create({'product_id': proPrd.id, 'new_quantity': qtyDisponibile, 'product_tmpl_id': proPrd.product_tmpl_id.id})
                        wiz_qty.change_product_qty()

                # se ci sono varianti
                if attributeOne and variantOne:
                    attributo = self.get_attribute(attributeOne)
                    values_ids = []
                    values = variantOne.split(',')
                    for val in values:
                        val = val.strip()
                        variante_id = self.get_variante(attributo, val)
                        values_ids.append(variante_id.id)
                    if product_id.attribute_line_ids:
                        attribute = product_id.attribute_line_ids.filtered(lambda x: x.attribute_id.id == attributo)
                        if attribute:
                            attribute.update({'value_ids': [(6, 0, values_ids)]})
                        else:
                            product_id.sudo().write({'attribute_line_ids': [(0, 0, {'attribute_id': attributo, 'value_ids': [(6, 0, values_ids)]})]})
                    else:
                        product_id.sudo().write({'attribute_line_ids': [(0, 0, {'attribute_id': attributo, 'value_ids': [(6, 0, values_ids)]})]})

                if attributeTwo and variantTwo:
                    attributo = self.get_attribute(attributeTwo)
                    values_ids = []
                    values = variantTwo.split(',')
                    for val in values:
                        val = val.strip()
                        variante_id = self.get_variante(attributo, val)
                        values_ids.append(variante_id.id)
                    if product_id.attribute_line_ids:
                        attribute = product_id.attribute_line_ids.filtered(lambda x: x.attribute_id.id == attributo)
                        if attribute:
                            attribute.update({'value_ids': [(6, 0, values_ids)]})
                        else:
                            product_id.sudo().write({'attribute_line_ids': [
                                (0, 0, {'attribute_id': attributo, 'value_ids': [(6, 0, values_ids)]})]})
                    else:
                        product_id.sudo().write({'attribute_line_ids': [
                            (0, 0, {'attribute_id': attributo, 'value_ids': [(6, 0, values_ids)]})]})

                if attributeThree and variantThree:
                    attributo = self.get_attribute(attributeThree)
                    values_ids = []
                    values = variantThree.split(',')
                    for val in values:
                        val = val.strip()
                        variante_id = self.get_variante(attributo, val)
                        values_ids.append(variante_id.id)
                    if product_id.attribute_line_ids:
                        attribute = product_id.attribute_line_ids.filtered(lambda x: x.attribute_id.id == attributo)
                        if attribute:
                            attribute.update({'value_ids': [(6, 0, values_ids)]})
                        else:
                            product_id.sudo().write({'attribute_line_ids': [
                                (0, 0, {'attribute_id': attributo, 'value_ids': [(6, 0, values_ids)]})]})
                    else:
                        product_id.sudo().write({'attribute_line_ids': [
                            (0, 0, {'attribute_id': attributo, 'value_ids': [(6, 0, values_ids)]})]})

                if attributeFourth and variantFourth:
                    attributo = self.get_attribute(attributeFourth)
                    values_ids = []
                    values = variantFourth.split(',')
                    for val in values:
                        val = val.strip()
                        variante_id = self.get_variante(attributo, val)
                        values_ids.append(variante_id.id)
                    if product_id.attribute_line_ids:
                        attribute = product_id.attribute_line_ids.filtered(lambda x: x.attribute_id.id == attributo)
                        if attribute:
                            attribute.update({'value_ids': [(6, 0, values_ids)]})
                        else:
                            product_id.sudo().write({'attribute_line_ids': [
                                (0, 0, {'attribute_id': attributo, 'value_ids': [(6, 0, values_ids)]})]})
                    else:
                        product_id.sudo().write({'attribute_line_ids': [
                            (0, 0, {'attribute_id': attributo, 'value_ids': [(6, 0, values_ids)]})]})

                if attributeFifth and variantFifth:
                    attributo = self.get_attribute(attributeFifth)
                    values_ids = []
                    values = variantFifth.split(',')
                    for val in values:
                        val = val.strip()
                        variante_id = self.get_variante(attributo, val)
                        values_ids.append(variante_id.id)
                    if product_id.attribute_line_ids:
                        attribute = product_id.attribute_line_ids.filtered(lambda x: x.attribute_id.id == attributo)
                        if attribute:
                            attribute.update({'value_ids': [(6, 0, values_ids)]})
                        else:
                            product_id.sudo().write({'attribute_line_ids': [
                                (0, 0, {'attribute_id': attributo, 'value_ids': [(6, 0, values_ids)]})]})
                    else:
                        product_id.sudo().write({'attribute_line_ids': [
                            (0, 0, {'attribute_id': attributo, 'value_ids': [(6, 0, values_ids)]})]})

                # Se specificato inserisco il fornitore
                if nomeFornitore:
                    self.GetOrCreateFornitoreProdotto(product_id, prezzoAcquisto, fornTempoconsegna, nomeFornitore, codiceFornitore)

                numElaborati += 1
                if numElaborati % 100 == 0:
                    lu.LogInfo(f'Num righe prodotto elaborate: {numElaborati}/{len(recordsPadre.values)} --> {codice}')
                    self.log(level=logging.INFO,
                             message=f'Num righe prodotto elaborate: {numElaborati}/{len(recordsPadre.values)} --> {codice}',
                             action_name='ImportExcelProdottiRettificata')

            except Exception as e:
                lu.LogError(f'Riga:{numElaborati} Nome: {productName} Sku:{codice} {_(e)}')
                info = f'-Riga:{numElaborati} Nome: {productName} Sku:{codice} {_(e)}'
                if info:
                    error.append(info)

        # * =======================================================
        # * ================ RIGHE PRODOTTI FIGLI =================
        # * =======================================================
        lu.LogInfo(f'Elaboro i prodotti figli')
        numElaborati = 0
        for record in recordsFiglio.values:
            try:
                codicePadre = str(record[lista_campi['Sku_Padre']]).strip()
                riga_padre = data.query(f"Sku_Prodotto == '{codicePadre}' ")
                nomePadre = riga_padre.values[0][lista_campi['Nome']]
                productName = str(record[lista_campi['Nome']]).strip()
                codice = str(record[lista_campi['Sku_Prodotto']]).strip()

                # Cerco il prodotto padre per codce padre o per nome
                product_padre = m_product_template.search([('default_code_import', '=', codicePadre)], limit=1)
                if not product_padre:
                    product_padre = m_product_template.search([('default_code', '=', codicePadre)], limit=1)
                if not product_padre:
                    product_padre = m_product_template.search([('name', '=', nomePadre)], limit=1)
                if not product_padre:
                    info = f'-Non è stato trovato il prodotto padre per il prodotto con nome: {productName} e sku:{codice}'
                    lu.LogInfo(info)
                    if info:
                        error.append(info)
                    continue

                listPrice = self.get_decimal_from_string(record[lista_campi['Prezzo_vendita']]) if record[lista_campi['Prezzo_vendita']] else 0
                qtyDisponibile = self.get_decimal_from_string(record[lista_campi['Qtà_in_magazzino']]) if record[lista_campi['Qtà_in_magazzino']] else 0

                barcode = record[lista_campi['Barcode']]

                fornTempoconsegna = int(record[lista_campi['Forn._Tempo_cons._(gg)']]) if record[lista_campi['Forn._Tempo_cons._(gg)']] else 0
                attributeOne = str(record[lista_campi['Attributo_1']]).strip()
                variantOne = str(record[lista_campi['Varianti_attr._1']]).strip()
                attributeTwo = str(record[lista_campi['Attributo_2']]).strip()
                variantTwo = str(record[lista_campi['Varianti_attr._2']]).strip()
                attributeThree = str(record[lista_campi['Attributo_3']]).strip()
                variantThree = str(record[lista_campi['Varianti_attr._3']]).strip()

                m_product_product = self.env['product.product']

                variant_list = []

                product = {'default_code': codice}
                # if lista_extra:
                #     for item, values in lista_extra.items():
                #         field_type, relation = self.GetFieldType("product.product", item)
                #         lu.LogInfo(f'field_type: {str(field_type)} relation: {str(relation)}')
                #
                #         if field_type == 'many2one':
                #             product[item] = self.GetOrCreateMany2one("product.product", str(record[values]).strip(), relation)
                #         else:
                #             product[item] = str(record[values]).strip()

                # CONTROLLO BARCODE
                if barcode:
                    existing_bc = m_product_product.search([('barcode', '=', barcode), ('default_code', '!=', codice)], limit=1)
                    if existing_bc:
                        lu.LogWarn(f'Esiste già un prodotto con questo barcode {barcode}: {existing_bc.id} - {existing_bc.name}')
                        sike = f'Esiste già un prodotto con questo barcode {barcode}: {existing_bc.id} - {existing_bc.name}'
                        error.append(sike)
                    else:
                        product['barcode'] = barcode

                if attributeOne and variantOne:
                    attributo = self.get_attribute(attributeOne)
                    values = variantOne.split(',')
                    for val in values:
                        val = val.strip()
                        variante_id = self.get_variante(attributo, val)
                        variant_list.append(variante_id.id)
                        if listPrice:
                            price_extra = listPrice - product_padre.list_price
                            if float(price_extra) > 0.0:
                                variante_tmpl_id = self.env['product.template.attribute.value'].search(
                                    [('product_attribute_value_id', '=', variante_id.id),
                                     ('product_tmpl_id', '=', product_padre.id)], limit=1)
                                if variante_tmpl_id:
                                    variante_tmpl_id.update({'price_extra': price_extra})
                                    listPrice = 0

                if attributeTwo and variantTwo:
                    attributo = self.get_attribute(attributeTwo)
                    values = variantTwo.split(',')
                    for val in values:
                        val = val.strip()
                        variante_id = self.get_variante(attributo, val)
                        variant_list.append(variante_id.id)

                if attributeThree and variantThree:
                    attributo = self.get_attribute(attributeThree)
                    values = variantThree.split(',')
                    for val in values:
                        val = val.strip()
                        variante_id = self.get_variante(attributo, val)
                        variant_list.append(variante_id.id)

                # Cerco il product.product
                prd_prd_ids = product_padre.product_variant_ids
                for prd_prd in prd_prd_ids:
                    var_ids_t = variant_list.copy()
                    if len(variant_list) != len(prd_prd.product_template_attribute_value_ids):
                        continue
                    for ptav_id in prd_prd.product_template_attribute_value_ids:
                        if ptav_id.product_attribute_value_id.id in var_ids_t:
                            var_ids_t.remove(ptav_id.product_attribute_value_id.id)
                    if len(var_ids_t) == 0:
                        prd_prd.update(product)
                        lu.LogInfo(f'write {product["default_code"]}: {prd_prd.id}')

                        if float(qtyDisponibile) > 0.0:
                            wiz_qty = self.env['stock.change.product.qty'].sudo().create(
                                {'product_id': prd_prd.id,
                                 'new_quantity': qtyDisponibile,
                                 'product_tmpl_id': prd_prd.product_tmpl_id.id})
                            wiz_qty.change_product_qty()
                        continue

                numElaborati += 1
                if numElaborati % 100 == 0:
                    lu.LogInfo(f'Num righe varianti elaborate: {numElaborati}/{len(recordsFiglio.values)} --> {codice}')
                    self.log(level=logging.INFO,
                             message=f'Num righe prodotto elaborate: {numElaborati}/{len(recordsFiglio.values)} --> {codice}',
                             action_name='ImportExcelProdottiRettificata')

            except Exception as e:
                lu.LogError(f'Riga:{numElaborati} Nome: {productName} Sku:{codice} {e}')
                info = f'-Riga:{numElaborati} Nome: {productName} Sku:{codice} {_(e)}'
                if info:
                    error.append(info)

        if error:
            try:
                error = '\n'.join([str(elem) for elem in error])
            except:
                error = 'indefinito'

        if error:
                self.error = error
                self.log(level=logging.INFO,
                         message=error,
                         action_name='ImportExcelProdottiRettificata')
                wiz_id = self.env.ref('import_products_excel.wiz_errore').id

                return {
                    'name': _('Log Error'),
                    'res_model': 'product.import.wizard',
                    'res_id': self.id,
                    'views': [(wiz_id, 'form')],
                    'type': 'ir.actions.act_window',
                    'target': 'new'
                }

        else:
            successo = f'Sono state importate {len(data.values)} righe con successo!\n' \
                       f'Num prodotti: {len(recordsPadre.values)}\nNum varianti: {len(recordsFiglio.values)}'
            self.error = successo
            self.log(level=logging.INFO,
                     message=successo,
                     action_name='ImportExcelProdottiRettificata')
            wiz_id = self.env.ref('import_products_excel.wiz_successo').id

            return {
                'name': _('Successo'),
                # 'view_type': 'form',
                'view_mode': 'form',
                'res_model': 'product.import.wizard',
                'res_id': self.id,
                'views': [(wiz_id, 'form')],
                'type': 'ir.actions.act_window',
                'target': 'new'
            }

    def GetOrCreateMany2one(self, model, value, fieldname='name'):

        lu.LogInfo(f'GetOrCreateMany2one: {model} {value} {fieldname}')
        model_env = self.sudo().env[model]
        record_id = model_env.sudo().search([(fieldname, '=', value)], limit=1)
        if record_id:
            return record_id.id

        data = {fieldname: value}
        record_id = model_env.create(data)

        lu.LogInfo(f'record_id: {record_id}')
        return record_id.id
    def GetOrCreateMany2many(self, model, value, fieldname='name'):

        lu.LogInfo(f'GetOrCreateMany2many: {model} {value} {fieldname}')
        model_env = self.sudo().env[model]
        values= list(value.split(','))
        record_ids=[]
        for val in values:
            record_id = model_env.sudo().search([(fieldname, '=', val)], limit=1)
            if not record_id:
                try:
                 record_id = model_env.create({'name':val})
                except Exception as e:
                    lu.LogInfo(f'Impossibile creare il record: {val} del modello {len(model_env)},errore:{e}')
                    self.log(level=logging.INFO,
                             message=f'Impossibile creare il record: {val} del modello {len(model_env)},errore:{e}',
                             action_name='ImportExcelProdottiRettificata')
            record_ids.append(record_id.id)
        data = {fieldname: value}


        lu.LogInfo(f'record_ids: {record_ids}')
        return [(6,0,record_ids)]

    def GetFieldType(self, model, fieldname):
        """
        binary	binario
        boolean	booleano
        char	carattere
        date	data
        datetime	data e ora
        float	virgola mobile
        html	HTML
        integer	intero
        many2many	molti a molti
        many2one	molti a uno
        many2one_reference	many2one_reference
        monetary	monetario
        one2many	uno a molti
        reference	riferimento
        selection	selezione
        text	testo
        """
        ir_model_obj = self.env['ir.model.fields'].sudo()
        ir_model_field = ir_model_obj.search([('model', '=', model), ('name', '=', fieldname)])
        field_type = ir_model_field.ttype
        relation = ir_model_field.relation

        return field_type, relation


    def GetOrCreateCategory(self, odooCategoryName):

        m_product_category = self.sudo().env["product.category"]

        # Splitto la categoria per trovare eventuali categorie/sottocategorie
        categorie = odooCategoryName.split('/')

        idCategory = None
        parent_id = None
        for x in range(len(categorie)):
            categoria = categorie[x].capitalize()
            data = {"name": categoria}

            if x == 0:
                categ_id = m_product_category.sudo().search([('name', '=', categoria)], limit=1)
            else:
                categ_id = m_product_category.search([('name', '=', categoria), ('parent_id', '=', parent_id.id)],
                                                     limit=1)

            # Se non esiste lo creo
            if categ_id:
                parent_id = idCategory = categ_id

            else:
                if parent_id:
                    data['parent_id'] = parent_id.id
                parent_id = idCategory = m_product_category.sudo().create(data)

        return idCategory
        #todo codice nosense, commento il tutto
        # categoria = odooCategoryName
        #
        # categ_id = m_product_public_category.search([('name', '=', categoria)], limit=1)
        #
        # if categ_id:
        #     idCategory = categ_id
        # else:
        #     idCategory = m_product_public_category.sudo().create([{"name": categoria}])
        #
        # return idCategory

    def GetOrCreateFornitoreProdotto(self, idProdotto, prezzo, delay, nomeFornitore, productCodeForn, product_id=False):

        # Ricerca id fornitore in base a nome
        m_res_partner = self.env["res.partner"]
        m_product_supplierinfo = self.env["product.supplierinfo"]
        try:
            idFornitore = None
            if nomeFornitore or productCodeForn:
                idFornitore = m_res_partner.search([('name', '=', nomeFornitore)], limit=1)

            if not idFornitore:
                idFornitore = m_res_partner.sudo().create({'name': nomeFornitore, 'company_type': 'company'})

            # Ricerca il fornitore di un prodotto, partendo dall'id del prodotto
            search_domain = [('product_tmpl_id', '=', idProdotto.id), ('name', '=', idFornitore.id)]
            if product_id:
                if product_id.product_tmpl_id == idProdotto:
                    search_domain.append(('product_id', '=', product_id.id))
            datiFornitore = m_product_supplierinfo.search(search_domain, limit=1)

            # Dati riga prodotto-fornitore
            data = {'product_tmpl_id': idProdotto.id, 'price': prezzo}
            if productCodeForn:
                data['product_code'] = productCodeForn
            if delay:
                data['delay'] = delay

            # se esiste, aggiorna altrimenti inserisce
            if product_id:
                if product_id.product_tmpl_id == idProdotto:
                    data['product_id'] = product_id.id
            if datiFornitore:
                datiFornitore.sudo().sudo().write(data)

            # altrimenti, inserisci nome fornitore e prezzo
            else:
                data['name'] = idFornitore.id
                idNewSupplier = m_product_supplierinfo.sudo().create(data)

        except Exception as e:
            lu.LogError(f'Errore nella creazione del fornitore {nomeFornitore} prodotto con id {idProdotto} - {e}')

    def get_attribute(self, attributo):
        attribute_env = self.env['product.attribute']
        attribute = attribute_env.search([('name', '=', attributo)])
        if not attribute:
            attribute = attribute_env.sudo().create({'name': attributo})
        return attribute.id

    def get_variante(self, attributo, val):
        values_env = self.env['product.attribute.value']
        valore = values_env.search([('name', '=', val), ('attribute_id', '=', attributo)])
        if not valore:
            valore = values_env.sudo().create({'name': val, 'attribute_id': attributo})
        return valore

    def GetIva(self, importo,type_tax_use='sale'):
        account_tax = self.env["account.tax"]
        tax_id = account_tax.search([('amount', '=', importo),('type_tax_use','=',type_tax_use)], limit=1)
        if tax_id:
            return tax_id
        else:
            return False

    def GetUom(self, name):

        name = str(name).strip()
        if not name:
            return False

        # Sostituisco PZ con Untia e MT con m
        name = name.replace('PZ', 'Unita').replace('MT', 'm')

        m_udm = self.env["uom.uom"]

        uom_id = m_udm.search([('name', '=', name)], limit=1)
        if uom_id:

            return uom_id.id

        else:
            uom_id = m_udm.search([('name', '=', name.lower())], limit=1)
            if uom_id:
                return uom_id.id
            else:
                # La cerco tutto maiuscolo
                uom_id = m_udm.search([('name', '=', name.upper())], limit=1)
                if uom_id:
                    return uom_id.id

        # Non esiste proprio, lo creo
        idNewUdm = m_udm.sudo().create({'name': name, 'category_id': 1, 'uom_type': 'bigger'})

        return idNewUdm.id

    def upload_product_image(self):
        lu.LogInfo(f'Caricamento immagini dei prodotti ...')
        m_product_product = self.env['product.product']
        zip_file = base64.decodestring(self.import_file)
        error = []

        endswith = ".jpg"
        unzip = zipfile.ZipFile(io.BytesIO(zip_file), "r")
        num = 0
        for file in unzip.infolist():
            try:
                image_name = ''
                if file.filename.endswith(endswith):
                    num += 1
                    try:
                        image_name = file.filename.split('/')[1]
                    except:
                        image_name = file.filename

                    f = unzip.open(file.filename)
                    picture = f.read(1024 * 1024)
                    # recupera il nome del file (senza estensione)
                    nomeFile = image_name.replace('.jpg', '')
                    # ricerca del prodotto con il default_code = nome file
                    product_id = m_product_product.search(
                        [('default_code', '=', nomeFile)], limit=1)
                    if not product_id:
                        product_id = m_product_product.search(
                            [('default_code_import', '=', nomeFile)], limit=1)
                    if product_id:
                        try:

                            byte_array = bytearray(picture)
                            base64_bytes = base64.b64encode(byte_array)  # base64.encodebytes(byte_data)

                            ImageSend = base64_bytes.decode('ascii')
                            product_id.update({'image_1920': ImageSend})

                            lu.LogInfo(f'Inserita immagine del prodotto {product_id.name}')

                        except Exception as e:
                            lu.LogError(f"Impossibile caricare l'immagine {file.filename}. Errore %s " % (str(e)))
                            info = f"Impossibile caricare l'immagine {file.filename}. Errore %s " % (str(e))
                            if info:
                                error.append(info)
                    else:
                        info = f"Impossibile caricare l'immagine {image_name}. Il prodotto non è stato trovato"
                        if info:
                            error.append(info)
                        pass
                else:
                    if image_name:
                        info = f"Impossibile caricare l'immagine {image_name}. Il formato non è corretto"
                        if info:
                            error.append(info)
                    pass
            except Exception as e:
                lu.LogError(f"Impossibile caricare l'immagine {file.filename}. Errore %s " % (str(e)))
                info = f"Impossibile caricare l'immagine {file.filename}. Errore %s " % (str(e))
                if info:
                    error.append(info)
        if error:
            error = '\n'.join([str(elem) for elem in error])
            self.error = error
        if self.error:
            wiz_id = self.env.ref('import_products_excel.wiz_errore').id

            return {
                'name': _('Log Error'),
                'res_model': 'product.import.wizard',
                'res_id': self.id,
                'views': [(wiz_id, 'form')],
                'type': 'ir.actions.act_window',
                'target': 'new'
            }
        else:

            self.error = "Tutte le %s immagini sono state caricate correttamente" % num
            wiz_id = self.env.ref('import_products_excel.wiz_successo').id

            return {
                'name': _('Successo'),
                'res_model': 'product.import.wizard',
                'res_id': self.id,
                'views': [(wiz_id, 'form')],
                'type': 'ir.actions.act_window',
                'target': 'new'
            }
