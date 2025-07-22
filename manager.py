from Data_Loader.dataLoader import DataLoader
from Cleaning.clean_and_split import CleanAndSplit 
from Builder.build_modle import BuildModel
from Classifier.classifier import Classifier
from Validation.test_model import TestModel

class Manager():

    def __init__(self):
        self.model = None
        self.model_score = None
        self.classifier = None
        self.run()
        

    def run(self):
        df = DataLoader.load_data("Data/labeled_data.csv")
        shuffled_df = CleanAndSplit.shuffl_df(df)
        train_df, test_df = CleanAndSplit.split_df(shuffled_df)

        self.model = BuildModel().fit(train_df)
        self.model_score = TestModel.evaluate(test_df, self.model)
        self.classifier = Classifier(self.model)

    def predict(self, features):
        return self.classifier.predict(features)



