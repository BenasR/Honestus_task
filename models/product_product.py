# -*- coding: utf-8 -*-

from odoo import models, fields


class ProductProductExtended(models.Model):
    _inherit = 'product.product'

    honestus_code = fields.Char(string="Honestus Code")
    honestus_price = fields.Float(string="Honestus Price")
