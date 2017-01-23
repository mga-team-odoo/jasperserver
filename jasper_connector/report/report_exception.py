# -*- coding: utf-8 -*-
##############################################################################
#
#   jasper_connector module for OpenERP, Management module for Jasper Server
#   Copyright (C) 2011 SYLEAM (<http://www.syleam.fr/>)
#             Christophe CHAUVET <christophe.chauvet@gmail.com>
#    Copyright (C) 2013-2016 Mirounga ([http://mirounga.fr])
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


class JasperException(Exception):
    """
    Redefine correctly exception
    """
    def __init__(self, title='Error', message='Empty message'):
        self.title = title
        self.message = message

    def __str__(self):
        return '%s: %s' % (self.title, self.message)

    def __repr__(self):
        return self.__str__()


class AuthError(JasperException):
    pass


class EvalError(JasperException):
    pass


if __name__ == '__main__':
    import logging
    logging.basicConfig(level=logging.DEBUG)
    log = logging.getLogger('jasperlib')
    try:
        # test str method
        try:
            raise JasperException('Error', 'Test JasperException')
        except JasperException, e:
            assert str(e) == 'Error: Test JasperException', 'Incorrect str()'
        # test title attribute
        try:
            raise JasperException('Error', 'Test JasperException')
        except JasperException, e:
            assert e.title == 'Error', 'Title must return "Error"'
        # test message attribute
        try:
            raise JasperException('Error', 'Test JasperException')
        except JasperException, e:
            assert e.message == 'Test JasperException', \
                'Message must return "Test JasperException"'

    except AssertionError, a:
        log.debug('Test failed: %s' % a)
    finally:
        log.debug('Finished')

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
