from odoo import models, fields, api

class AccountTax(models.Model):
    _inherit = 'account.tax'

    business_model = fields.Selection([
        ('retail', 'Retail [RT]'),
        ('corporate', 'Corporate [CORP]'),
        ('subscription', 'Subscription [SUB]')
    ], string='Business Model')