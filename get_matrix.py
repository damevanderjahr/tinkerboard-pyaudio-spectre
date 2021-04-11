from color_transform import *
from sound_processing import *


import numpy as np

mat = np.zeros(shape=(8,8),dtype=np.dtype("i,i,i"))

led_cnt = 64
m = 8
n = 8


# fill output 8x8 (r,g,b) matrix
def get_matrix():
    spectre = get_spectre()
    # set hue for 0..7 line
    h = [(1 + 45 * i) % 360 for i in range(8)]
    while True:
        s = spectre.__next__()
        for i in range(0, led_cnt):
            # compute saturation and value for hsv color model
            s_l = s[7 - i % m] * 20 if s[7 - i % m] > (i // m) else 0
            s_l = s_l if s_l < 100 else 100
            v = np.exp((s_l - 20) / 50)
            # transform hsv to rgb model
            r, g, b = hsv_to_rgb(h[i // m], s_l, v)
            try:
                mat[i//m][i % m] = (r, g, b)
            except OverflowError:
                print(s[7 - i % m])
                print(h, s_l, v)
                print((r, g, b))
                continue
        yield mat
