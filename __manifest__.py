# -*- coding: utf-8 -*-
{
    'name': "Pago a Proveedores",

    'summary': "Liquidacion de facturas de proveedores",

    'description': """
        Supercalifragilistico long description
    """,
    'sequence': -100,
    'author': "DanielBogado",
    'website': "http://www.verbosoft.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Extra tools',
    'version': '1.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail','towing_service'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/liquidacion.xml',
        'views/purchase_move.xml',
        'wizard/purchase_move_wizard.xml',
        
    ],
    "license": "AGPL-3",
    'installable': True,
    'application': True,
    # only loaded in demonstration mode
    'demo': [
    ],        
    
}
