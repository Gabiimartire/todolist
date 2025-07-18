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
    print("Seleccione su espacio de trabajo en el que desea trabajar")
    mostrar_espacios(data)