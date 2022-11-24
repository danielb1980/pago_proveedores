from odoo import api,fields,models,_

 
    
class LiquidacionPagos(models.TransientModel):
    _name = 'pago_proveedores.pagos.wizard'
    
    @api.model
    def _default_liquidacion(self):
        return self.env['pago_proveedores.liquidacion'].browse(self._context.get('active_id'))
    
    liquidacion_id = fields.Many2one('pago_proveedores.liquidacion', required=True, default=_default_liquidacion)
    
    medio_de_pago=fields.Selection([("E", "Efectivo"),("T", "Transferencia"),("M", "Mercadopago")],string="Medio de Pago",index=True, default="M")
    currency_id = fields.Many2one(related='company_id.currency_id', depends=["company_id"], store=True, ondelete="restrict")
    company_id = fields.Many2one(
        "res.company",
        string=_("Company"),
        required=True,
        index=True,
        default=lambda self: self.env.user.company_id
    )
    currency_id = fields.Many2one(related='liquidacion_id.currency_id', depends=["liquidacion_id"], store=True, ondelete="restrict")
    partner_id = fields.Many2one(
        "res.partner",
        string=_("Partner"),
        required=True,
        index=True,
        ondelete="restrict",
        related='liquidacion_id.partner_id'
    )

    amount = fields.Monetary('Monto a Pagar')
    partner_bank_id=fields.One2many(related='partner_id.bank_ids')
    partner_account=fields.Char(related='partner_bank_id.acc_number',string=_("CBU/CVU"))
    
    comprobante=fields.Char(string=_("Nº Comprobante"))
    def action_pago(self):
        pago = self.env['pago_proveedores.pagos'].create({'partner_id':self.partner_id.id,'liquidacion_id':self.liquidacion_id.id,'partner_account':self.partner_account,'medio_de_pago':self.medio_de_pago,'comprobante':self.comprobante,'amount':self.amount})
   