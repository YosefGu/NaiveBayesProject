from fastapi import FastAPI
from pydantic import BaseModel

from Classifier.classifier import Classifier
from Validation.test_model import TestModel
from manager import Manager

app = FastAPI()
manager = Manager()

class InputData(BaseModel):
    Browser: str
    Device_Type: str
    Is_Student: str
    Visited_Site: str
    Usage_Frequency: str
    Income_Level: str

@app.on_event("startup")
def startup_event():
    print("start")
    manager.initilaze()
    print("end")

@app.get("/")
def root():
    return {"response": "predict server is running"}

@app.post("/predict")
def predict(sample: InputData):
    try: 
        prediction = Classifier.predict(manager.model, sample)
        return {"prediction": prediction}
    except Exception as e:
        return {"error": f"Model could not be loaded: {str(e)}"}


@app.get("/test-model")
def test_model():
    return TestModel.evaluate(manager.model, manager.test_df)


