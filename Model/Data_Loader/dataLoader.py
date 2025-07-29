import pandas as pd

class DataLoader():
    @staticmethod
    def load_data(csv_file):
        try:
           df = pd.read_csv(csv_file)
           return df
        except Exception as e:
            print(e)


    