import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib
import os

def retrain_model(data_path="titanic_train_clean.csv", model_output="model.pkl"):
    # 1. Cargar dataset
    df = pd.read_csv(data_path)

    # 2. Separar variables
    X = df.drop("Survived", axis=1)
    y = df["Survived"]

    # 3. División train/test
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # 4. Entrenar modelo
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)

    # 5. Evaluar
    accuracy = accuracy_score(y_test, model.predict(X_test))
    print(f"[Reentrenamiento] Precisión: {accuracy:.4f}")

    # 6. Guardar modelo
    joblib.dump(model, model_output)
    print(f"[Reentrenamiento] Modelo guardado en '{model_output}'")

if __name__ == "__main__":
    retrain_model()
