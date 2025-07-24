from collections import defaultdict

class BuildModel():

    def __init__(self):
        self.class_probs = {}  # P(y)
        self.feature_probs = defaultdict(self._default_nested_dict)  # P(x_i | y)
    
    def _default_nested_dict(self):
        return defaultdict(dict)
    
    def fit(self, df):
        # הסרת עמודת id כי היא לא תכונה שימושית
        if 'ID' in df.columns:
            df = df.drop(columns=['ID'])

        label_col = 'Buy_Computer'
        features = df.columns.drop(label_col)

        label_counts = df[label_col].value_counts()
        total_samples = len(df)

        # חישוב P(y)
        self.class_probs = {label: count / total_samples for label, count in label_counts.items()}

        # חישוב P(x_i | y) עם Laplace smoothing
        for feature in features:
            values = df[feature].unique()
            for value in values:
                for label in label_counts.index:
                    count_label = label_counts[label]
                    count_value_label = len(df[(df[feature] == value) & (df[label_col] == label)])
                    self.feature_probs[feature][value][label] = (count_value_label + 1) / (count_label + len(values))

        return self  

