from pydantic import BaseModel
from fastapi import FastAPI, status, HTTPException
from fastapi.responses import JSONResponse
import pandas as pd
import joblib
import uuid
import os

class PassengerInput(BaseModel):
    Pclass: int
    Sex: int
    Age: float
    SibSp: int
    Parch: int
    Fare: float
    Embarked_Q: int
    Embarked_S: int

# Crear instancia de la app
api = FastAPI(
    title="MLOps Titanic Predictor",
    description="API para predecir supervivencia en Titanic",
    version="0.0.1",
)

# Cargar el modelo
try:
    current_dir = os.path.dirname(os.path.abspath(__file__))
    model_path = os.path.abspath(os.path.join(current_dir, "..", "model.pkl"))
    print(f"Intentando cargar el modelo desde: {model_path}")
    model = joblib.load(model_path)
except Exception as e:
    model = None
    print(f"Error cargando el modelo: {e}")

@api.get("/", tags=["Root"])
async def root():
    return {"message": "¡API de predicción del Titanic funcionando!"}

@api.post("/predict", tags=["Prediction"])
async def predict(data: PassengerInput):
    if model is None:
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail="Modelo no cargado")

    try:
        # Convertimos los datos de entrada en un DataFrame
        input_data = pd.DataFrame([data.dict()])

        # Realizamos la predicción
        prediction = model.predict(input_data)[0]

        # Devolvemos la respuesta
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "id": str(uuid.uuid4()),
                "prediction": int(prediction),
                "input_data": data.dict()
            }
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Error en la predicción: {str(e)}"
        )
