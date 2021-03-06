# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2015  ADHOC SA  (http://www.adhoc.com.ar)
#    All Rights Reserved.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Website Documentation',
    'category': 'Website',
    'summary': 'Website, Documentation',
    'version': '1.0',
    'description': """
Documentation Using Website, pages and google docs
To create a page you can type: http://localhost:9069/page/asda
        """,
    'author': 'ADHOC SA',
    'website': 'www.adhoc.com.ar',
    'depends': [
        'website',
    ],
    'data': [
        'data/doc_data.xml',
        'security/ir.model.access.csv',
        'security/security.xml',
        'views/doc.xml',
        'views/website_doc.xml',
    ],
    'demo': [
    ],
    'qweb': [
        'static/src/xml/website_doc.xml'
    ],
    'installable': True,
    'application': True,
}
