from odoo import api,fields,models

class LiquidacionPurchaseMoveLine(models.TransientModel):
    _name = 'pago_proveedores.purchase.move.line'

    def _default_liquidacion(self):
        return self.env['pago_proveedores.liquidacion'].browse(self._context.get('active_id'))

    wizard_id = fields.Many2one('pago_proveedores.purchase.move.wizard',"Wizard")
    currency_id = fields.Many2one(related='purchase_move_id.currency_id', depends=["purchase_move_id"], store=True, ondelete="restrict")
    purchase_move_id = fields.Many2one('purchase.move', string="Factura")
    customer_id = fields.Many2one("res.partner",string="Cliente", related='purchase_move_id.customer_id')
    amount = fields.Monetary(related='purchase_move_id.amount_total')
    invoice_date = fields.Date('Fecha', related="purchase_move_id.invoice_date")
    selected = fields.Boolean("Seleccionada")
    
    
    
class LiquidacionPurchaseMoveWizard(models.TransientModel):
    _name = 'pago_proveedores.purchase.move.wizard'
    
    @api.model
    def _default_liquidacion(self):
        return self.env['pago_proveedores.liquidacion'].browse(self._context.get('active_id'))
    
    @api.model
    def get_lines(self):
        liq = self._default_liquidacion()
        # Busco todas las facturas de este partner que estén en esta liquidacion o en ninguna
        moves = self.env['purchase.move'].search(['&',('partner_id','=',liq.partner_id.id),('liquidacion_id','in',[False,liq.id])])
        lines = []
        for move in moves:
            # Creo una linea por cada factura
            lines.append({
                'wizard_id': self.id,
                'purchase_move_id': move.id,
                'selected': move.liquidacion_id == liq
            })
        return lines
    

    liquidacion_id = fields.Many2one('pago_proveedores.liquidacion', required=True, default=_default_liquidacion)
    line_ids = fields.One2many('pago_proveedores.purchase.move.line','wizard_id', default=get_lines)
    currency_id = fields.Many2one(related='liquidacion_id.currency_id', depends=["liquidacion_id"], store=True, ondelete="restrict")
    amount_selected = fields.Monetary('Monto seleccionado',compute="_compute_selected_amount")
    
    @api.depends('line_ids')
    def _compute_selected_amount(self):
        amounts = self.line_ids.filtered(lambda l: l.selected).mapped('amount')
        print("AMOUNTS",amounts)
        self.amount_selected = sum(amounts) 
        
    def update_selection(self):
        for line in self.line_ids:
            if line.selected:
                line.purchase_move_id.liquidacion_id = self.liquidacion_id.id
            else:
                line.purchase_move_id.liquidacion_id = False
        