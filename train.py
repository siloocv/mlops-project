import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib

# 1. Cargar el dataset limpio
df = pd.read_csv("titanic_train_clean.csv")

# 2. Separar variables predictoras (X) y variable objetivo (y)
X = df.drop("Survived", axis=1)
y = df["Survived"]

# 3. Dividir en conjunto de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 4. Crear y entrenar el modelo
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# 5. Evaluar el modelo
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Precisión del modelo: {accuracy:.4f}")

# 6. Guardar el modelo entrenado
joblib.dump(model, "model.pkl")
print("✅ Modelo guardado como 'model.pkl'")
