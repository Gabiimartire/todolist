#mostrar espacios de trabajo
def mostrar_espacios(espacios_de_trabajo):
    print("Espacios de trabajo disponibles: ")
    for i, espacio in enumerate(espacios_de_trabajo):
        print(f"{i + 1}. {espacio['nombre']}")
    