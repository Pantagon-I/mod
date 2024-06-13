from odoo import models, fields

class CustomModel(models.Model):
    """
    Model for storing custom data with name, age, and active status.
    """
    _name = 'custom.model'
    _description = 'Custom Model'

    name = fields.Char(string='Name', required=True, help='Enter the name of the entity')
    age = fields.Integer(string='Age', help='Enter the age of the entity')
    is_active = fields.Boolean(string='Active', default=True, help='Check to mark as active')

