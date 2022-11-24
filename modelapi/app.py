from fastapi import FastAPI
from modelapi import training

app = FastAPI()

@app.post("/predict/")
async def predict():
    return pass