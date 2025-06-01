from odoo import models, fields

class Disease(models.Model):
    _name = 'hospital.disease'
    _description = 'Hospital Disease'

    name = fields.Char(string='Disease Name', required=True)
    symptoms = fields.Text(string='Symptoms')
    severity = fields.Selection([
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ], string='Severity', default='low')

    final_action = fields.Selection([
        ('go_home', 'Go Home'),
        ('stay_hospital', 'Stay in Hospital'),
        ('consult_doctor', 'Consult Doctor'),
    ], string='Final Action', required=True)

    requires_medication = fields.Boolean(string='Requires Medication', default=False)
