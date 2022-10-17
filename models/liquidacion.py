from odoo import _,models,fields,api


class liquidacion(models.Model):
    _name = 'pagoproveedores.liquidacion'
    proveedor = fields.Char(string="Proveedor")
    monto = fields.Char(string="Monto total")
    fecha = fields.Date(string="Fecha Liquidacion")
    partner_id = fields.Many2one(
        "res.partner",
        string=_("Partner"),
        required=True,
        index=True,
    )
    partner_id2 = fields.Many2one(
        "res.partner",
        string="Partner",
        required=True,
        index=True,
    )