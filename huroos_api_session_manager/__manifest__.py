# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.
{
    'name': "Huroos - Api session manager",
    'version': "14.0.0.0",
    'author': "AIR-sc",
    'summary': 'Huroos - Api session manager. Consente di aggiungere un layer di sicurezza nelle API sviluppate nei propri moduli.',
    'description': """
\nPer avere un layer di sicurezza nelle API sviluppate nei propri moduli (es: RMA ticketing, Tag RFID), si richiede a chi chiama le nostre API
di fornire un token che scade ogni tot ore (di default è 12).
\nPer richiedere un nuovo token occorre utilizzare la funzione apposita possando come parametro la password fornita a chi chiama le API,
questa password viene generata automaticamente quando si crea in anagrafica il profilo di autorizzazioni (Settings-->Technical-->API auth).
\n\n
\n***UTILIZZO***\n
\n1 - Creare da interfaccia un API auth (Settings-->Technical-->API auth), viene generata una password automaticamente.
\n2 - Utilizzando la password precedentemente creata, richiedere via codice un token.
\nIl token ottenuto andrebbe poi passato come parametro nelle chiamate successive nelle API presenti nel proprio modulo.
\npsw = "API_4779556285"
\nenv["api_session.utils"].get_auth_token(psw)
\n3 - Verificare la validità del token prima di effettuare ulteriori operazioni nelle API sviluppate nel proprio modulo.
\ntoken = "1kfs9LOrQri5z6gW55G5lop0T"
\nis_valid = env["api_session.utils"].check_auth_token_is_valid(token) """,
    'license': 'LGPL-3',
    'category': "Extra Tools",
    'data': [
        'security/ir.model.access.csv',
        'views/api_auth.xml',
        'views/api_session.xml'
    ],
    'website': 'https://www.huroos.com',
    'depends': ['base', 'mail'],
    'installable': True,
    'auto_install': False,
    'images': ['static/description/icon.png'],

}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

