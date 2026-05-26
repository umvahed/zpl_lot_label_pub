# ZPL Lot Label

Odoo 18 module — adds a **Print → ZPL Lot Label** action to stock lot records. Outputs raw ZPL (Zebra Printer Language) commands for direct printing on any Zebra-compatible label printer, with no PDF conversion and no driver required.

## Features

- One-click label printing from any `stock.lot` record
- Raw `qweb-text` report — plain ZPL sent directly to the printer
- Two Code 128 barcodes per label: lot number (top) and internal reference (bottom)
- Human-readable lot display name printed between the barcodes
- Works with browser-based ZPL utilities, direct IP printing (port 9100), and any ZPL-capable print service
- Test without a physical printer by pasting output into [labelary.com/viewer.html](https://labelary.com/viewer.html)

## Requirements

| Dependency | Notes |
|---|---|
| `stock` | Odoo Inventory module (standard) |
| Odoo version | 18.0 |
| Printer | Any Zebra-compatible label printer (203 dpi default) |

## Installation

1. Copy the `zpl_lot_label` folder into your Odoo addons path.
2. Restart the Odoo server.
3. Go to **Apps → Update Apps List**.
4. Search for **ZPL Lot Label** and click **Install**.

## Usage

1. Open **Inventory → Products → Lots/Serial Numbers**.
2. Select one or more lot records.
3. Click **Print → ZPL Lot Label**.
4. Send the plain-text output to your Zebra printer.

## Customisation

The label template is in `reports/label_template.xml` and uses standard ZPL commands. To adjust the layout:

- **Label size / DPI** — modify the `^FO` coordinate values. Coordinates are calculated at 203 dpi (standard Zebra resolution). For 300 dpi printers, scale all values by `300/203 ≈ 1.48`.
- **Custom barcode field** — if you store barcodes in a custom field on `stock.lot` (e.g. added via Odoo Studio), change the `barcode_value` line in the template to reference your field.

## License

LGPL-3 — see [zpl_lot_label/LICENSE](zpl_lot_label/LICENSE).

## Support

support@sebenz.co.za
