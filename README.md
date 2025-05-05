Titanic Survival Predictor – MLOps Project
Este proyecto aplica buenas prácticas de MLOps para construir un sistema completo de predicción de supervivencia en el Titanic, usando FastAPI, GitHub Actions, Docker y DVC para versionar modelos y datos.

## Integrantes del Proyecto

- Siloé Campos (@siloocv)
- Roselind Vargas (@Roselind26)
- Sebastián Casanova (@Casanova560)

Funcionalidades
Entrenamiento y reentrenamiento automático del modelo

API REST para realizar predicciones en tiempo real

Conteinerización lista para despliegue en producción

CI/CD con GitHub Actions para automatizar flujos

Versionamiento de datos y modelos con DVC

Estructura del Proyecto
graphql
Copiar
Editar
├── principal.py                      # API FastAPI para predicciones
├── train.py                          # Entrenamiento inicial del modelo
├── retrain.py                        # Script de reentrenamiento para CI/CD
├── modelo.pkl                        # Modelo entrenado (Regresión Logística)
├── limpieza_del_titanic.csv          # Dataset limpio de Titanic
├── requisitos.txt                    # Dependencias
├── Dockerfile                        # Imagen de contenedor para despliegue
├── .dockerignore                     # Archivos a excluir del contenedor
├── .dvc/                             # Configuración DVC
├── modelo.pkl.dvc                    # Archivo de versionamiento del modelo
├── .github/
│   └── workflows/
│       └── mlops.yml                 # Pipeline de CI/CD con GitHub Actions
└── README.md                         # Este archivo
Descripción del Proyecto
Entrada: JSON con los siguientes datos de un pasajero:

json
Copiar
Editar
{
  "Pclass": 3,
  "Sex": "male",
  "Age": 22,
  "SibSp": 1,
  "Parch": 0,
  "Fare": 7.25
}
Modelo: Regresión logística entrenada con scikit-learn

Salida:

0 = No sobrevivió

1 = Sobrevivió

API REST: Implementada con FastAPI

Cómo Usar el Proyecto
Entrenar el Modelo
bash
Copiar
Editar
python train.py
Levantar la API Localmente
bash
Copiar
Editar
uvicorn principal:app --reload
Documentación automática disponible en:
http://127.0.0.1:8000/docs

Usar Docker
Build la Imagen:

bash
Copiar
Editar
docker build -t titanic-api .
Correr el Contenedor:

bash
Copiar
Editar
docker run -d -p 8000:8000 titanic-api
Acceso a la API en:
http://localhost:8000/docs

CI/CD
GitHub Actions automatiza:

Reentrenamiento del modelo (workflow mlops.yml)

Despliegue automático de la imagen Docker

Versionamiento con DVC
El proyecto utiliza DVC para versionar el modelo y el dataset.

Para clonar y recuperar los datos:

bash
Copiar
Editar
git clone https://github.com/siloocv/mlops-project.git
cd mlops-project
dvc pull
Recuerda configurar tus credenciales si usas un object storage como AWS S3.

Validación y Seguridad
Validación de entradas: Implementada con FastAPI y Pydantic.


