import requests
import pandas as pd
import pickle


class Manager():

    def initilaze(self):
        print("Fetching model from producer...")
        res = requests.get("http://model-container:8000/get-model")  # שם הקונטיינר השני
        with open('model.pkl', 'wb') as f:
            f.write(res.content)
        print("Model downloaded and saved.")




    # def get_model():
    #     data = requests.get("http://127.0.0.1:8001/get-model")
    #     return data
    
    # def get_test_df():
    #     data_dict = requests.get("http://127.0.0.1:8001/get-test-data").json()
    #     # return data_dict
    #     return pd.DataFrame(data_dict)
