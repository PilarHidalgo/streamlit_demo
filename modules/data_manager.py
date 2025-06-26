import pandas as pd

def manage_data(file_location):
    data_frame = pd.read_csv(file_location)
    data_frame['age'] = [age+1 if age >= 18 else age for age in data_frame['age']]
    data_frame = data_frame[data_frame['age'].notnull()]
    return data_frame
