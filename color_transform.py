import math


# color transform from HSV to RGB scheme
def hsv_to_rgb(h, s, v):
    h_i = math.floor(h / 60.0) % 6
    v_min = (100 - s) * v // 100
    a = (v - v_min) * (h % 60) // 60
    v_inc = v_min + a
    v_dec = v - a
    if h_i == 0:
        r, g, b = v, v_inc, v_min
    elif h_i == 1:
        r, g, b = v_dec, v, v_min
    elif h_i == 2:
        r, g, b = v_min, v, v_inc
    elif h_i == 3:
        r, g, b = v_min, v_dec, v
    elif h_i == 4:
        r, g, b = v_inc, v_min, v
    elif h_i == 5:
        r, g, b = v, v_min, v_dec
    else:
        raise ValueError
    return r, g, b
