
class Classifier:
    
    @staticmethod
    def predict(model, sample): 
            probs = {}
            class_probs = model["class_probs"]
            feature_probs = model["feature_probs"]

            for label in class_probs:
                prob = class_probs[label]
                for feature in feature_probs:
                    value = sample[feature]
                    prob *= feature_probs[feature].get(value, {}).get(label, 1e-6) 

            return max(probs, key=probs.get)


   
