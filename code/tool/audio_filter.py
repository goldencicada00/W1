import numpy as np
from scipy.io import wavfile
from scipy import signal


# ============================================================
# Settings
# ============================================================

INPUT_FILE = "enroll.wav"

STFT_OUTPUT = "enroll_STFT_HPF.wav"
IIR_OUTPUT = "enroll_IIR_HPF.wav"

CUTOFF_HZ = 100
STFT_NPERSEG = 2048
IIR_ORDER = 4


# ============================================================
# Read WAV
# ============================================================

fs, x = wavfile.read(INPUT_FILE)

print("Input file:", INPUT_FILE)
print("Sample rate:", fs, "Hz")
print("Audio shape:", x.shape)
print("Data type:", x.dtype)


# Convert WAV data to floating point
original_dtype = x.dtype

if np.issubdtype(original_dtype, np.integer):
    max_value = np.iinfo(original_dtype).max
    x_float = x.astype(np.float64) / max_value
else:
    x_float = x.astype(np.float64)


# ============================================================
# Method 1: STFT High-Pass Filtering
# ============================================================

print("\nProcessing STFT method...")

f, t, Zxx = signal.stft(
    x_float,
    fs=fs,
    nperseg=STFT_NPERSEG
)

# Keep original STFT for verification
Zxx_before = Zxx.copy()

# Frequency mask
mask = f < CUTOFF_HZ

# Remove all STFT bins below 100 Hz
Zxx[mask, :] = 0


# ----- Verify STFT mask -----

frequency_resolution = fs / STFT_NPERSEG

max_before = np.max(
    np.abs(Zxx_before[mask, :])
)

max_after = np.max(
    np.abs(Zxx[mask, :])
)

all_zero = np.all(
    Zxx[mask, :] == 0
)

print("\nSTFT verification")
print("-----------------")
print("Frequency resolution:", frequency_resolution, "Hz")
print("Highest removed frequency:", f[mask][-1], "Hz")
print("First preserved frequency:", f[~mask][0], "Hz")
print("Maximum magnitude before masking:", max_before)
print("Maximum magnitude after masking:", max_after)
print("All bins below 100 Hz are zero:", all_zero)

assert all_zero, "STFT masking failed!"


# ISTFT
_, y_stft = signal.istft(
    Zxx,
    fs=fs,
    nperseg=STFT_NPERSEG
)

# Keep same length as original
y_stft = y_stft[:len(x_float)]


# ============================================================
# Method 2: IIR High-Pass Filtering
# ============================================================

print("\nProcessing IIR method...")

sos = signal.butter(
    IIR_ORDER,
    CUTOFF_HZ,
    btype="highpass",
    fs=fs,
    output="sos"
)

y_iir = signal.sosfilt(
    sos,
    x_float
)


# ============================================================
# Save WAV
# ============================================================

def save_wav(filename, audio):

    audio = np.clip(
        audio,
        -1.0,
        1.0
    )

    if np.issubdtype(original_dtype, np.integer):
        audio = (
            audio * max_value
        ).astype(original_dtype)

    wavfile.write(
        filename,
        fs,
        audio
    )


save_wav(
    STFT_OUTPUT,
    y_stft
)

save_wav(
    IIR_OUTPUT,
    y_iir
)


print("\nDone!")
print("Output:")
print(STFT_OUTPUT)
print(IIR_OUTPUT)
