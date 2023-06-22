import numpy as np
from datetime import timedelta

def slice_data(data, time_step, n_samples):
    timestamp = np.array(data['glucose_level_ts'], dtype=float)
    glucose = np.array(data['glucose_level_mg/dL'], dtype=float)
    n_samples_per_segment = int(time_step * 60 / timedelta(minutes=1)) * n_samples
    glucose_seg_ts = []
    glucose_sliced = []
    
    for start_ts in data['bolus_start_ts']:
        start_index = np.argmax(timestamp >= start_ts)
        end_index = start_index + n_samples_per_segment
        if end_index <= len(data):
            glucose_seg_ts.append(timestamp[start_index:end_index])
            glucose_sliced.append(glucose[start_index:end_index])
    
    return glucose_sliced, glucose_seg_ts
