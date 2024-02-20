import json
from datetime import datetime

# Definición de la clase Raton
class Raton:
    def __init__(self, identificador, nombre, dias_en_lab, sexo, peso, temperatura, genotipo_x, genotipo_y):
        self.identificador = identificador
        self.nombre = nombre
        self.dias_en_lab = dias_en_lab
        self.sexo = sexo
        self.peso = peso
        self.temperatura = temperatura
        self.genotipo_x = genotipo_x
        self.genotipo_y = genotipo_y
        self.fecha_nacimiento = (datetime.now() - timedelta(days=dias_en_lab)).strftime('%Y-%m-%d')

    def to_dict(self):
        return vars(self)

# Definición de la clase Poblacion
class Poblacion:
    def __init__(self, nombre):
        self.nombre = nombre
        self.ratones = []

    def agregar_raton(self, raton):
        self.ratones.append(raton)

    def eliminar_raton(self, identificador):
        self.ratones = [raton for raton in self.ratones if raton.identificador != identificador]

    def obtener_raton(self, identificador):
        for raton in self.ratones:
            if raton.identificador == identificador:
                return raton
        return None

    def guardar_poblacion(self):
        with open(f"{self.nombre}.json", 'w') as file:
            json.dump([raton.to_dict() for raton in self.ratones], file, indent=4)

# Funciones para la interfaz de usuario de la consola
def main_menu():
    while True:
        print("\nMenu Principal")
        print("1. Crear una nueva poblacion de ratones.")
        print("2. Añadir un nuevo raton a una poblacion existente.")
        print("3. Listar los codigos de referencia de los ratones de una poblacion.")
        print("4. Eliminar un raton de una poblacion.")
        print("5. Mostrar informacion detallada de un raton.")
        print("6. Guardar los datos de una poblacion.")
        print("7. Salir.")
        opcion = input("Seleccione una opcion: ")

        if opcion == '7':
            break
        elif opcion == '1':
            nombre_poblacion = input("Ingrese el nombre de la nueva poblacion: ")
            # Aquí se crearía la nueva población y se guardaría
        elif opcion == '2':
            # Aquí se añadiría un nuevo ratón a una población existente
            pass
        # Implementar las otras opciones aquí.

# Ejecución principal
if __name__ == "__main__":
    main_menu()
