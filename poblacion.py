class Poblacion:
    def __init__(self, nombre, responsable, dias_en_lab):
        self.nombre = nombre
        self.responsable = responsable
        self.dias_en_lab = int(dias_en_lab)
        self.ratones = {}

    def agregar_raton(self, raton):
        if raton.codigo_ref in self.ratones:
            raise ValueError("Un ratón con ese código ya existe.")
        self.ratones[raton.codigo_ref] = raton

    def eliminar_raton(self, codigo_ref):
        if codigo_ref in self.ratones:
            del self.ratones[codigo_ref]
        else:
            raise KeyError("Código de referencia no encontrado.")

    def modificar_raton(self, codigo_ref, **kwargs):
        raton = self.ratones.get(codigo_ref)
        if not raton:
            raise KeyError("Código de referencia no encontrado.")
        for key, value in kwargs.items():
            if hasattr(raton, key):
                setattr(raton, key, value)
            else:
                raise AttributeError(f"El atributo {key} no es válido para Raton.")

    def obtener_info_raton(self, codigo_ref):
        raton = self.ratones.get(codigo_ref)
        if not raton:
            raise KeyError("Código de referencia no encontrado.")
        return raton.to_dict()

    def listar_codigos(self):
        return list(self.ratones.keys())

    def to_list_of_dicts(self):
        return [raton.to_dict() for raton
