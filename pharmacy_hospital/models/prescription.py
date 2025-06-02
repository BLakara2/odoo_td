from odoo import models, fields

class Prescription(models.Model):
    _name = 'pharmacy_hospital.prescription'
    _description = "Prescription médicale"

    patient_id = fields.Many2one('hospital.patient', string="Patient", required=True)
    doctor_id = fields.Many2one('hospital_doctor.doctor', string="Médecin", required=True)
    medicine_ids = fields.Many2many('pharmacy.medicine', string="Médicaments prescrits", required=True)
    pharmacy_id = fields.Many2one('pharmacy.pharmacy', string="Pharmacie recommandée")
    date_prescription = fields.Datetime(string="Date de prescription", default=fields.Datetime.now)
