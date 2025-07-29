from fastapi import FastAPI
from pydantic import BaseModel

from manager import Manager

manager = Manager()
app = FastAPI()

class InputData(BaseModel):
    Browser: str
    Device_Type: str
    Is_Student: str
    Visited_Site: str
    Usage_Frequency: str
    Income_Level: str

# Root
@app.get("/")
def root():
    return {"status": "Server is running!"}

# Predict
@app.post("/predict")
def predict(data: InputData):
    sample = {
        "Browser": data.Browser,
        "Device_Type": data.Device_Type,
        "Is_Student": data.Is_Student,
        "Visited_Site": data.Visited_Site,
        "Usage_Frequency": data.Usage_Frequency,
        "Income_Level": data.Income_Level
    }
    
    prediction = manager.predict(sample)
    return {"prediction": prediction}

