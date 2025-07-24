from Classifier.classifier import Classifier

class TestModel():

    @staticmethod
    def evaluate(model, test_df):
        # הסרת עמודת id
        if 'ID' in test_df.columns:
            test_df = test_df.drop(columns=['ID'])

        predictor = Classifier()
        correct = 0
        total = len(test_df)
        for _, row in test_df.iterrows():
            sample = row.drop('Buy_Computer')  # סדרה של תכונות עם אינדקס שמות עמודות
            actual = row['Buy_Computer']
            prediction = predictor.predict(model,sample)
            if prediction == actual:
                correct += 1
        return f"{(correct / total):.2%}" 