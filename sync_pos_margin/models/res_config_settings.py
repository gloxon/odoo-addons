# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    group_pos_margin = fields.Boolean('Margin', implied_group='sync_pos_margin.group_pos_margin', default=False)
