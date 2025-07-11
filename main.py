from fastapi import FastAPI
import joblib
from models import schema
from models.predict import MLmodel1


app=FastAPI()

@app.get("/")
def base():
    return {'message': 'Hello World'}

@app.post("/predict")
def get_results(input: schema.HeartInput):
    return MLmodel1(input)
