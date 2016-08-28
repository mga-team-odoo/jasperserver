# -*- coding: utf-8 -*-
##############################################################################
#
#   jasper_connector module for OpenERP, Management module for Jasper Server
#   Copyright (C) 2015 MIROUNGA (<http://www.mirounga.fr/>)
#             Christophe CHAUVET <christophe.chauvet@gmail.com>
#
#   This file is a part of jasper_connector
#
#   jasper_connector is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Affero General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   jasper_connector is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU Affero General Public License for more details.
#
#   You should have received a copy of the GNU Affero General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp import models, fields
import openerp

from openerp.addons.jasper_connector.report.jasper import report_jasper
from openerp.addons.jasper_connector.common import registered_report
import logging

_logger = logging.getLogger(__name__)


class ResLang(models.Model):
    _inherit = 'res.lang'

    js_pattern_date = fields.Char(string='Pattern Date', size=32,
                                  help='Jasper pattern date')
    js_pattern_time = fields.Char(string='Pattern Time', size=32,
                                  help='Jasper pattern time')
    js_pattern_datetime = fields.Char(string='Pattern Date Time', size=64,
                                      help='Jasper pattern datetime')
    js_pattern_currency = fields.Char(string='Pattern Currency', size=32,
                                      help='Jasper pattern currency')
    js_pattern_number = fields.Char(string='Pattern Number', size=32,
                                    help='Jasper pattern number')


class ResGroups(models.Model):
    _inherit = 'res.groups'

    is_jasper = fields.Boolean(string='JasperServer',
                               help='Dedicate groups for JasperServer',
                               default=False)


class IrActionReport(models.Model):
    _inherit = 'ir.actions.report.xml'

    report_type = fields.Selection(selection_add=[('jasper', 'Jasper')])

    def register_all(self, cursor):
        """
        Register all jasper report
        """
        _logger.info('====[REGISTER JASPER REPORT]========================')
        cursor.execute("""SELECT id, report_name
                            FROM ir_act_report_xml
                           WHERE report_type = 'jasper'""")
        records = cursor.dictfetchall()
        for record in records:
            registered_report(record['report_name'])
        _logger.info('====[END REGISTER JASPER REPORT]====================')
        return True

    def _lookup_report(self, cr, name):
        """
        Use new report function to detect old report and
        use custom python parser
        """
        if 'report.' + name in openerp.report.interface.report_int._reports:
            rp = openerp.report.interface.report_int._reports['report.' + name]  # noqa
            if not isinstance(rp, report_jasper):
                rp = None
        else:
            cr.execute("""SELECT * FROM ir_act_report_xml
                           WHERE report_name=%s AND report_type=%s""",
                       (name, 'jasper'))
            r = cr.dictfetchone()
            rp = r and report_jasper('report.'+r['report_name']) or None

        if rp:
            return rp

        return super(IrActionReport, self)._lookup_report(cr, name)

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
