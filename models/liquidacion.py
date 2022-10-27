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
    purchase_move_ids= fields.One2many("purchase.move","liquidacion_id",string=_("Facturas"))
    currency_id = fields.Many2one(related='company_id.currency_id', depends=["company_id"], store=True, ondelete="restrict")
    
    monto = fields.Monetary(string="Monto total")
    fecha = fields.Date(string="Fecha Liquidacion", default=fields.Datetime.now)
    
    partner_id = fields.Many2one(
        "res.partner",
        string=_("Partner"),
        required=True,
        index=True,
        ondelete="restrict"
    )
   
    estado = fields.Selection([("B", "Borrador"),("P", "Pendiente"),("C", "Controlado"),("A", "Aprobado"),("P", "Pagado")], default="B")
    observaciones = fields.Text(string="Observaciones")
