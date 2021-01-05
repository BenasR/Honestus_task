# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.addons import decimal_precision as dp


class SaleOrderLineExtended(models.Model):
    _inherit = 'sale.order.line'

    @api.depends('honestus_price', 'price_unit')
    def compute_margin(self):
        """
        Compute sale order line product's margin.
        :return: Float
        """
        for line in self:
            product_unit_price = line.honestus_price if line.honestus_price > 0 else line.price_unit
            line.product_margin = product_unit_price - line.product_id.standard_price / product_unit_price

    honestus_code = fields.Char(related='product_id.honestus_code',
                                readonly=True)
    honestus_price = fields.Float(related='product_id.honestus_price',
                                  readonly=True)
    product_code = fields.Char(related='product_id.default_code',
                               readonly=True)
    standard_price = fields.Float(relates='product_id.standard_price',
                                  readonly=True)
    product_margin = fields.Float(string="Margin",
                                  compute='compute_margin',
                                  readonly=True,
                                  store=True,
                                  digits=dp.get_precision('Product Price'))
