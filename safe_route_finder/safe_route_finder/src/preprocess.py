import pandas as pd

def load_crime_data(file_path):
    df = pd.read_csv(file_path)
    return df[['latitude', 'longitude']]
