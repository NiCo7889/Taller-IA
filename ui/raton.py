from datetime import datetime, timedelta

class Raton:
    def __init__(self, codigo_ref, fecha_nac, peso, sexo, temp, gen_x, gen_y, notas=''):
        self.codigo_ref = codigo_ref
        self.fecha_nac = datetime.strptime(fecha_nac, '%Y-%m-%d')
        self.peso = int(peso)
        self.sexo = sexo
        self.temp = float(temp)
        self.gen_x = gen_x
        self.gen_y = gen_y
        self.notas = notas

    def es_esteril(self):
        return (self.sexo == 'Macho' and self.gen_x == 'Mutado') or \
               (self.sexo == 'Hembra' and self.gen_x == 'Mutado' and 'Mutado' in self.notas)

    def es_poligamo(self):
        return self.sexo == 'Macho' and self.gen_y == 'Mutado'

    def to_dict(self):
        return {
            'codigo_ref': self.codigo_ref,
            'fecha_nac': self.fecha_nac.strftime('%Y-%m-%d'),
            'peso': self.peso,
            'sexo': self.sexo,
            'temp': self.temp,
            'gen_x': self.gen_x,
            'gen_y': self.gen_y,
            'notas': self.notas
        }
