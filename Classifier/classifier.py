import math
import pandas as pd

class Classifier:

    def __init__(self, model):
        self.model = model
    
    def predict(self, sample):
        if isinstance(sample, dict):
            sample = pd.Series(sample)

        results = {}
        for label in self.model.class_probs:
            log_prob = math.log(self.model.class_probs[label])
            for feature in self.model.feature_probs.keys():
                value = sample[feature]  # sample חייב להיות Series עם שמות עמודות כאינדקס
                if value in self.model.feature_probs[feature]:
                    prob = self.model.feature_probs[feature][value].get(label, 1e-6)
                else:
                    prob = 1e-6
                log_prob += math.log(prob)
            results[label] = log_prob
        return max(results, key=results.get)

   
