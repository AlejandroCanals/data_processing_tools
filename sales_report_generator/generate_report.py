import os
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet 
from ordered_summary import ordenar_datos
#Esta funcion genera una tabla en un pdf con los reportes extraido del script ordered_summary que coge los datos del archivo json.


def generar_pdf(reportes,nombre_archivo,ruta_carpeta):

    ruta_completa = os.path.join(ruta_carpeta,nombre_archivo)

    pdf = SimpleDocTemplate(ruta_completa, pagesize=letter)

    # Contenido del PDF
    elementos = []

    # Estilos de texto
    styles = getSampleStyleSheet()
    estilo_titulo = styles['Heading1']
    estilo_titulo.alignment = 1  # Alineación centrada
    elementos.append(Spacer(1, 12))  # Espacio entre título y tabla

    # Título
    titulo = Paragraph("Reporte de Ventas", estilo_titulo)
    elementos.append(titulo)

    # Tabla de reportes
    data = [["id", "Marca", "Modelo", "Ventas Totales"]]

    for reporte in reportes:
        data.append([str(reporte["id"]), reporte["car"]["car_make"], reporte["car"]["car_model"], str(reporte["total_sales"])])
    
    tabla = Table(data)

    # Estilo de la tabla
    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),  # Encabezado de fondo gris
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),  # Color de texto blanco para el encabezado
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Alinear todo el contenido al centro
        ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),  # Cuadrícula interna con ancho y color
        ('BOX', (0, 0), (-1, -1), 0.25, colors.black),  # Borde de la tabla con ancho y color
    ])
    tabla.setStyle(style)

    elementos.append(tabla)

    pdf.build(elementos)
    print(f"Se ha generado el PDF en: {ruta_completa}")



if __name__ == "__main__":
    # Solicitar nombre de archivo al usuario
    nombre_archivo = input('Introduce un nombre para generar un archivo PDF: ').strip() + '.pdf'

    # Ruta donde se guardarán los PDFs generados
    ruta_carpeta = 'pdfs_generados'
    # Obtener los datos ordenados
    try:
        reportes = ordenar_datos()
    except FileNotFoundError:
        print("No se encontró el archivo JSON 'data.json'. Asegúrate de que esté en la carpeta 'data'.")
    except Exception as e:
        print(f"Ocurrió un error al ordenar los datos: {str(e)}")
    else:
        # Generar el PDF con los reportes ordenados
        generar_pdf(reportes, nombre_archivo, ruta_carpeta)