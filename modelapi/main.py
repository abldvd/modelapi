import pandas as pd
from fastapi import FastAPI
from modelapi.models import ModelInput, ModelOutput
from modelapi.predicting import get_parsed_prediction

app = FastAPI()

model_name = "Iris Dataset classificator (Vector Support Machine)"
version = "v1.0.0"


@app.get('/')
async def model_info():
    return {
        "name": model_name,
        "version": version
    }


@app.get('/health')
async def service_health():
    return {
        "ok"
    }

@app.post("/predict/", response_model=ModelOutput)
async def predict(input: ModelInput):

    data = pd.json_normalize(input.__dict__)

    prediction = get_parsed_prediction(data)

    log = {"iputs": input.__dict__, "prediction": prediction}

    return prediction