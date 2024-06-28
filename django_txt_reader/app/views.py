from django.shortcuts import render
from scripts.procesar_archivos import procesar_archivos_txt
# Create your views here.

def mostrar_datos_serializados(request):
    directorio_de_archivos = 'archivos/' 
    datos_serializados = procesar_archivos_txt(directorio_de_archivos)
    return render(request, 'app/mostrar_datos.html', {'datos_serializados': datos_serializados})