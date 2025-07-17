import json
from pathlib import Path
print("Buenasss")
#Verificar si existe el JSON, para saber si en el primer uso lo crea 
def verificar_json(ruta_del_json):
    return ruta_del_json.exists()

ruta = Path("espacios")/"espacios_de_trabajo.json"

if not verificar_json(ruta):
    espacios = [{}]
    json_nuevo = "espacios_de_trabajo.json"
    #CREAR EL JSON
    with open(ruta, 'w', encoding='utf-8') as archivo:
        json.dump(espacios, archivo, indent=4, ensure_ascii=False)
    print("Cree su primer espacio de trabajo")
else:
    print("Seleccione su espacio de trabajo en el que desea trabajar")
