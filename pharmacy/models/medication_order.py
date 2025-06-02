from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class MedicationOrder(models.Model):
    _name = 'pharmacy.medication.order'
    _description = "Commande de Médicaments"
    
    name = fields.Char(string='Nom de la commande', required=True)
    patient_id = fields.Many2one('hospital.patient', string='Patient', required=True)
    pharmacy_id = fields.Many2one('pharmacy.pharmacy', string="Pharmacie", required=True)
    order_line_ids = fields.One2many('pharmacy.medication.order.line', 'order_id', string="Lignes de commande")
    order_date = fields.Date(string="Date de commande", default=fields.Date.context_today)
    state = fields.Selection([
        ('draft', 'Brouillon'),
        ('confirmed', 'Validée'),
        ('delivered', 'Livrée'),
        ('cancelled', 'Annulée'),
    ], string="État", default='draft', readonly=True, copy=False, tracking=True)

    def action_confirm(self):
        for order in self:
            for line in order.order_line_ids:
                if line.quantity > line.medicine_id.stock:
                    raise UserError(_("Stock insuffisant pour %s") % line.medicine_id.name)
            order.state = 'confirmed'

    def action_deliver(self):
        for order in self:
            if order.state != 'confirmed':
                raise UserError(_("La commande doit être validée avant livraison."))
            for line in order.order_line_ids:
                med = line.medicine_id
                if line.quantity > med.stock:
                    raise UserError(_("Stock insuffisant pour %s lors de la livraison.") % med.name)
                med.stock -= line.quantity
            order.state = 'delivered'

    def action_cancel(self):
        self.state = 'cancelled'


class MedicationOrderLine(models.Model):
    _name = 'pharmacy.medication.order.line'
    _description = "Ligne de Commande Médicament"

    order_id = fields.Many2one('pharmacy.medication.order', string="Commande", required=True, ondelete='cascade')
    medicine_id = fields.Many2one('pharmacy.medicine', string="Médicament", required=True)
    quantity = fields.Integer(string="Quantité", default=1, required=True)

    @api.constrains('quantity')
    def _check_quantity_positive(self):
        for line in self:
            if line.quantity <= 0:
                raise ValidationError(_("La quantité doit être strictement positive."))
