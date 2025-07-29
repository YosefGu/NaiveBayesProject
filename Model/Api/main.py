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
    return manager.get_model()

@app.get("/get-test-df")
def get_test_df():
    return manager.get_test_df()


