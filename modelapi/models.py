import joblib
from pydantic import BaseModel, Field

model = joblib.load('model/iris_classifier.joblib')

class ModelInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

class ModelOutput(BaseModel):
    label: str
    prediction: int