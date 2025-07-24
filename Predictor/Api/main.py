import pickle
from fastapi import FastAPI
from pydantic import BaseModel

from Classifier.classifier import Classifier
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
    with open("model.pkl", "rb") as f:
        model = pickle.load(f)
    prediction = Classifier.predict(model, sample)
    return {"prediction": prediction}


# @app.get("/test-model")
# def test_model():
#     model= Utils.get_model()
#     test_df = Utils.get_test_df()
#     # return {"model": model, "df" : test_df}
#     return TestModel.evaluate(model, test_df)


