import json
from pathlib import Path
from pages.mostrar import mostrar_espacios
#Verificar si existe el JSON, para saber si en el primer uso lo crea 
def verificar_json(ruta_del_json):
    return ruta_del_json.exists()
ruta = Path("espacios")/"espacios_de_trabajo.json"

if not verificar_json(ruta):
    espacios = []
    json_nuevo = "espacios_de_trabajo.json"
    #CREAR EL JSON
    with open(ruta, 'w', encoding='utf-8') as archivo:
        json.dump(espacios, archivo, indent=4, ensure_ascii=False)
else:
    ruta = Path("espacios")/"espacios_de_trabajo.json"
    with open(ruta, 'r',encoding='utf-8') as archivo:
        data = json.load(archivo)

print("Bienvenido a la aplicación de gestión de espacios de trabajo.")
print("Quiere trabajar en un espacio de trabajo existente? (s/n)")
respuesta = input().strip().lower()
if respuesta == 's':
    print("Cargando espacios de trabajo...")
    print("Seleccione un espacio de trabajo:")
    mostrar_espacios(data)
    num_espacio = input("Ingrese el número del espacio de trabajo: ")
    #AGREGAR LÓGICA PARA TRABAJAR  CON TABLEROS DEL ESPACIO DE TRABAJO

else:
    respuesta = input("Quiere [c]rear un nuevo espacio de trabajo? o [b]orrar uno? c/b").strip().lower()
    if(respuesta == 'b'):
        print("Borrar un espacio de trabajo.")
        mostrar_espacios(data)
        num_espacio = input("Ingrese el número del espacio de trabajo a borrar: ")
        #AGREGAR LÓGICA PARA BORRAR EL ESPACIO DE TRABAJO
    elif respuesta == 'c':
        print("Crear un nuevo espacio de trabajo.")
        nombre_nuevo_espacio = input("Ingrese el nombre del nuevo espacio de trabajo: ")
        #AGREGAR LÓGICA PARA CREAR NUEVO ESPACIO DE TRABAJO