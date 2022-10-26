from odoo import fields,models

class PurchaseMove(models.Model):
        _inherit = "purchase.move"
        liquidacion_id=fields.Many2one("pago_proveedores.liquidacion",string="Liquidacion")
        
        def action_liquidate(self):
            # self es un recordset de uno o varios purchase.move
            # chequear que sean todos del mismo partner.
            #crear la liquidacion
            liquidacion = self.env['pago_proveedores.liquidacion'].create({'partner_id':self.partner_id.id})
            
            for record in self:
                #agregar las purchase.move a la liquidacion
                record.liquidacion_id = liquidacion.id
            
            return {
                'name': 'Liquidación',
                'view_mode': 'form',
                'view_id': self.env.ref('pago_proveedores.liquidaciones_form').id,
                'res_model': 'pago_proveedores.liquidacion',
                'type': 'ir.actions.act_window',
                'nodestroy': True,
                'target': 'current',
                'res_id': liquidacion.id,
            }
    