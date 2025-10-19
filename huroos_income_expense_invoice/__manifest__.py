# -*- coding: utf-8 -*-
# Powered by Marco Frascerra.
# Part of Huroos. See LICENSE file for full copyright and licensing details.
# © 2023 Huroos Srl. (<https://www.huroos.com>).

{
    'name': 'Conti di costo / ricavo',
    'version': '14.0.0.0',
    'summary': "Modulo che aggiunge due campi nei contatti, uno sper il conto "
               "di costo e l'altro per il conto di ricavo. Alla creazione della fattura al contatto, "
               "verranno assegnati in automatico i conti in ogni riga della fattura, se popolati nell'anagrafica.",
    'description': "Conti di costo / ricavo",
    'author': 'Huroos Srl',
    'website': 'https://www.huroos.com',
    'category': 'accounting',
    'depends': ['account','l10n_it_fatturapa_in','l10n_it_fatturapa_import_zip'],
    'data': [
        'views/res_partner.xml'
    ],
}