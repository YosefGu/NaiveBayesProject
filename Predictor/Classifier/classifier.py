

class Classifier:
    
    @staticmethod
    def predict(model, sample):  # sample: dict[str, str]
        probs = {}
        for label in model.class_probs:
            prob = model.class_probs[label]
            for feature in model.feature_probs:
                value = sample[feature]
                prob *= model.feature_probs[feature].get(value, {}).get(label, 1e-6)  # כדי להימנע מ-KeyError
            probs[label] = prob
        return max(probs, key=probs.get)


   
