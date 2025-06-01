from odoo import models, fields

class HospitalAdmission(models.Model):
    _name = 'hospital.admission'
    _description = 'Hospital Admission'

    patient_id = fields.Many2one('hospital.patient', string='Patient', required=True)
    admission_date = fields.Date(string='Date d\'admission')
    discharge_date = fields.Date(string='Date de sortie')
