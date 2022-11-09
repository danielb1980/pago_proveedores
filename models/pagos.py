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
    cuenta=fields.Many2one(
        "res.partner",
        string=_("Cuenta"),
        required=True,
        index=True,
        ondelete="restrict"
    )