from odoo import models,fields,api


class liquidacion(models.Model):
    _name = 'pago_proveedores.liquidacion'
    proveedor = fields.Char(string="Proveedor")
    monto = fields.Char(string="Monto total")
    fecha = fields.Date(string="Fecha Liquidacion")
    