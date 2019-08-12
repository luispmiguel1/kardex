# -*- encoding: utf-8 -*-

{
    'name' : 'Kardex',
    'version' : '1.0',
    'category': 'Custom',
    'description': """Modulo para reporte de kardex""",
    'author': 'Rodrigo Fernandez',
    'website': 'http://aquih.com/',
    'depends' : [ 'stock' ],
    'data' : [
        'views/report.xml',
        'views/reporte_kardex.xml',
        'views/report_stockinventory.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'certificate': '',
}