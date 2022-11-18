from odoo import api,fields,models,_

 
    
class LiquidacionPagos(models.TransientModel):
    _name = 'pago_proveedores.pagos.wizard'
    
    @api.model
    def _default_liquidacion(self):
        return self.env['pago_proveedores.liquidacion'].browse(self._context.get('active_id'))
    
    liquidacion_id = fields.Many2one('pago_proveedores.liquidacion', required=True, default=_default_liquidacion)
    currency_id = fields.Many2one(related='liquidacion_id.currency_id', depends=["liquidacion_id"], store=True, ondelete="restrict")
    medio_de_pago=fields.Selection([("E", "Efectivo"),("T", "Transferencia"),("M", "Mercadopago")],string="Medio de Pago",index=True, default="M")
    cuenta=fields.Many2one(
        "res.partner",
        string=_("Cuenta"),
        required=True,
        index=True,
        ondelete="restrict"
    )
    partner_id = fields.Many2one(
        "res.partner",
        string=_("Partner"),
        required=True,
        index=True,
        ondelete="restrict",
        related='liquidacion_id.partner_id'
    )

    amount = fields.Monetary('Monto seleccionado')
    partner_bank_id=fields.One2many(related='partner_id.bank_ids')
    partner_account=fields.Char(related='partner_bank_id.acc_number',string=_("CBU/CVU"))
    comprobante=fields.Char(string=_("Nº Comprobante"))
   