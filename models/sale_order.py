from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    business_model = fields.Selection([
        ('retail', 'Retail'),
        ('corporate', 'Corporate'),
        ('subscription', 'Subscription')
    ], string="Business Model")

    def name_get(self):
        result = []
        for order in self:
            name = order.name
            if order.business_model:
                short_name = {
                    'retail': '[RT]',
                    'corporate': '[CORP]',
                    'subscription': '[SUB]'
                }.get(order.business_model, '')
                name = f'{short_name} - {name}'
            result.append((order.id, name))
        return result
    
    @api.onchange('business_model')
    def _onchange_business_model(self):
        if self.business_model:
            tax_ids = self.env['account.tax'].search([('business_model', '=', self.business_model)])
            self.order_line.tax_id = False