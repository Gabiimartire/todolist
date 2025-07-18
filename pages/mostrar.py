#mostrar espacios de trabajo
def mostrar_espacios(espacios_de_trabajo):
    print("Espacios de trabajo disponibles: ")
    for espacio in espacios_de_trabajo:
        print("* ", espacio['nombre'])
    