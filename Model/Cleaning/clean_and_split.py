
class CleanAndSplit():

    @staticmethod
    def shuffl_df(df):
        return df.sample(frac=1, random_state=42)

    @staticmethod
    def split_df(df):
        train_df = df[:int(0.7 * len(df))]
        test_df = df[int(0.7 * len(df)):]
        return train_df, test_df

