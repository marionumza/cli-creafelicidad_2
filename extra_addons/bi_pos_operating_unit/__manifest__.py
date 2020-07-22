# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

{
    "name" : "POS Operating Unit",
    "version" : "11.0.0.6",
    "category" : "Point of Sale",
    "depends" : ['base','sale','point_of_sale','operating_unit'], #,'account_operating_unit'
    "author": "BrowseInfo",
    'summary': 'This apps helps to handel Multiple Operating Unit on Point of Sale for single company',
    "description": """
       POS Multiple operating unit management for single company, Multiple pos operation management for single company, POS multiple operation for single company.
     multiple Branch for POS
     multiple operating unit for POS,
    multiple unit on POS
    multiple unit operation for POS
    branch on POS session
    Branch on POS receipt
    different unit on POS
    POS Unit Operation For single company
    operating unit on POS session
    operating unit on POS receipt
    different unit operation on POS
    POS multiple Unit Operation For single company
    
    """,
    "website" : "www.browseinfo.in",
    "price": 39,
    "currency": "EUR",
    "data": [
        'views/custom_pos_view.xml',
        'security/point_of_sale_security.xml',
    ],
    'qweb': [
    ],
    "auto_install": False,
    "installable": True,
    'live_test_url': "https://youtu.be/aoQnN3d52xc",
    "images":['static/description/Banner.png'],
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
