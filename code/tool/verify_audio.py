import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy import signal


# ============================================================
# Settings
# ============================================================

ORIGINAL_FILE = "enroll.wav"
STFT_FILE = "enroll_STFT_HPF.wav"
IIR_FILE = "enroll_IIR_HPF.wav"

CUTOFF_HZ = 100

PSD_NPERSEG = 8192
PSD_NOVERLAP = 4096

DISPLAY_MAX_HZ = 500


# ============================================================
# Functions
# ============================================================

def read_audio(filename):

    fs, x = wavfile.read(filename)

    if x.ndim > 1:
        x = np.mean(x, axis=1)

    if np.issubdtype(x.dtype, np.integer):
        x = (
            x.astype(np.float64)
            / np.iinfo(x.dtype).max
        )
    else:
        x = x.astype(np.float64)

    return fs, x


def get_psd(x, fs):

    f, psd = signal.welch(
        x,
        fs=fs,
        window="hann",
        nperseg=PSD_NPERSEG,
        noverlap=PSD_NOVERLAP,
        scaling="density"
    )

    psd_db = 10 * np.log10(
        psd + 1e-20
    )

    return f, psd_db


# ============================================================
# Read WAV files
# ============================================================

fs_original, x_original = read_audio(
    ORIGINAL_FILE
)

fs_stft, x_stft = read_audio(
    STFT_FILE
)

fs_iir, x_iir = read_audio(
    IIR_FILE
)


if not (
    fs_original
    == fs_stft
    == fs_iir
):
    raise ValueError(
        "Sample rates are different."
    )


# ============================================================
# Calculate PSD
# ============================================================

f_original, psd_original = get_psd(
    x_original,
    fs_original
)

f_stft, psd_stft = get_psd(
    x_stft,
    fs_stft
)

f_iir, psd_iir = get_psd(
    x_iir,
    fs_iir
)


# ============================================================
# Plot
# ============================================================

plt.figure(
    figsize=(12, 6)
)

plt.plot(
    f_original,
    psd_original,
    label="Original",
    linestyle="--"
)

plt.plot(
    f_stft,
    psd_stft,
    label="STFT HPF"
)

plt.plot(
    f_iir,
    psd_iir,
    label="IIR HPF"
)

plt.axvline(
    CUTOFF_HZ,
    linestyle="--",
    label="100 Hz cutoff"
)

plt.xlim(
    0,
    DISPLAY_MAX_HZ
)

plt.xlabel(
    "Frequency (Hz)"
)

plt.ylabel(
    "Power Spectral Density (dB/Hz)"
)

plt.title(
    "Frequency Spectrum Comparison"
)

plt.grid()
plt.legend()

plt.tight_layout()
plt.show()
