# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api


class PosOrderLine(models.Model):
    _inherit = "pos.order.line"

    purchase_price = fields.Float('Cost Price', compute='_compute_purchase_price', store=True)
    margin = fields.Float('Margin', compute='_compute_product_margin', store=True)
    margin_percentage = fields.Float('Margin Rate', compute='_compute_product_margin', store=True)

    @api.depends('product_id')
    def _compute_purchase_price(self):
        for rec in self:
            rec.purchase_price = rec.product_id.standard_price if rec.product_id else 0.0

    @api.depends('purchase_price')
    def _compute_product_margin(self):
        for rec in self:
            currency = rec.order_id.pricelist_id.currency_id
            rec.margin = currency.round(rec.price_subtotal - (rec.purchase_price * rec.qty))
            if rec.purchase_price > 0 and rec.qty > 0:
                rec.margin_percentage = (rec.margin / (rec.purchase_price * rec.qty))


class PosOrder(models.Model):
    _inherit = "pos.order"

    total_margin = fields.Float('Total Margin', compute='_compute_total_margin', store=True)

    @api.depends('lines.margin')
    def _compute_total_margin(self):
        for rec in self:
            rec.total_margin = sum(rec.lines.mapped('margin'))

