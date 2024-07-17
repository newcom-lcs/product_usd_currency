##############################################################################
# For copyright and license notices, see __manifest__.py file in module root
# directory
##############################################################################
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    @api.depends('company_id')
    def _compute_currency_id(self):
        for template in self:
            if template.currency_id_override:
                template.currency_id = template.currency_id_override
                template.cost_currency_id = template.currency_id_override
            else:
                super(ProductTemplate, self)._compute_currency_id()

    currency_id_override = fields.Many2one(
        'res.currency','Currency'
    )

