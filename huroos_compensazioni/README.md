# Huroos Compensazioni

## Description

Consente di registrare il pagamento di fatture attive e passive specificando come metodo di pagamento la compensazione con una o più fatture da/verso lo stesso cliente/fornitore.
## License

Copyright 2022 - Huroos srl - www.huroos.com
License LGPL-3.0 or later [GNU Lesser General Public License](https://www.gnu.org/licenses/lgpl-3.0.en.html)

## Installation

This module can be installed as a regular Odoo module. It depends on the 'base', 'contacts', 'hr', 'hr_skills', 'project', 'planning', 'project_forecast', 'documents', 'hr_recruitment', 'timesheet_grid', 'hr_contract' modules.

## Usage
Impostare nei settings il registro contabile per le compensazioni (eventualmente crearlo) e i conti debito/credito da utilizzare.

Nel wizard di registrazione di un pagamento di una fattura, spuntare la casella 'Compensazione', selezionare una o più fatture, selezionare il metodo di pagamento della differenza (cash/bank/...) e confermare.
L'app esegue le seguenti operazioni/scritture:
- crea una registrazione contabile di compensazione per registrare il debito verso il cliente
- se cash crea una registrazione nel Registratori di cassa con importo e partner specificato
- riconcilia tutte le fatture coinvolte con la registrazione contabile di compensazione ed eventualmente con la registrazione di cassa

## Support

For support, please visit the [Huroos website](https://www.huroos.com/)