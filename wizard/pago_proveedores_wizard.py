from odoo import api,fields,models

 
    
class LiquidacionPagos(models.TransientModel):
    _name = 'pago_proveedores.pagos.wizard'
    
    @api.model
    def _default_liquidacion(self):
        return self.env['pago_proveedores.liquidacion'].browse(self._context.get('active_id'))
    
    liquidacion_id = fields.Many2one('pago_proveedores.liquidacion', required=True, default=_default_liquidacion)
    currency_id = fields.Many2one(related='liquidacion_id.currency_id', depends=["liquidacion_id"], store=True, ondelete="restrict")
    amount = fields.Monetary('Monto seleccionado')
    
   