from odoo import models, fields, api

class Libro(models.Model):
    _name = 'biblioteca.libro'
    _description = 'Libro'

    name = fields.Char(string='Título', required=True)
    autor = fields.Char(string='Autor', required=True)
    editorial = fields.Char(string='Editorial', required=True)
    fecha_publicacion = fields.Date(string='Fecha de Publicación')
    dar_el_primer_numeros_para_sumar = fields.Integer(string='Dar primer número para sumar')
    dar_el_segundo_numeros_para_sumar = fields.Integer(string='Dar segundo número para sumar')
    resultado = fields.Integer(string='Resultado', compute='_compute_resultado', store=True)

    @api.depends('dar_el_primer_numeros_para_sumar', 'dar_el_segundo_numeros_para_sumar')
    def _compute_resultado(self):
        for record in self:
            record.resultado = record.dar_el_primer_numeros_para_sumar + record.dar_el_segundo_numeros_para_sumar

