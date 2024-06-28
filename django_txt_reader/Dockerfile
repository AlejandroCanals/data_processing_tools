# Usa la imagen base oficial de Python
FROM python:3.11-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia todos los archivos y carpetas locales al contenedor
COPY ./ .

# Instala las dependencias necesarias
RUN pip install --no-cache-dir -r requirements.txt

# Puerto en el que la aplicación va a escuchar
EXPOSE 8000

# Comando para ejecutar la aplicación (ajustar según la estructura de tu proyecto)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]