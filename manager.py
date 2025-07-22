from Data_Loader.dataLoader import DataLoader
from Cleaning.clean_and_split import CleanAndSplit 
from Builder.build_modle import BuildModel
from Classifier.classifier import Classifier
from Validation.test_model import TestModel

def run():
    df = DataLoader.load_data("Data/labeled_data.csv")
    shuffled_df = CleanAndSplit.shuffl_df(df)
    train_df, test_df = CleanAndSplit.split_df(shuffled_df)

    model = BuildModel()
    model.fit(train_df)

    print(TestModel.evaluate(test_df, model))

    predictor = Classifier(model)

    sample = {
        "Browser": "Chrome",
        "Device_Type": "Desktop",
        "Is_Student": "Yes",
        "Visited_Site": "Yes",
        "Usage_Frequency": "Low",
        "Income_Level": "Medium"
        }

    print(predictor.predict(sample))

if __name__ == "__main__":
    run()
