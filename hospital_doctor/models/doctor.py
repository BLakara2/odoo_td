from odoo import models, fields, api

class Doctor(models.Model):
    _name = 'hospital_doctor.doctor'
    _description = 'Doctor'

    name = fields.Char(string='Name', required=True)
    specialization = fields.Char(string='Specialization')
    phone = fields.Char(string='Phone')
    email = fields.Char(string='Email')
    patient_ids = fields.One2many('hospital.patient', 'doctor_id', string='Patients')