from odoo import models, fields, api
import requests


class VisitorTracking(models.Model):
    _name = 'visitor.tracking'
    _description = 'Información de Seguimiento de Visitantes'

    ip_address = fields.Char(string='Dirección IP', readonly=True)
    country = fields.Char(string='País', readonly=True)
    city = fields.Char(string='Ciudad', readonly=True)
    longitude = fields.Float(string='Longitud', readonly=True)
    latitude = fields.Float(string='Latitud', readonly=True)
    service_provider = fields.Char(string='Proveedor de Servicios', readonly=True)
    organization = fields.Char(string='Organización', readonly=True)
    visit_time = fields.Datetime(string='Hora de Visita', default=fields.Datetime.now, readonly=True)
    api_key = fields.Char(string='Clave API', required=True)

    def action_get_location(self):
        # Usar la API key del campo del formulario en lugar de la variable de entorno
        api_key = self.api_key
        if not api_key:
            raise models.ValidationError('Por favor ingrese una clave API válida')

        try:
            # Obtener IP pública
            ip_response = requests.get('https://api.ipify.org?format=json')
            ip_address = ip_response.json()['ip']

            # Obtener información de geolocalización
            url = f'https://api.ipgeolocation.io/ipgeo?apiKey={api_key}&ip={ip_address}'
            response = requests.get(url)
            data = response.json()

            self.write({
                'ip_address': ip_address,
                'country': data.get('country_name'),
                'city': data.get('city'),
                'longitude': float(data.get('longitude', 0)),
                'latitude': float(data.get('latitude', 0)),
                'service_provider': data.get('isp'),
                'organization': data.get('organization'),
            })

        except Exception as e:
            raise models.ValidationError(f'Error al obtener datos de ubicación: {str(e)}')