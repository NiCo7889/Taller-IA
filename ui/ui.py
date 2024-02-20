def print_menu():
    print("\nMenu Principal")
    print("1. Abrir una poblacion existente.")
    print("2. Crear una nueva población de ratones.")
    print("3. Añadir un nuevo ratón a una población existente.")
    print("4. Listar códigos de todos los ratones.")
    print("5. Eliminar un ratón de una población.")
    print("6. Modificar los datos de un ratón.")
    print("7. Ver información detallada de un ratón.")
    print("8. Guardar los datos de la población.")
    print("9. Guardar como una nueva población.")
    print("0. Salir.")

def get_input(prompt, validation_func=None):
    while True:
        user_input = input(prompt)
        if not validation_func or validation_func(user_input):
            return user_input
        else:
            print("Entrada inválida, intente de nuevo.")
