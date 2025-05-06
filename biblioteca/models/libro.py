from odoo import models, fields

class Libro(models.Model):
    _name = 'biblioteca.libro'
    _description = 'Libro'

    name = fields.Char(string='Título', required=True)
    autor = fields.Char(string='Autor')
    fecha_publicacion = fields.Date(string='Fecha de Publicación')
