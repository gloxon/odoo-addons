# -*- coding: utf-8 -*-
# © 2016 Jérôme Guerriat
# © 2016 Niboo SPRL (<https://www.niboo.be/>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models

TYPE2JOURNAL = {
    'out_invoice': 'sale',
    'in_invoice': 'purchase',
    'out_refund': 'sale',
    'in_refund': 'purchase',
}


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    @api.model
    def _default_journal(self):
        """
        This method retrieves the default journal for an invoice
        :return: Default journal for the invoice
        """
        if self._context.get('default_journal_id', False):
            return self.env['account.journal'].browse(
                self._context.get('default_journal_id'))

        inv_type = self._context.get('type', 'out_invoice')
        inv_types = inv_type if isinstance(inv_type, list) else [inv_type]
        company_id = self._context.get('company_id',
                                       self.env.user.company_id.id)

        domain = [
            ('type', 'in', filter(None, map(TYPE2JOURNAL.get, inv_types))),
            ('company_id', '=', company_id),
        ]

        if inv_type == 'in_invoice':
            domain.append(('subtype', '=', 'vendor_bills'))
        return self.env['account.journal'].search(domain, limit=1)

    journal_id = fields.Many2one('account.journal',
                                 default=_default_journal)

    @api.onchange('partner_id', 'company_id')
    def _onchange_partner_id(self):
        """
        This method selects the journal when the partner is updated
        """
        res = super(AccountInvoice, self)._onchange_partner_id()
        currency = self.partner_id.property_purchase_currency_id

        if not self.env.context.get('default_journal_id') and\
                self.partner_id and self.currency_id and\
                self.type in ['in_invoice', 'in_refund'] and\
                self.currency_id != currency:

            journal_domain = [
                ('type', '=', 'purchase'),
                ('company_id', '=', self.company_id.id),
                ('currency_id', '=', currency.id),
            ]

            if self.type == 'in_invoice':
                journal_domain.append(('subtype', '=', 'vendor_bills'))

            default_journal_id = self.env['account.journal'].search(
                journal_domain, limit=1)

            if default_journal_id:
                self.journal_id = default_journal_id
        return res
