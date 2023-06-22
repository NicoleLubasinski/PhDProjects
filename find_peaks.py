from scipy.signal import find_peaks
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def isolate_segment(glucose_sliced, glucose_seg_ts):
    # Example usage of the sliced data
    glucose_segment = glucose_sliced[2]  # Selecting the 3rd segment
    glucose_segment_ts = glucose_seg_ts[2]

    print("Length of glucose segment:", len(glucose_segment))
    
    # Perform clustering algorithm
    
    return isolate_segment

def plot_glucose_segment(glucose_segment_ts, glucose_segment):
    fig = plt.figure()
    ax = fig.add_subplot()

    ax.plot(glucose_segment_ts, glucose_segment)
    fmt = mdates.DateFormatter('%Y-%m-%d %H:%M:%S')
    ax.xaxis.set_major_formatter(fmt)
    fig.autofmt_xdate(bottom=0.2, rotation=30, ha='right')
    plt.show()