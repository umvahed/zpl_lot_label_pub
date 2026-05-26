# zpl_lot_label

Odoo 18 module that adds a **Print → ZPL Lot Label** action to stock lot records. Outputs raw ZPL (Zebra Printer Language) commands for direct printing on Zebra-compatible printers — no PDF, no driver.

## Publisher
- Author: Bitquanta
- Website: https://sebenz.co.za
- Support: support@sebenz.co.za
- License: LGPL-3

## Structure

```
zpl_lot_label_pub/
├── README.md                          # Repo-level docs (GitHub)
└── zpl_lot_label/
    ├── __manifest__.py
    ├── __init__.py
    ├── LICENSE
    ├── reports/
    │   ├── label_template.xml         # QWeb text template (ZPL commands)
    │   └── action_report.xml          # ir.actions.report registration
    ├── doc/
    │   └── index.rst                  # Odoo store documentation
    └── static/description/
        ├── index.html                 # Store listing page
        ├── icon.png                   # MISSING — needs to be added (128×128 PNG)
        └── banner.png                 # MISSING — needs to be added
```

## Key Design Decisions

- Report type is `qweb-text` — renders plain text (ZPL), not PDF.
- `label_template.xml` must be loaded **before** `action_report.xml` in the manifest `data` list (template must exist before the action references it).
- Label coordinates calculated at 203 dpi. Scale `^FO` values by 1.48 for 300 dpi printers.
- The `barcode_value` in `label_template.xml` falls back from `lot.ref` to `lot.name` if no internal reference is set.

## Dependencies
- `stock`

## Status
- [x] Manifest placeholders filled in
- [x] `label_template.xml` added to manifest `data` (was missing — critical bug fixed)
- [x] Stray `reports/__init__.py` deleted
- [x] README.md + doc/index.rst written
- [ ] icon.png needed at `static/description/icon.png`
- [ ] banner.png needed at `static/description/banner.png`
- [ ] Screenshots needed (add to `static/description/` and list in manifest `images`)
