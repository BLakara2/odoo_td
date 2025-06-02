from odoo import models, fields

class Pharmacy(models.Model):
    _name = 'pharmacy.pharmacy'
    _description = "Pharmacie"

    name = fields.Char(string="Nom", required=True)
    address = fields.Char(string="Adresse")
    medicine_ids = fields.One2many('pharmacy.medicine', 'pharmacy_id', string="Médicaments")

class Medicine(models.Model):
    _name = 'pharmacy.medicine'
    _description = "Médicament"

    name = fields.Char(string="Nom", required=True)
    price = fields.Float(string="Prix")
    stock = fields.Integer(string="Stock")
    restock_delay = fields.Integer(string="Délai réapprovisionnement (jours)")
    pharmacy_id = fields.Many2one('pharmacy.pharmacy', string="Pharmacie")

    equivalent_ids = fields.Many2many(
        'pharmacy.medicine', 'medicine_equivalent_rel',
        'medicine_id', 'equivalent_id',
        string="Médicaments équivalents")