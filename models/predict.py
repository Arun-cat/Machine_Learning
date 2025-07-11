import joblib
from models.schema import HeartInput
import os

model = joblib.load(os.path.join(os.path.dirname(__file__), "../Heart_disease.pkl"))


def MLmodel1(input: HeartInput):
    data = list(input.dict().values())
    try:
        results = model.predict([data])[0]
        return {'message': 'will get HeartDisease'} if results == 1 else {'message': 'will not get HeartDisease'}
    except Exception as e:
        return {'message': str(e)}