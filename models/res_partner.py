from pickle import TRUE
from odoo import fields,api,models,_
import logging
_logger = logging.getLogger(__name__)

class ResPartner(models.Model):
    _inherit = "res.partner"

    liquidacion_ids=fields.One2many("pago_proveedores.liquidacion","partner_id",string="Liquidacion")
    pago_proveedores_liquidacion_count = fields.Integer(_('Liquidaciones_count'), compute='_compute_pago_proveedores_liquidacion_count')
    
    #monto_facturado = fields.Monetary(_('facturas_suma'), compute='_compute_purchase_move_suma')
    #monto_liquidado = fields.Monetary(_('facturas_liquidadas_suma'), compute='_compute_liquidaciones_suma')
    #monto_pagado = fields.Monetary(_('pagos_suma'), compute='_compute_pago_proveedores_liquidacion_count')
    #monto_pendiente = fields.Monetary(_('facturas_no_liquidadas_suma'), compute='_compute_pago_proveedores_liquidacion_count')
    
    @api.depends('liquidacion_ids')
    def _compute_pago_proveedores_liquidacion_count(self):
        for partner in self:
            print("liquidaciones",partner.pago_proveedores_liquidacion_count)
            if partner.towing_driver:
                partner.pago_proveedores_liquidacion_count = len(partner.liquidacion_ids)
            else:
                partner.pago_proveedores_liquidacion_count=0
    
    def action_open_pago_proveedores_liquidacion(self):
        for partner in self:
            action = self.env.ref("pago_proveedores.action_liquidaciones").read()[0]
            action["context"] = {}
            action["domain"] = [("id", "in", partner.liquidacion_ids.ids)]
            return action


            