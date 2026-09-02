import numpy as np
import matplotlib.pyplot as plt
from scipy import signal


fs = 16000
cutoff = 100
order = 4


# =====================================
# Design IIR High-Pass Filter
# =====================================

sos = signal.butter(
    order,
    cutoff,
    btype="highpass",
    fs=fs,
    output="sos"
)


# =====================================
# Frequency response
# =====================================

f, h = signal.sosfreqz(
    sos,
    worN=8192,
    fs=fs
)


magnitude_db = 20 * np.log10(
    np.abs(h) + 1e-12
)


# =====================================
# Plot
# =====================================

plt.figure(figsize=(10, 6))

plt.plot(
    f,
    magnitude_db,
    label="4th-order Butterworth HPF"
)

plt.axvline(
    100,
    linestyle="--",
    label="100 Hz cutoff"
)

plt.axhline(
    -3,
    linestyle="--",
    label="-3 dB"
)

plt.xlim(0, 500)

plt.ylim(-80, 5)

plt.xlabel("Frequency (Hz)")
plt.ylabel("Gain (dB)")

plt.title(
    "Frequency Response of 100 Hz IIR High-Pass Filter"
)

plt.grid()
plt.legend()

plt.tight_layout()
plt.show()
