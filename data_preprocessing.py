import pandas as pd
import os
from datetime import timedelta

def read_data(filename):
    unfiltered = pd.read_csv(os.path.join("CSV Files", filename))
    unfiltered['glucose_level_ts'] = pd.to_datetime(unfiltered['glucose_level_ts'], dayfirst=True)
    unfiltered.drop('glucose_level_mmol/L', axis=1, inplace=True)
    return unfiltered

def preprocess_data(data):
    data['day_of_week'] = data['glucose_level_ts'].dt.dayofweek
    data['day_of_week_name'] = data['glucose_level_ts'].dt.day_name()
    time_step = data['glucose_level_ts'].diff().mode()[0] / timedelta(minutes=1)
    data['bg_rate_of_change'] = data['glucose_level_mg/dL'].diff() / time_step
    return data