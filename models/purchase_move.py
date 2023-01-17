from pickle import TRUE
from odoo import fields,models,_
from odoo.exceptions import ValidationError
import logging
_logger = logging.getLogger(__name__)

class PurchaseMove(models.Model):
        _inherit = "purchase.move"
        liquidacion_id=fields.Many2one("pago_proveedores.liquidacion",string="Liquidacion")
        liquidacion_estado=fields.Selection(related='liquidacion_id.estado')
        
        def action_liquidate(self):
            # self es un recordset de uno o varios purchase.move
            # chequear que sean todos del mismo partner.
            #crear la liquidacion
            total_liquidacion=0
            if (all(x == self.partner_id[0] for x in self.partner_id) ):
                _logger.info("todos iguales")
            
            else:
                _logger.info("NO SON IGUALEs")
                
                raise ValidationError(_("Debe seleccionar facturas de unb solo Conductor"))
            
            for record in self:
                #agregar las purchase.move a la liquidacion
                _logger.info(self.liquidacion_id)
                _logger.info(len(record.liquidacion_id))

                if len(record.liquidacion_id)>0:
                    raise ValidationError(_("Una factura o mas se encuentran incluidas en otra liquidacion"))

            liquidacion = self.env['pago_proveedores.liquidacion'].create({'partner_id':self.partner_id.id})
           
            for record in self:
                #agregar las purchase.move a la liquidacion
                record.liquidacion_id = liquidacion.id
                total_liquidacion+=record.amount_total
            liquidacion.monto=total_liquidacion
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
            
  
                

            
        
            

                
            
           
            
            
            
 

    