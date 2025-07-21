import json
from pathlib import Path
from pages.mostrar import mostrar_espacios
import time
#Verificar si existe el JSON, para saber si en el primer uso lo crea 

ruta = Path("espacios")/"espacios_de_trabajo.json"
ruta.parent.mkdir(parents=True, exist_ok=True)

def verificar_json(ruta_del_json):
    return ruta_del_json.exists()
#Creando la ruta donde debe estar el JSON
if not verificar_json(ruta):
    espacios = []
    #CREAR EL JSON
    with open(ruta, 'w', encoding='utf-8') as archivo:
        json.dump(espacios, archivo, indent=4, ensure_ascii=False)
else:
    with open(ruta, 'r',encoding='utf-8') as archivo:
        data = json.load(archivo)

print("Bienvenido a la aplicación de gestión de espacios de trabajo.")
respuesta = input("Quiere trabajar en un espacio de trabajo existente? (s/n): ").strip().lower()
if respuesta == 's':
    time.sleep(1)
    print("Cargando espacios de trabajo...")
    time.sleep(2)
    print("Seleccione un espacio de trabajo:")
    time.sleep(1)
    mostrar_espacios(data)
    num_espacio = input("Ingrese el número del espacio de trabajo: ")
    #AGREGAR LÓGICA PARA TRABAJAR  CON TABLEROS DEL ESPACIO DE TRABAJO

else:
    time.sleep(1)
    respuesta = input("Quiere [c]rear un nuevo espacio de trabajo? o [b]orrar uno? c/b: ").strip().lower()
    if(respuesta == 'b'):
        print("Borrar un espacio de trabajo.")
        mostrar_espacios(data)
        num_espacio = input("Ingrese el número del espacio de trabajo a borrar: ")
        #AGREGAR LÓGICA PARA BORRAR EL ESPACIO DE TRABAJO
    elif respuesta == 'c':
        print("Crear un nuevo espacio de trabajo.")
        nombre_nuevo_espacio = input("Ingrese el nombre del nuevo espacio de trabajo: ")
        #AGREGAR LÓGICA PARA CREAR NUEVO ESPACIO DE TRABAJO