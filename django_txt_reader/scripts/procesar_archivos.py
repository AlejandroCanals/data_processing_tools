import os

def procesar_archivos_txt(ruta_directorio):
    """
    Procesa archivos de texto en un directorio y devuelve una lista de diccionarios con título,
    autor, fecha y descripción.
    """
    contenidos = []
    for filename in os.listdir(ruta_directorio):
        if filename.endswith(".txt"):  # Verificar si el archivo termina con '.txt'
            ruta_archivo = os.path.join(ruta_directorio, filename)
            with open(ruta_archivo, 'r', encoding='utf-8') as archivo:

                # Inicializar variables para título, autor, fecha y descripción
                titulo = archivo.readline().strip() 
                autor = archivo.readline().strip()
                fecha = archivo.readline().strip()
                descripcion = archivo.readlines()
                descripcion = str(descripcion).strip()
                descripcion = descripcion.replace('[', '').replace(']', '').replace(',', '')

                # Construir diccionario con la información recolectada
                datos_archivo = {
                    "titulo": titulo,
                    "autor": autor,
                    "fecha": fecha,
                    "descripcion": descripcion  # Eliminar espacios adicionales al inicio y final
                }

                contenidos.append(datos_archivo)
    
    return contenidos
