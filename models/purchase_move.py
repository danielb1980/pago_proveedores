from pickle import TRUE
from odoo import fields,models,_
from odoo.exceptions import ValidationError
import logging
_logger = logging.getLogger(__name__)

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
            
        def action_remove_from_liquidacion(self):
            self.liquidacion_id = False
            
        def check(self):
            #_logger.info(all(x == self.partner_id[0] for x in self.partner_id))
            _logger.info(self.partner_id)
            if (all(x == self.partner_id[0] for x in self.partner_id)):
                _logger.info("todos iguales")

                
            else:
                _logger.info("NO SON IGUALEs")
                
                raise ValidationError(_("Debe seleccionar facturas de unb solo Conductor"))
                

            
        
            

                
            
           
            
            
            
 

    