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

```bash
python train.py
