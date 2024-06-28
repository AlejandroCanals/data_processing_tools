import json

#Ejercicio para encontrar el coche mas vendido de los objetos json


#Abro archivo
with open('data_json/data.json','r') as file:
        objetos = json.load(file)

#Asigno una variable para el maximo de ventas
max_total_sales = 0


#Recorro el objeto y encuentro el coche mas vendido comparando los valores de sus ventas con mi variable max_total_sales
for data in objetos:

    total_sales = data["total_sales"]
    if total_sales > max_total_sales:
          max_total_sales = total_sales
          most_selled_car = data


print(most_selled_car)
print(f'El coche mas vendido es {most_selled_car["car"]["car_make"]} con un precio de {most_selled_car["price"]} , un total de ventas de {most_selled_car["total_sales"]} del año {most_selled_car["car"]["car_year"]}')