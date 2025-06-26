import pandas as pd

def handle_dataset(path):
    df = pd.read_csv(path)
    df['age'] = df['age'].apply(lambda x: x + 1 if x > 18 else x)
    df = df.dropna(subset=['age'])
    return df
