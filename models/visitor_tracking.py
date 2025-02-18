from odoo import models, fields, api

class VisitorTracking(models.Model):
    _name = 'visitor_tracking.info'
    _description = 'Visitor Tracking Info'

    # Información geolocalizada del visitante
    ip_address = fields.Char(string='IP Address', required=True)
    country_code = fields.Selection(
        selection=[
            ('AD', 'Andorra'),
            ('AE', 'Emiratos Árabes Unidos'),
            # ... otros países ...
        ],
        string='Country Code',
    )
    city_name = fields.Char(string='City Name')
    longitude = fields.Float(string='Longitude')
    latitude = fields.Float(string='Latitude')
    service_provider = fields.Char(string='Service Provider')
    organization = fields.Char(string='Organization')
    visit_time = fields.Datetime(string='Visit Time')

    # Autenticación con la API de geolocalización
    api_key = fields.Char(
        string="API Key",
        help="The API key used to access the Geolocation API. "
             "Should be defined in your .env file and set as 'APIKEY'."
    )
    