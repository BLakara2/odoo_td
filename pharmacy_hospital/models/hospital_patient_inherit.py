from odoo import models, fields

class HospitalPatient(models.Model):
    _inherit = 'hospital.patient'

    prescription_ids = fields.One2many('pharmacy_hospital.prescription', 'patient_id', string="Prescriptions")
    medication_order_ids = fields.One2many('pharmacy.medication.order', 'patient_id', string="Commandes Médicaments")