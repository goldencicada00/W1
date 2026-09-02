import numpy as np
from scipy.io import wavfile
from scipy import signal


# =========================
# 1. Read WAV file
# =========================

input_file = "enroll.wav"

fs, x = wavfile.read(input_file)

print("Sample rate:", fs, "Hz")
print("Audio shape:", x.shape)
print("Data type:", x.dtype)


# Convert audio to floating point
original_dtype = x.dtype

if np.issubdtype(original_dtype, np.integer):

    max_value = np.iinfo(original_dtype).max

    x_float = (
        x.astype(np.float64)
        / max_value
    )

else:

    x_float = x.astype(np.float64)


# =========================
# 2. STFT method
# =========================

print("\nProcessing STFT method...")


nperseg = 2048


# ---------------------------------
# STFT
# ---------------------------------

f, t, Zxx = signal.stft(
    x_float,
    fs=fs,
    nperseg=nperseg,
    axis=0
)


# Keep STFT before masking
Zxx_before = Zxx.copy()


# ---------------------------------
# Frequency mask
# ---------------------------------

mask = f < 100


# Remove frequencies below 100 Hz
Zxx[mask, ...] = 0


# =================================
# STFT Mask Verification
# =================================

print("\n===== STFT Mask Verification =====")


frequency_resolution = fs / nperseg

print(
    "Frequency resolution:",
    frequency_resolution,
    "Hz"
)


print(
    "Number of frequency bins removed:",
    np.sum(mask)
)


print(
    "Highest removed frequency:",
    f[mask][-1],
    "Hz"
)


print(
    "First preserved frequency:",
    f[~mask][0],
    "Hz"
)


max_before = np.max(
    np.abs(
        Zxx_before[mask, ...]
    )
)

print(
    "Maximum magnitude below 100 Hz BEFORE masking:",
    max_before
)


max_after = np.max(
    np.abs(
        Zxx[mask, ...]
    )
)

print(
    "Maximum magnitude below 100 Hz AFTER masking:",
    max_after
)


all_zero = np.all(
    Zxx[mask, ...] == 0
)

print(
    "All STFT bins below 100 Hz are zero:",
    all_zero
)


# Do not continue if masking failed
assert all_zero, "STFT masking failed!"


# ---------------------------------
# ISTFT
# ---------------------------------

_, y_stft = signal.istft(
    Zxx,
    fs=fs,
    nperseg=nperseg
)


# Keep the same length
y_stft = y_stft[
    :len(x_float)
]


# =========================
# 3. IIR HPF method
# =========================

print("\nProcessing IIR HPF method...")


cutoff = 100
order = 4


# Design a 4th-order Butterworth
# 100 Hz high-pass IIR filter
sos = signal.butter(
    order,
    cutoff,
    btype="highpass",
    fs=fs,
    output="sos"
)


# Filter in time domain
y_iir = signal.sosfilt(
    sos,
    x_float,
    axis=0
)


# =========================
# 4. Convert back to WAV
# =========================

def save_wav(filename, audio):

    # Prevent clipping
    audio = np.clip(
        audio,
        -1.0,
        1.0
    )

    # Convert back to original integer type
    if np.issubdtype(
        original_dtype,
        np.integer
    ):

        audio = audio * max_value

        audio = audio.astype(
            original_dtype
        )

    wavfile.write(
        filename,
        fs,
        audio
    )


# =========================
# 5. Save output WAV files
# =========================

save_wav(
    "enroll_STFT_HPF.wav",
    y_stft
)

save_wav(
    "enroll_IIR_HPF.wav",
    y_iir
)


print("\nDone!")

print("Output:")

print(
    "enroll_STFT_HPF.wav"
)

print(
    "enroll_IIR_HPF.wav"
)
