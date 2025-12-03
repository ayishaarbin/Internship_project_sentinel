from sklearn.preprocessing import LabelEncoder

def preprocess_dataframe(df):
    encoder = LabelEncoder()
    for col in df.columns:
        if df[col].dtype == 'object':
            df[col] = encoder.fit_transform(df[col])
    return df
