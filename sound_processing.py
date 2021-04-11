from get_sound import *
import numpy as np


fr = 44100
# coefficients of logistic function
p = 6
k = 15
r = 1
x = 6
# magic coefficient of normalization
magic = 6.5


def get_spectre():
    s_y = get_level()
    while True:
        a = s_y.__next__()
        # get fft of sound samples
        a = a * np.hamming(len(a))
        f = np.abs(np.fft.fft(a))
        freq = np.fft.fftfreq(len(a), 1.0/44100)
        vals = np.zeros(shape=8)
        f = f[: int(len(f)/2)]
        freq = freq[: int(len(freq)/2)]
        mark = 32
        # get root mean square of fft by intervals [0..32] (32..64] .. (4096..22050]
        for i in range(0, 8):
            tmp = f[np.where((mark > freq) & (freq >= mark / 2.0))] ** 2
            l = max(1, len(tmp))
            vals[i] += (np.sum(tmp) / l) ** 0.5
            if i == 0:
                tmp = f[np.where(freq <= mark/2.0)] ** 2
                l = max(1, len(tmp))
                vals[i] += (np.sum(tmp) / l) ** 0.5
            elif i == 7:
                tmp = f[np.where(freq > mark)] ** 2
                l = max(1, len(tmp))
                vals[i] += (np.sum(tmp) / l) ** 0.5
            mark *= 2

        # get log10 of RMS of intervals
        v1 = np.log10(vals + 1)

        # get normalized output for independence from input volume level
        v_max = np.max(v1)
        v1 = v1 / (v_max + 0.0001) * magic

        # logistic transform for large dynamic range
        v2 = np.exp(r * (v1 - x))
        v3 = k * p * v2 / (k + p * (v2 - 1))
        yield v3
