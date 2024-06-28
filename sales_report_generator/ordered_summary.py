import json
 

# Cargar los objetos desde el archivo JSON

def ordenar_datos():
    with open('data.json', 'r') as file:
        objetos = json.load(file)

    # Inicializar una lista vacía para almacenar los objetos ordenados
    datos_ordenados = []

    # Iterar sobre cada objeto y ordenarlos por 'total_sales'
    while objetos:
        max_total_sales = -1
        most_selled_car = None
        
        # Encontrar el objeto con más ventas en la lista restante
        for data in objetos:
            total_sales = data["total_sales"]
            if total_sales > max_total_sales:
                max_total_sales = total_sales
                most_selled_car = data
        
        # Agregar el objeto con mas ventas a la lista ordenada y removerlo de la lista original
        datos_ordenados.append(most_selled_car)
        objetos.remove(most_selled_car)

    return datos_ordenados

# Imprimir los objetos ordenados por ventas
"""for obj in datos_ordenados:
    print(obj)
    pass
"""

ordenar_datos()