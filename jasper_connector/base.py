# -*- coding: utf-8 -*-
##############################################################################
#
#   jasper_server module for OpenERP, Management module for Jasper Server
#   Copyright (C) 2015 MIROUNGA (<http://www.mirounga.fr/>)
#             Christophe CHAUVET <christophe.chauvet@mirounga.fr>
#
#   This file is a part of jasper_server
#
#   jasper_server is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Affero General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   jasper_server is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU Affero General Public License for more details.
#
#   You should have received a copy of the GNU Affero General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp.osv import orm
from openerp.osv import fields


class res_lang(orm.Model):
    _inherit = 'res.lang'

    _columns = {
        'js_pattern_date': fields.char('Pattern Date', size=32, help='Jasper pattern date'),
        'js_pattern_time': fields.char('Pattern Time', size=32, help='Jasper pattern time'),
        'js_pattern_datetime': fields.char('Pattern Date Time', size=64, help='Jasper pattern datetime'),
        'js_pattern_currency': fields.char('Pattern Currency', size=32, help='Jasper pattern currency'),
        'js_pattern_number': fields.char('Pattern Number', size=32, help='Jasper pattern number'),
    }

class res_groups(orm.Model):
    _inherit = 'res.groups'

    _columns = {
        'is_jasper': fields.boolean(
            'JasperServer',
            help='Dedicate groups for JasperServer'),
    }

    _defaults = {
        'is_jasper': False,
    }


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
