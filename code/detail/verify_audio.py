import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy import signal


# =====================================
# 1. Read WAV file
# =====================================

def read_audio(filename):

    fs, x = wavfile.read(filename)

    # Convert stereo to mono if necessary
    if x.ndim > 1:
        x = np.mean(x, axis=1)

    # Convert integer WAV to floating point
    if np.issubdtype(x.dtype, np.integer):
        max_value = np.iinfo(x.dtype).max
        x = x.astype(np.float64) / max_value
    else:
        x = x.astype(np.float64)

    return fs, x


# =====================================
# 2. Read three audio files
# =====================================

fs_original, x_original = read_audio(
    "enroll.wav"
)

fs_stft, x_stft = read_audio(
    "enroll_STFT_HPF.wav"
)

fs_iir, x_iir = read_audio(
    "enroll_IIR_HPF.wav"
)


print("Original sample rate:", fs_original)
print("STFT sample rate:", fs_stft)
print("IIR sample rate:", fs_iir)


# =====================================
# 3. Check sample rates
# =====================================

if not (
    fs_original == fs_stft == fs_iir
):
    raise ValueError(
        "The sample rates of the three WAV files are different."
    )


# =====================================
# 4. Calculate Welch PSD
# =====================================

def get_psd(x, fs):

    f, psd = signal.welch(
        x,
        fs=fs,
        window="hann",
        nperseg=8192,
        noverlap=4096,
        scaling="density"
    )

    psd_db = 10 * np.log10(
        psd + 1e-20
    )

    return f, psd_db


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


# =====================================
# 5. Plot PSD comparison
# =====================================

plt.figure(figsize=(12, 6))


# STFT result
plt.plot(
    f_stft,
    psd_stft,
    label="STFT HPF",
    linewidth=1.5,
    alpha=0.8
)


# IIR result
plt.plot(
    f_iir,
    psd_iir,
    label="IIR HPF",
    linewidth=1.5,
    alpha=0.8
)


# Original is drawn last so it is not hidden
plt.plot(
    f_original,
    psd_original,
    label="Original",
    linewidth=1.2,
    linestyle="--",
    alpha=0.8
)


# 100 Hz cutoff
plt.axvline(
    x=100,
    linestyle="--",
    linewidth=1.5,
    label="100 Hz cutoff"
)


plt.xlim(0, 500)

plt.xlabel("Frequency (Hz)")
plt.ylabel("Power Spectral Density (dB/Hz)")

plt.title(
    "Frequency Spectrum Comparison"
)

plt.legend()
plt.grid()

plt.tight_layout()
plt.show()
