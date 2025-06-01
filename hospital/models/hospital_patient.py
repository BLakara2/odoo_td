from odoo import models, fields

class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Hospital Patient'

    name = fields.Char(string='Nom', required=True)
    age = fields.Integer(string='Âge')
    gender = fields.Selection([('male', 'Homme'), ('female', 'Femme')], string='Sexe')
    state = fields.Selection([
        ('new', 'Nouveau'),
        ('treatment', 'En traitement'),
        ('recovering', 'En rémission'),
        ('discharged', 'Sorti'),
    ], string="État", default='new')

    doctor_id = fields.Many2one('hospital_doctor.doctor', string='Médecin')
    disease_id = fields.Many2one('hospital.disease', string='Maladie')
