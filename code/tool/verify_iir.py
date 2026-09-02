import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy import signal


# ============================================================
# Settings
# ============================================================

INPUT_FILE = "enroll.wav"

CUTOFF_HZ = 100
IIR_ORDER = 4

DISPLAY_MAX_HZ = 500


# ============================================================
# Read sample rate
# ============================================================

fs, _ = wavfile.read(
    INPUT_FILE
)

print("Sample rate:", fs, "Hz")


# ============================================================
# Design IIR High-Pass Filter
# ============================================================

sos = signal.butter(
    IIR_ORDER,
    CUTOFF_HZ,
    btype="highpass",
    fs=fs,
    output="sos"
)


# ============================================================
# Calculate Frequency Response
# ============================================================

f, h = signal.sosfreqz(
    sos,
    worN=8192,
    fs=fs
)

magnitude_db = 20 * np.log10(
    np.abs(h) + 1e-12
)


# ============================================================
# Plot
# ============================================================

plt.figure(
    figsize=(10, 6)
)

plt.plot(
    f,
    magnitude_db,
    label=f"{IIR_ORDER}th-order Butterworth HPF"
)

plt.axvline(
    CUTOFF_HZ,
    linestyle="--",
    label="100 Hz cutoff"
)

plt.axhline(
    -3,
    linestyle="--",
    label="-3 dB"
)

plt.xlim(
    0,
    DISPLAY_MAX_HZ
)

plt.ylim(
    -80,
    5
)

plt.xlabel(
    "Frequency (Hz)"
)

plt.ylabel(
    "Gain (dB)"
)

plt.title(
    "Frequency Response of 100 Hz IIR High-Pass Filter"
)

plt.grid()
plt.legend()

plt.tight_layout()
plt.show()
