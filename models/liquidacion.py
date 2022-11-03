from operator import truediv
from xml.dom import ValidationErr
from odoo import _,models,fields,api
import logging

_logger = logging.getLogger(__name__)


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
    monto2= fields.Monetary(string="Total Liquidado",compute="_compute_amount")
    fecha = fields.Date(string="Fecha Liquidacion", default=fields.Datetime.now)
    
    partner_id = fields.Many2one(
        "res.partner",
        string=_("Partner"),
        required=True,
        index=True,
        ondelete="restrict"
    )
    
    estado = fields.Selection([("B", "Borrador"),("E", "Enviado"),("C", "Controlado"),("A", "Aprobado"),("P", "Pagado")],string="Estado",index=True, default="B")
    observaciones = fields.Text(string="Observaciones")
   
    @api.onchange('purchase_move_ids')
    def check_liquidacion_id(self):
        facturas=self.env['purchase.move']
        _logger.info(self.purchase_move_ids)
        for record in facturas:
            _logger.info(record.liquidacion_id)
            if record.liquidacion_id!=False:
                
                raise ValidationErr("la factura ya fue incluida en otra liquidacion")


    def action_enviado(self):
          self.ensure_one()
          self.estado=('E')

    def action_controlado(self):
          self.ensure_one()
          self.estado=('C')

    def action_aprobado(self):
          self.ensure_one()
          self.estado=('A')
    def action_pagado(self):
          self.ensure_one()
          self.estado=('P')

    @api.depends('purchase_move_ids')
    def _compute_amount(self):
        amounts=0
        for x in self.purchase_move_ids:
            amounts+= x.amount_total
        self.monto2 = amounts 
       
