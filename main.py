from fastapi import FastAPI, status, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, field_validator
import numpy as np
import joblib

# Inicializamos la app con título y versión
app = FastAPI(
    title="Titanic Survival Predictor",
    version="1.0.0",
    description="API que predice la probabilidad de supervivencia de un pasajero del Titanic."
)

# Cargar el modelo previamente entrenado
model = joblib.load("model.pkl")


class Passenger(BaseModel):
    Pclass: int = Field(..., title="Passenger Class (1, 2, 3)")
    Sex: int = Field(..., title="Sex (0 = female, 1 = male)")
    Age: float = Field(..., title="Age of the passenger")
    SibSp: int = Field(..., title="Number of siblings/spouses aboard")
    Parch: int = Field(..., title="Number of parents/children aboard")
    Fare: float = Field(..., title="Passenger fare")
    Embarked_Q: int = Field(..., title="Embarked at Queenstown (1 if true, 0 if false)")
    Embarked_S: int = Field(..., title="Embarked at Southampton (1 if true, 0 if false)")

    @field_validator("Pclass")
    def validate_pclass(cls, value):
        if value not in [1, 2, 3]:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Pclass must be 1, 2, or 3."
            )
        return value

    @field_validator("Sex")
    def validate_sex(cls, value):
        if value not in [0, 1]:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Sex must be 0 (female) or 1 (male)."
            )
        return value

    @field_validator("Age")
    def validate_age(cls, value):
        if value <= 0 or value > 100:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Age must be between 1 and 100."
            )
        return value


@app.get("/", tags=["Root"])
def home():
    return {"message": "Welcome to the Titanic Survival Predictor API. Go to /docs for Swagger UI."}


@app.post("/predict", tags=["Prediction"])
def predict(passenger: Passenger):
    try:
        # Preparamos los datos en el orden que espera el modelo
        data = np.array([[passenger.Pclass, passenger.Sex, passenger.Age,
                          passenger.SibSp, passenger.Parch, passenger.Fare,
                          passenger.Embarked_Q, passenger.Embarked_S]])

        prediction = model.predict(data)[0]

        if prediction == 1:
            result = "Passenger likely survived."
        else:
            result = "Passenger likely did not survive."

        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={"prediction": result}
        )

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Error during prediction: {str(e)}"
        )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000
    )
