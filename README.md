# W1
### open file
1. `cd /d "C:\Users\Amy.Cheng\Desktop\W1-W4\W1\作業"`
### install
1. `python -m pip install numpy scipy`
### run
1. `audio_filter.py`
2. output
   ```
   C:\Users\Amy.Cheng\Desktop\W1-W4\W1\作業>python audio_filter.py
      Sample rate: 16000 Hz
      Audio shape: (509353,)
      Data type: int16
      
      Processing STFT method...
      Processing IIR HPF method...
      
      Done!
      Output:
      enroll_STFT_HPF.wav
      enroll_IIR_HPF.wav
   ```
### check:use specturm
1. 做一個:`verify_audio.py`
   * 它專門比較：
     *　Original
     *　STFT processed
     *　IIR processed
     
     三個音訊的頻率


