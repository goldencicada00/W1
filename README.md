# W1
# 執行
1. 執行產生 WAV 檔案 : `python audio_filter.py`
2. 用 Spectrum 比較 : `python verify_audio.py`
3. 針對 IIR Filter 分析 : `python verify_iir.py`

----------------------------------------------------------------------------------------------------------------------------------------
# create
### open file
1. `cd /d "C:\Users\Amy.Cheng\Desktop\W1-W4\W1\作業"`
### install
1. `python -m pip install numpy scipy`
### run
1. `audio_filter.py`
2. output
   ```
   Sample rate: 16000 Hz
   Audio shape: (509353,)
   Data type: int16
   
   Processing STFT method...
   
   ===== STFT Mask Verification =====
   Frequency resolution: 7.8125 Hz
   Number of frequency bins removed: 13
   Highest removed frequency: 93.75 Hz
   First preserved frequency: 101.5625 Hz
   Maximum magnitude below 100 Hz BEFORE masking: 0.12714940443508835
   Maximum magnitude below 100 Hz AFTER masking: 0.0
   All STFT bins below 100 Hz are zero: True
   
   Processing IIR HPF method...
   
   Done!
   Output:
   enroll_STFT_HPF.wav
   enroll_IIR_HPF.wav
   ```
### check : use specturm
1. 做一個:`verify_audio.py`
   * 它專門比較：
     * Original
     * STFT processed
     * IIR processed
     
     三個音訊的頻率
2. 安裝 matplotlib
   `python -m pip install matplotlib`
3. run
   `python verify_audio.py`
### 畫 IIR Filter 本身
1. 可以直接回答：「我的 Butterworth filter 真的是 100 Hz HPF 嗎？」
2. 建立:`verify_iir.py`
3. 執行:`python verify_iir.py`
   
----------------------------------------------------------------------------------------------------------------------------------------
# result
1. 用 Spectrum 比較
![image]()
2. 針對 IIR Filter 分析
![image]()
