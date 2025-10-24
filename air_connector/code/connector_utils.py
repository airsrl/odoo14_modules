from enum import Enum
from . import odoo_utils as ou
import datetime


class log_status(Enum):
    pending = 'pending'
    error = 'error'
    complete = 'complete'


def upd_log_entry(self, log_id, status, response, notes):
    log_env = self.env['connector.log']

    # Check whether a row with the same values already exists
    log_entry = log_env.search([('id', '=', log_id)], limit=1)
    if log_entry:
        res = log_entry.update(
            {
                'execution_date': datetime.datetime.now(),
                'status': status.value,
                'response': response,
                'notes': notes
            }
        )
        return res

    return False


def add_new_log_entry(self, model, record_id, operation, status: log_status, notes):
    log_env = self.env['connector.log']

    if record_id == 0:
        return

    #  SC 19/12/2023: La verifica non va fatta sullo status error ma sullo stato del record
    #  che si sta cercando di inserire.
    #  Altrimenti se esiste una riga di tipo error il prodotto non verrà mai più aggiornato su WP
    #  (a meno che non vengano elaborati/rimossi i record di tipo error)

    # Check whether a row with error status already exists
    # existing_log_entry = log_env.search(
    #     [
    #         ('model', '=', model),
    #         ('record_id', '=', record_id),
    #         ('operation', '=', operation),
    #         ('status', '=', log_status.error.value)
    #     ],
    #     limit=1
    # )
    #
    # if existing_log_entry and len(existing_log_entry) > 0:
    #     ou.log_info(f'existing_log_entry with error status: {existing_log_entry.id}')
    #     return

    # Check whether a row with the same values already exists
    existing_log_entry = log_env.search(
        [
            ('model', '=', model),
            ('record_id', '=', record_id),
            ('operation', '=', operation),
            ('status', '=', status.value)
        ],
        limit=1
    )

    if (not existing_log_entry) or len(existing_log_entry) == 0:
        new_log = {
            'creation_date': datetime.datetime.now(),
            'model': model,
            'record_id': record_id,
            'operation': operation,
            'status': status.value,
            'notes': notes
        }
        log_env.create(new_log)
    else:
        ou.log_info(f'existing_log_entry already: {existing_log_entry.id}')

    return True
