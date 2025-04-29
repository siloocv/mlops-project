# Titanic Survival Predictor – MLOps Project

Este proyecto aplica buenas prácticas de MLOps para construir un sistema completo de predicción de supervivencia en el Titanic usando FastAPI, GitHub Actions, Docker y DVC.

---

# Estructura del Proyecto

├── principal.py # API FastAPI para predicción ├── train.py # Entrenamiento inicial del modelo ├── retrain.py # Script de reentrenamiento para CI/CD ├── modelo.pkl # Modelo entrenado (regresión logística) ├── limpieza_del_tren_del_titánico.csv # Dataset limpio ├── requisitos.txt # Dependencias ├── Dockerfile # Imagen de contenedor para despliegue ├── .dockerignore # Archivos a excluir del contenedor └── .github/ └── workflows/ └── mlops.yml # Pipeline de CI/CD con GitHub Actions

yaml
Copiar
Editar

---

## Descripción

- **Entrada**: JSON con datos de un pasajero del Titanic  
- **Modelo**: Regresión logística entrenada con `scikit-learn`  
- **Salida**: Predicción (`0 = no sobrevivió`, `1 = sobrevivió`)  
- **API REST**: Implementada con FastAPI  

---

## Entrenamiento del Modelo

python train.py

## Automatización con GitHub Actions

El proyecto implementa dos flujos de trabajo automáticos mediante GitHub Actions:

### 🔄 mlops.yml – Construcción y despliegue automático
- Cada vez que se hace push a las ramas `develop` o `mlops`, se construye automáticamente la imagen Docker del proyecto.
- La imagen es subida a DockerHub de forma continua.
- Se utilizan secretos de GitHub (`DOCKER_USERNAME`, `DOCKER_PASSWORD`) para mantener seguras las credenciales.

### 🤖 retrain.yml – Reentrenamiento automático del modelo
- Workflow que ejecuta el script `retrain.py`, el cual reentrena el modelo de regresión logística.
- Se actualizan automáticamente:
  - El archivo `modelo.pkl`
  - Las métricas (`metrics.txt`)
  - La gráfica de importancia de variables (`feature_importance.png`)
- Si hay cambios en estos archivos, el workflow realiza un commit y push automático a la rama activa.
- Actualmente pendiente de ejecución completa por configuración de secretos.

Estos workflows permiten mantener el sistema actualizado, reproducible y seguro, alineado con buenas prácticas de MLOps.
