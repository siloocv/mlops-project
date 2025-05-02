FROM python:3.11

WORKDIR /app

COPY . .

# Si no estás segura de que requirements.txt tiene todo
RUN pip install --no-cache-dir fastapi uvicorn pandas joblib scikit-learn

EXPOSE 8000

CMD ["uvicorn", "api.main:api", "--host", "0.0.0.0", "--port", "8000"]
