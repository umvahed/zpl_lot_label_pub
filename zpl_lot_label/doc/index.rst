ZPL Lot Label
=============

Adds a **Print → ZPL Lot Label** action to stock lot records. Outputs raw ZPL
(Zebra Printer Language) commands for direct printing on any Zebra-compatible label
printer — no PDF conversion, no driver required.

Features
--------

* One-click label printing from any ``stock.lot`` record.
* ``qweb-text`` report type — plain ZPL sent directly to the printer.
* Two Code 128 barcodes per label: lot number (top) and internal reference (bottom).
* Human-readable lot display name printed between the barcodes.
* Works with browser-based ZPL utilities, direct IP printing (port 9100), and any
  ZPL-capable print service.
* Test without a printer: paste the output into https://labelary.com/viewer.html

Requirements
------------

* ``stock`` (standard Odoo Inventory module)
* Odoo 18.0
* Any Zebra-compatible label printer (template coordinates calculated at 203 dpi)

Installation
------------

1. Copy the ``zpl_lot_label`` folder into your Odoo addons path.
2. Restart the Odoo server.
3. Go to **Apps → Update Apps List**.
4. Search for **ZPL Lot Label** and click **Install**.

Usage
-----

1. Open **Inventory → Products → Lots/Serial Numbers**.
2. Select one or more lot records.
3. Click **Print → ZPL Lot Label**.
4. Send the plain-text output to your Zebra printer.

Label layout
------------

The default label contains:

* **Barcode 1** (top, Code 128) — the lot name (``stock.lot.name``).
* **Human-readable text** — the lot display name.
* **Barcode 2** (bottom, Code 128) — the internal reference (``stock.lot.ref``),
  falling back to the lot name if no reference is set.

Customisation
-------------

The label template is defined in ``reports/label_template.xml`` using standard ZPL
commands.

Adjusting for label size or printer DPI
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Modify the ``^FO`` coordinate values in the template. Default coordinates are
calculated at 203 dpi. For a 300 dpi printer, scale all ``^FO`` values by
approximately 1.48 (``300 / 203``).

Using a custom barcode field
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If your ``stock.lot`` records have a custom barcode field (e.g. added via Odoo Studio),
change the ``barcode_value`` line in ``reports/label_template.xml`` to reference your
field instead of the default ``lot.ref`` / ``lot.name`` fallback.

License
-------

LGPL-3
