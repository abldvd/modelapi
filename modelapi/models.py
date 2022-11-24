import joblib
from pydantic import BaseModel, Field

model = joblib.load('./modelapi/model/iris_classifier.joblib')

class ModelInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

    class Config:
        schema_extra = {
            "example":{
                "sepal_length": 5.,
                "sepal_width": 3.5,
                "petal_length": 1.5,
                "petal_width": 2
            }
        }

class ModelOutput(BaseModel):
    label: str
    prediction: int