from pickle import TRUE
from odoo import fields,models,_
import logging
_logger = logging.getLogger(__name__)

class ResPartner(models.Model):
    _inherit = "res.partner"

    liquidacion_id=fields.Many2one("pago_proveedores.liquidacion",string="Liquidacion")
 
 