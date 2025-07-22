import math
import pandas as pd

class Classifier:

    def __init__(self, model):
        self.model = model
    
    def predict(self, sample):  # sample: dict[str, str]
        probs = {}
        for label in self.model.class_probs:
            prob = self.model.class_probs[label]
            for feature in self.model.feature_probs:
                value = sample[feature]
                prob *= self.model.feature_probs[feature].get(value, {}).get(label, 1e-6)  # כדי להימנע מ-KeyError
            probs[label] = prob
        return max(probs, key=probs.get)


   
