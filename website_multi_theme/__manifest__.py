# -*- coding: utf-8 -*-
# Copyright 2015 Antiun Ingenieria S.L. - Antonio Espinosa
# Copyright 2017 Jairo Llopis <jairo.llopis@tecnativa.com>
# Copyright 2018 Ivan Yelizariev <https://it-projects.info/team/yelizariev>
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

{
    "name": "Website Multi Theme",
    "summary": "Support different theme per website",
    "version": "10.0.1.3.3",
    "category": "Website",
    "website": "https://www.tecnativa.com",
    "author": "Tecnativa, IT-Projects LLC, Odoo Community Association (OCA)",
    "license": "LGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "website",
    ],
    "data": [
        "security/ir.model.access.csv",
        "wizards/website_config_settings_view.xml",
        "data/themes_bootswatch.xml",
        "data/themes_private.xml",
        "templates/assets.xml",
        "templates/patterns.xml",
        "data/themes_default.xml",
        "views/ir_ui_view.xml",
    ],
    "demo": [
        "demo/pages.xml",
        "demo/themes.xml",
    ],
    "external_dependencies": {
        "bin": [
            "lessc",
            "sass",
            "scss",
        ],
    },
}
