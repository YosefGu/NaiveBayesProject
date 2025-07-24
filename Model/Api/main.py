from fastapi import FastAPI
from fastapi.responses import FileResponse

from manager import Manager

app = FastAPI()

manager = Manager()

@app.on_event("startup")
def startup_event():
    print("start")
    manager.run()
    print("end")

@app.get("/")
def root():
    return {"status": "Model server is running!", 
            "model": "Model is builded and ready for testing and predicting"}

@app.get("/get-model")
def get_model():
    return FileResponse("model.pkl", media_type="application/octet-stream", filename="model.pkl")

# @app.get("/get-test-data")
# def get_test_df():
#     pass
    # return manager.get_test_df()

# class InputData(BaseModel):
#     Browser: str
#     Device_Type: str
#     Is_Student: str
#     Visited_Site: str
#     Usage_Frequency: str
#     Income_Level: str


# @app.post("/predict")
# def predict(data: InputData):
#     sample = {
#         "Browser": data.Browser,
#         "Device_Type": data.Device_Type,
#         "Is_Student": data.Is_Student,
#         "Visited_Site": data.Visited_Site,
#         "Usage_Frequency": data.Usage_Frequency,
#         "Income_Level": data.Income_Level
#     }
    
#     prediction = manager.predict(sample)
#     return {"prediction": prediction}

