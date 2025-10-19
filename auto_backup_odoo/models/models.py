# -*- coding: utf-8 -*-
import logging
import os
import time
import re

from odoo import models, fields, api, tools, _

_logger = logging.getLogger("############### Backup ODOO DB Logs #################")


class OdooBackupConfig(models.Model):
    """
    Base CLass for Backup Configuration
    """
    _name = 'auto.backup'
    _description = "Model For Auto Backup Filestore And Database"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    def log(self, string, type='info'):
        """
        Write logs in Terminal
        :param string: Message
        :param type: Info/Exception
        :return:
        """
        if type == 'info':
            _logger.info(str(string))
        elif type == 'exception':
            _logger.exception(str(string))

    def calc_x_days(self, x_days):
        """
        Convert x days -> time() to delete old backup files
        :return x days
        :param x_days:
        :return:
        """
        return time.time() - (60 * 60 * 24 * x_days or 1)

    def _get_key_from_url(self, url):
        """
        Extract unique key from the drive folder/file url
        https://drive.google.com/drive/u/0/folders/1vzEwZyIBBthjvgKK97OYiByWAI1u6k4 -> 1vzEwZyIBBthjvgKK97OYiByWAI1u6k4
        :param url:
        :return:
        """
        word = re.search("(key=|/folders/)([A-Za-z0-9-_]+)", url)
        if word:
            return word.group(2)
        return None

    name = fields.Char(required=True, )
    host = fields.Char(string='Host',
                       required=True,
                       size=100,
                       copy=False,
                       default='localhost',
                       track_visibility='onchange', )
    user = fields.Char(string='Database Role',
                       required=True,
                       size=100,
                       copy=False,
                       default=tools.config['db_user'])
    db_password = fields.Char(string="Password",
                              required=True,
                              copy=False,
                              default=tools.config['db_password'])
    backup_dir = fields.Char(string='Backup Directory',
                             required=True,
                             size=200,
                             copy=False,
                             default='/opt/odoo/',
                             track_visibility='onchange', help="""
Local: Local Backup Path. Eg: /opt/odoo/backups
Remote: Remote Backup Path Eg: /opt/odoo/backups
Google Drive: The IDs of the parent folders which contain the file.
If not specified as part of a create request, the file will be placed directly in the user's My Drive folder.
If not specified as part of a copy request, the file will inherit any discoverable parents of the source file.
Update requests must use the addParents and removeParents parameters to modify the parents list.
Eg: https://drive.google.com/drive/u/0/folders/1vzEwZyIBBthjvgKK97OYiByWAI1u6k4
    """)
    db = fields.Char(string='Database',
                     required=True,
                     copy=False,
                     default=lambda self: self._cr.dbname,
                     track_visibility='onchange', )
    active = fields.Boolean(string='Active',
                            default=True)
    backup_mode = fields.Selection(
        selection=[('local', 'Local'),
                   ('remote', 'Remote Server'),
                   ('drive', 'Google Drive'),
                   ('dropbox', 'Dropbox'),
                   ('s3', 'Amazon S3')],
        string='Backup Mode', copy=False, required=True, default='local', tracking=True, help="""""")
    format = fields.Selection(selection=[('c', 'Custom Archive'),
                                         ('p', 'Plain Text SQL'),
                                         ('t', 'tar archive')],
                              string='Format',
                              copy=False,
                              required=True,
                              default='c',
                              track_visibility='onchange',
                              help="""
                            Selects the format of the output. the format can be one of the following:
plain
    Output a plain-text SQL script file (the default).
    The plain text format is useful for very small databases with a minimal number of objects but other than that,
    it should be avoided.
custom
    Output a custom archive suitable for input into pg_restore.
    This is the most flexible format in that it allows the reordering of loading data as well as to object definitions.
    This format is also compressed by default.
    Here we user gzip ie, test.gz, We also recommend you to select Custom, 
    because Using the custom format you can restore single objects from a backup.
tar
    Output a tar archive suitable for input into pg_restore.
    Using this archive format allows reordering and/or exclusion of database objects at the time the
    database is restored. It is also possible to limit which data is reloaded at restore time.
    we use tar with gzip

                              """)
    x_days = fields.Float(string='Days',
                          copy=False,
                          track_visibility='onchange',
                          default=1,
                          help="""
                            Remove old backups automatically from the input days ago. Input should be the number of days.
                          """
                          )
    state = fields.Selection(selection=[('active', 'Active'),
                                        ('inactive', 'Inactive')],
                             string="Status",
                             track_visibility='onchange',
                             default='active',
                             copy=False)
    # Google Drive Fields
    # We Need URI To Know The Drive Destination Folder
    # Eg: https://drive.google.com/drive/u/0/folders/1vzEwZyIBBthjvgKK97OYiByWAI1u6k4
    # Filestore Fields
    backup_dir_filestore = fields.Char(string='Filestore Backup Directory',
                                       required=True,
                                       size=200,
                                       copy=False,
                                       default='/opt/odoo/',
                                       track_visibility='onchange', help="""
Local: Local Filestore Backup Path. Eg: /opt/odoo/filestoreBackups
Remote: Remote Filestore  Backup Path Eg: /opt/odoo/filestoreBackups
Google Drive: The IDs of the parent folders which contain the file.
If not specified as part of a create request, the file will be placed directly in the user's My Drive folder.
If not specified as part of a copy request, the file will inherit any discoverable parents of the source file.
Update requests must use the addParents and removeParents parameters to modify the parents list.
Eg: https://drive.google.com/drive/u/0/folders/1vzEwZyIBBthjvgKK97OYiByWAI1u6k4
    """)
    filestore_path = fields.Char(string='FileStore Path',
                                 required=True,
                                 size=200,
                                 copy=False,
                                 default=tools.config['data_dir'],
                                 track_visibility='onchange', )

    def toggle_active(self):
        """
        Function changes the record status active or inactive
        :return:
        """
        for record in self:
            record.active = not record.active
            record.state = 'active' if record.state == 'inactive' else 'inactive'

    def _check_path_access(self, path):
        """
        Make sure the defined locations are accessible to read and write.
        :param path:
        :return:
        """
        if not os.access(path, os.F_OK):
            self.message_post(
                body="Backup Error.\n Info: %s" % "Path" + path + "Not Exist",
                subtype_xmlid="mail.mt_comment",
                message_type="comment")
            return False
        if not os.access(path, os.R_OK):
            self.message_post(
                body="Backup Error.\n Info: %s" % "No Permission to Read file in " + path,
                subtype_xmlid="mail.mt_comment",
                message_type="comment")
            return False
        if not os.access(path, os.W_OK):
            self.message_post(
                body="Backup Error.\n Info: %s" % "No Permission to write file in " + path,
                subtype_xmlid="mail.mt_comment",
                message_type="comment")
            return False
        _logger.info("Path Write, Read Access OK")

    @api.model
    def dump(self):
        """
        Dump the current DB To a specified format. In default, it is compressed to save space and handle the data.
        You can only restore the compressed dump file using the command: pg_restore source destination
        :return:
        """
        # pass
        BackupPool = self.env['auto.backup']
        backup_records = BackupPool.search([])
        #
        for record in backup_records:
            # Backup Formats
            if record.format == 'c':
                dumper = """pg_dump -h {host} -U {user} -F c {db_name} > {b_db_name}.sql.gz"""
            elif record.format == 'p':
                dumper = """pg_dump -h {host} -U {user} -F p {db_name} > {b_db_name}.sql"""  # Not recommended
            elif record.format == 't':
                dumper = """pg_dump -h {host} -U {user} -F t {db_name} > {b_db_name}.tar"""
            else:
                continue
            if record.backup_mode == 'local':
                try:
                    # Backup DB
                    record.dump_start(
                        db=record.db,
                        user=record.user,
                        password=record.db_password,
                        host=record.host,
                        dirr=record.backup_dir,
                        dumper=dumper,
                        x_days=record.x_days,
                    )
                except Exception as e:
                    record.message_post(
                        body="Backup Error.\n Info: %s" % (str(e) or repr(e)),
                        subtype_xmlid="mail.mt_comment",
                        message_type="comment")
                # Copying FileStore
                record.copy_filestore(
                    db=record.db,
                    filestore_path=record.filestore_path,
                    dirr=record.backup_dir_filestore,
                    x_days=record.x_days)

            elif record.backup_mode == 'remote':
                # Dump DB
                record.remote_dump_start(
                    db=record.db,
                    user=record.user,
                    password=record.db_password,
                    host=record.host,
                    remote_host=record.remote_host,
                    remote_user=record.remote_user,
                    remote_pswd=record.remote_password,
                    dumper=dumper,
                    dirr=record.backup_dir,
                    x_days=record.x_days,
                )
                # Dump Filestore
                record.remote_transfer_filestore(
                    db=record.db,
                    filestore_path=record.filestore_path,
                    remote_host=record.remote_host,
                    remote_user=record.remote_user,
                    remote_pswd=record.remote_password,
                    dirr=record.backup_dir_filestore,
                    x_days=record.x_days)
            elif record.backup_mode == 'drive':
                # Upload Backup To Drive
                record.drive_dump_start(
                    db=record.db,
                    user=record.user,
                    password=record.db_password,
                    host=record.host,
                    dirr=record.backup_dir,
                    dumper=dumper,
                    x_days=record.x_days,
                )
                # Upload FileStore To Drive
                record.drive_upload_filestore(
                    db=record.db,
                    filestore_path=record.filestore_path,
                    dirr=record.backup_dir_filestore,
                    x_days=record.x_days)
            elif record.backup_mode == 'dropbox':
                # Get Access Tocken
                if not record.dropbox_token:
                    token = record._get_dropbox_access_tocken(code=record.dropbox_secret)
                    if token:
                        record.dropbox_token = token
                        record.message_post(body="DropBox Access Token Updated.",
                                            subtype_xmlid="mail.mt_comment",
                                            message_type="comment")
                # Upload DB To DropBox
                record.dropbox_dump_start(
                    db=record.db,
                    user=record.user,
                    password=record.db_password,
                    host=record.host,
                    dirr=record.backup_dir,
                    dumper=dumper,
                    x_days=record.x_days,
                )
                # Upload FileStore To Drive
                record.dropbox_upload_filestore(
                    db=record.db,
                    filestore_path=record.filestore_path,
                    dirr=record.backup_dir_filestore,
                    x_days=record.x_days)
            elif record.backup_mode == 's3':
                # Upload DB To AWS S3
                record.aws_dump_start(
                    db=record.db,
                    user=record.user,
                    password=record.db_password,
                    host=record.host,
                    dirr=record.backup_dir,
                    dumper=dumper,
                    x_days=record.x_days,
                )
                # Upload FileStore To S3
                record.aws_upload_filestore(
                    db=record.db,
                    filestore_path=record.filestore_path,
                    dirr=record.backup_dir_filestore,
                    x_days=record.x_days)
            else:
                pass

# Reference: https://developers.google.com/drive/api/v3/reference
