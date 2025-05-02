FROM python:3.11

WORKDIR /app

COPY . .

RUN pip install fastapi uvicorn pandas joblib scikit-learn

EXPOSE 8000

CMD ["uvicorn", "api.main:api", "--host", "0.0.0.0", "--port", "8000"]
