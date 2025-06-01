from odoo import models, fields, api
from datetime import datetime, timedelta

class HospitalNurse(models.Model):
    _name = 'hospital.nurse'
    _description = 'Infirmière'

    name = fields.Char(string='Nom', required=True)
    round_ids = fields.One2many('hospital.round', 'nurse_id', string="Rondes")

    def get_ronde_jour(self):
        today = fields.Date.context_today(self)
        return self.round_ids.filtered(lambda r: r.date == today and not r.done)

    def get_ronde_semaine(self):
        today = fields.Date.context_today(self)
        end_week = today + timedelta(days=6 - today.weekday())
        return self.round_ids.filtered(lambda r: today <= r.date <= end_week and not r.done)
    
    def print_week_rounds(self):
        return self.env.ref('hospital_nurse.action_report_week_rounds').report_action(self)

class HospitalRound(models.Model):
    _name = 'hospital.round'
    _description = 'Ronde infirmière'

    nurse_id = fields.Many2one('hospital.nurse', string='Infirmière', required=True)
    patient_id = fields.Many2one('hospital.patient', string='Patient', required=True)
    date = fields.Date(string='Date de la ronde', required=True)
    description = fields.Text(string='Observations')
    done = fields.Boolean(string='Ronde effectuée', default=False)

    def action_marquer_faite(self):
        self.done = True

    def action_liberer_patient(self):
        self.patient_id.state = 'discharged'
        self.done = True

    def action_programmer_ronde(self, date, description):
        self.env['hospital.round'].create({
            'nurse_id': self.nurse_id.id,
            'patient_id': self.patient_id.id,
            'date': date,
            'description': description,
        })
