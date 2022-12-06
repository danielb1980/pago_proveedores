from odoo import _,models,fields,api

class pagos(models.Model):
    _name = 'pago_proveedores.pagos'
    liquidacion_id=fields.Many2one(
        "pago_proveedores.liquidacion",
        string=_("Liquidacion"),
        required=True,
        index=True,
        ondelete="restrict"
    )
    
    medio_de_pago = fields.Selection([("E", "Efectivo"),("T", "Transferencia"),("M", "Mercadopago")],string="Medio de Pago",index=True, default="M")
    
    partner_id = fields.Many2one(
        "res.partner",
        string=_("Partner"),
        required=True,
        index=True,
        ondelete="restrict"
    )

    company_id = fields.Many2one(
        "res.company",
        string=_("Company"),
        required=True,
        index=True,
        default=lambda self: self.env.user.company_id
    )
    currency_id = fields.Many2one(related='liquidacion_id.currency_id', depends=["liquidacion_id"], store=True, ondelete="restrict")

    amount=fields.Monetary('Monto')

    
    partner_bank_id=fields.One2many(related='partner_id.bank_ids')
    partner_account=fields.Char(related='partner_bank_id.acc_number')
    comprobante=fields.Char(string=_("Nº Comprobante"))
    