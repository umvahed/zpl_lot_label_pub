# -*- coding: utf-8 -*-
{
    'name': 'ZPL Lot Label',
    'version': '18.0.1.0.0',
    'summary': 'Print ZPL barcode labels for stock lots directly from Odoo',
    'description': """
Adds a **Print → ZPL Lot Label** action to stock lot records.
Outputs raw **ZPL (Zebra Printer Language)** commands for direct printing on
any Zebra-compatible label printer.

**Label layout:**

- Barcode 1 (top, Code 128): lot number
- Human-readable text: lot display name
- Barcode 2 (bottom, Code 128): lot internal reference (falls back to lot number)

**Report type:** qweb-text — plain text output sent directly to the printer.
No PDF conversion. Works with browser-based ZPL print utilities and
direct IP printing to Zebra printers.

**Test without a printer:**
Paste the ZPL output into https://labelary.com/viewer.html for a live preview.

**Customisation:**
The label template (`reports/label_template.xml`) uses standard ZPL commands.
Adjust `^FO` coordinates for your label size and printer DPI.
If you use a custom barcode field on `stock.lot`, edit the `barcode_value`
line in the template to reference your field.
    """,
    'author': 'Bitquanta',
    'website': 'https://sebenz.co.za',
    'support': 'support@sebenz.co.za',
    'category': 'Inventory',
    'license': 'LGPL-3',
    'depends': ['stock'],
    'data': [
        'reports/label_template.xml',
        'reports/action_report.xml',
    ],
    'images': ['static/description/banner.png'],
    'price': 10.00,
    'currency': 'EUR',
    'installable': True,
    'auto_install': False,
    'application': False,
}
