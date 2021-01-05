# -*- coding: utf-8 -*-
{
    'name': "Honestus Task",

    'summary': """ Module for honestus task """,

    'description': """
        Module for honestus task
    """,

    'author': "Benas R.",
    'website': "http://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '12.0.1.0',

    # any module necessary for this one to work correctly
    'depends': ['base_setup', 'sale_management', 'product'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/product_views.xml',
        'views/sale_views.xml',
        'report/sale_report_templates.xml',
    ],
    'installable': True,
    'application': True,
}
