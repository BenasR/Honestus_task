# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrderExtended(models.Model):
    _inherit = 'sale.order'

    @api.depends('order_line.honestus_price', 'order_line.product_uom_qty')
    def compute_total_honestus_price(self):
        """
        Compute the total honestus price from order lines product quantity and
        product honestus price.
        :return: Float
        """
        total_price = 0.0
        for order in self:
            for order_line in order.order_line:
                total_price += order_line.honestus_price * order_line.product_uom_qty
            order.update({'total_honestus_price': total_price})

    total_honestus_price = fields.Float(string="Honestus Price Total",
                                        compute="compute_total_honestus_price",
                                        readonly=True,
                                        store=True)
