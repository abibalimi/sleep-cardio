#/usr/bin/env python3
import mne
import matplotlib.pyplot as plt

# Paths to files
psg_path = "data/SC4001E0-PSG.edf"           # EEG/PSG file
hypnogram_path = "data/SC4001EC-Hypnogram.edf"  # Hypnogram annotations

# Load EEG data (raw signals)
raw = mne.io.read_raw_edf(psg_path, preload=True, verbose=False)

# Load sleep stage annotations
annotations = mne.read_annotations(hypnogram_path)

# Attach annotations to raw EEG
raw.set_annotations(annotations)

# Plot EEG + hypnogram
raw.plot(title="EEG with Sleep Stages", duration=600, scalings="auto")
plt.show()