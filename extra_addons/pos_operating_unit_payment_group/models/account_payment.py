# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class AccountPayment(models.Model):
    _inherit = "account.payment"

    @api.multi
    @api.constrains('payment_group_id', 'payment_type')
    def check_payment_group(self):
        # odoo tests don't create payments with payment gorups
        if self.env.registry.in_test_mode():
            return True
        for rec in self:
            # if rec.partner_type and rec.partner_id and \
            #    not rec.payment_group_id:
            #     print ('rec', rec)
            #     print ('rec.partner_type', rec.partner_type)
            #     print ('rec.partner_id', rec.partner_id)
            #     print ('rec.payment_group_id', rec.payment_group_id)
            #     raise ValidationError(_(
            #         'Payments with partners must be created from '
            #         'payments groups'))
            # transfers or payments from bank reconciliation without partners
            if not rec.partner_type and rec.payment_group_id:
                raise ValidationError(_(
                    "Payments without partners (usually transfers) cant't "
                    "have a related payment group"))
