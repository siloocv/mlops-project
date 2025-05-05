# Imagen base
FROM python:3.11-slim

# Setear directorio de trabajo
WORKDIR /app

# Copiar archivos del proyecto
COPY . .

# Instalar dependencias y DVC con soporte para S3
RUN pip install --no-cache-dir -r requirements.txt \
    && pip install dvc[s3]

# Exponer puerto
EXPOSE 8000

# Descargar el modelo desde DVC antes de arrancar la API
CMD dvc pull && uvicorn main:app --host 0.0.0.0 --port 8000

