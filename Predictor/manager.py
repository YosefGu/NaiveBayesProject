import requests
import pandas as pd

class Manager():

    def __init__(self):
        self.model = None
        self.test_df = None

    def initilaze(self):
        print("Fetching model from producer...")
        res = requests.get("http://v2-model-container:8001/get-model")  
        self.model = res.json()
        print("Model downloaded and saved.")
        
        data_dict = requests.get("http://v2-model-container:8001/get-test-df").json()
        self.test_df = pd.DataFrame(data_dict)

