from odoo import models, fields, api
from odoo.exceptions import UserError
import requests
import logging

# Configurar el logger
_logger = logging.getLogger(__name__)

class VisitorTracking(models.Model):
    _name = 'visitor_tracking.info'
    _description = 'Visitor Tracking'
    