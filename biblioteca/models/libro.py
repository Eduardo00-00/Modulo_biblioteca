from odoo import models, fields, api

class Libro(models.Model):
    _name = 'biblioteca.libro'
    _description = 'Libro'

    name = fields.Char(string='Título', required=True)
    apellido = fields.Char(string='Apellido', required=True)
    autor = fields.Char(string='Autor', required=True)
    editorial = fields.Char(string='Editorial', required=True)
    
   
    @api.depends('dar_el_primer_numeros_para_sumar', 'dar_el_segundo_numeros_para_sumar')
    def _compute_resultado_funcion(self):
        for record in self:
            record.resultado = record.dar_el_primer_numeros_para_sumar + record.dar_el_segundo_numeros_para_sumar
            # Aquí puedes agregar la lógica adicional que necesites para calcular el resultado

