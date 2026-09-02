# 理解目前對 16000 Hz WAV 做了什麼

1. WAV 的 Sample rate = 16000 Hz

    依 [Nyquist theorem](https://github.com/goldencicada00/W1/blob/main/learn/Nyquist_Shannon_sampling_theorem.md)，可以表示的最高頻率是：
  
    $$ f_{\text{max}} = \frac{f_s}{2} = \frac{16000}{2} = 8000 Hz $$
   
    所以原始音訊頻率範圍大約是：
    ```
    0 Hz ─────────────────────────────────── 8000 Hz
    ```
    而要求是：
    ```
    0 ── 100 Hz │ 100 Hz ───────────── 8000 Hz
       壓掉     │          保留
    ```
2. 
