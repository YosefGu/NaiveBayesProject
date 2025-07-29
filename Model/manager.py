from Data_Loader.dataLoader import DataLoader
from Cleaning.clean_and_split import CleanAndSplit 
from Builder.build_modle import BuildModel


class Manager():

    def __init__(self):
        self.model = None
        self.model_score = None
        self.train_df = None
        self.test_df = None
        

    def run(self):
        print("=== Manager started ===")
        df = DataLoader.load_data("Data/labeled_data.csv")
        shuffled_df = CleanAndSplit.shuffl_df(df)
        self.train_df, self.test_df = CleanAndSplit.split_df(shuffled_df)

        class_probs, feature_probs = BuildModel().fit(self.train_df)
        self.model = {"class_probs" : class_probs, "feature_probs" : feature_probs}
        
        print("=== Model saved successfully ===")

    def get_model(self):
        return self.model
    
    def get_test_df(self):
        return self.test_df.to_dict(orient="records")



