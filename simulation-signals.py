#/usr/bin/env python3

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# SETUP

# Simulate time (1-minute resolution for 8 hours)
time = pd.date_range(start='2025-07-10 22:00', periods=480, freq='T')  # 8 hours
print(f'{time = }')
      
# Simulate heart rate (bpm): baseline + noise + circadian rhythm
hr = 60 + 5*np.sin(np.linspace(0, 3*np.pi, 480)) + np.random.normal(0, 1, 480)
print(f'{hr = }')

# Simulate sleep stages (0=Awake, 1=N1, 2=N2, 3=N3, 4=REM)
sleep_stages = np.random.choice([0,1,2,3,4], size=480, p=[0.1,0.15,0.4,0.25,0.1])
print(f'{sleep_stages = }')

df = pd.DataFrame({'Time': time, 'HeartRate': hr, 'SleepStage': sleep_stages})
df.set_index('Time', inplace=True)
