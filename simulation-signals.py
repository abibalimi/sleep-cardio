#/usr/bin/env python3

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# SETUP
def setup() -> pd.DataFrame:
    """Generate heart rate and sleep stages signals"""
    
    # Simulate time (1-minute resolution for 8 hours)
    time = pd.date_range(start='2025-07-10 22:00', periods=480, freq='T')  # 8 hours

        
    # Simulate heart rate (bpm): baseline + noise + circadian rhythm
    hr = 60 + 5*np.sin(np.linspace(0, 3*np.pi, 480)) + np.random.normal(0, 1, 480)


    # Simulate sleep stages (0=Awake, 1=N1, 2=N2, 3=N3, 4=REM)
    sleep_stages = np.random.choice([0,1,2,3,4], size=480, p=[0.1,0.15,0.4,0.25,0.1])
    

    df = pd.DataFrame({'Time': time, 'HeartRate': hr, 'SleepStage': sleep_stages})
    df.set_index('Time', inplace=True)
    
    return df


# VISUALIZATION
def visualize(df: pd.DataFrame) -> None:
    """Visualize sleep and heart signals"""
    
    fig, ax = plt.subplots(2, 1, figsize=(12, 6), sharex=True)

    # Heart rate
    ax[0].plot(df.index, df['HeartRate'], color='red', label='Heart Rate (bpm)')
    ax[0].set_ylabel('Heart Rate')
    ax[0].legend()
    ax[0].grid(True)

    # Sleep stage (inverted y-axis for intuitive stage depth)
    ax[1].step(df.index, df['SleepStage'], where='post', color='blue', label='Sleep Stage')
    ax[1].invert_yaxis()
    ax[1].set_yticks([0,1,2,3,4])
    ax[1].set_yticklabels(['Awake', 'N1', 'N2', 'N3', 'REM'])
    ax[1].set_ylabel('Sleep Stage')
    ax[1].legend()
    ax[1].grid(True)

    plt.xlabel('Time')
    plt.tight_layout()
    fig.savefig("Simulation of Sleep stages and Heart rates.")
    plt.show()


if __name__ == "__main__":
    df = setup()
    visualize(df)