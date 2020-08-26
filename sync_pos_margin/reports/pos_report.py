# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _


class PosOrderReport(models.Model):
    _inherit = "report.pos.order"

    margin = fields.Float('Margin', groups="sync_pos_margin.group_pos_margin", readonly=True)
    margin_percentage = fields.Float('Margin Rate', groups="sync_pos_margin.group_pos_margin", readonly=True)

    def _select(self):
        return super(PosOrderReport, self)._select() + ", l.margin AS margin, l.margin_percentage AS margin_percentage"

    def _group_by(self):
        return super(PosOrderReport, self)._group_by() + ", l.margin, l.margin_percentage"
