from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

model = joblib.load("model.pkl")

app = FastAPI(title="Titanic Survival Predictor")

class Passenger(BaseModel):
    Pclass: int
    Sex: int
    Age: float
    SibSp: int
    Parch: int
    Fare: float
    Embarked_Q: int
    Embarked_S: int

@app.get("/")
def home():
    return {"message": "API para predecir supervivencia en Titanic"}

@app.post("/predict")
def predict(passenger: Passenger):
    data = np.array([[passenger.Pclass, passenger.Sex, passenger.Age,
                      passenger.SibSp, passenger.Parch, passenger.Fare,
                      passenger.Embarked_Q, passenger.Embarked_S]])
    
    prediction = model.predict(data)[0]
    
    return {"prediction": int(prediction)}
