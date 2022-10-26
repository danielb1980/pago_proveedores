from operator import truediv
from odoo import _,models,fields,api


class liquidacion(models.Model):
    _name = 'pago_proveedores.liquidacion'
    
    # Los documentos en Odoo tienen una compania y una moneda asignada, que facilita el procesamiento de montos.
    # Definidos asi, se calculan automaticamente desde el usuario que los crea
    company_id = fields.Many2one(
        "res.company",
        string=_("Company"),
        required=True,
        index=True,
        default=lambda self: self.env.user.company_id
    )
    purchase_move_ids= fields.One2many("purchase.move","id",string=_("Facturas"),required=True)
    
    currency_id = fields.Many2one(related='company_id.currency_id', depends=["company_id"], store=True, ondelete="restrict")
    
    # Usar partner_id para identificar al proveedor
    #proveedor = fields.Char(string="Proveedor") 
    
    monto = fields.Monetary(string="Monto total")
    fecha = fields.Date(string="Fecha Liquidacion", default=fields.Datetime.now)
    
    partner_id = fields.Many2one(
        "res.partner",
        string=_("Partner"),
        required=True,
        index=True
    )
    LiquidacionLine_ids=fields.One2many("pago_proveedores.liquidacion.line","liquidacion_id",_("Facturas"))
    estado = fields.Selection([("B", "Borrador"),("A", "Aprobado")])
    observaciones = fields.Text(string="Observaciones")
class LiquidacionLine(models.Model):
    _name = 'pago_proveedores.liquidacion.line'
    factura=fields.Many2one("purchase.move",string="Factura")
      
    liquidacion_id=fields.Many2one("pago_proveedores.liquidacion",string="Liquidacion")
    