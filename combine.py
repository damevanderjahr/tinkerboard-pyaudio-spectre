from color_transform import *
from get_matrix import *
import spidev

# original code and instructions:
# https://tinkerboarding.co.uk/wiki/index.php/Waveshare-Expansions
# https://tinkerboarding.co.uk/wiki/images/5/5d/TB_sample_code.7z


# transform byte to bits sequence
def byte2bits(byte):
    b0 = 0x1
    b1 = 0x7
    mask = 0x80
    while mask != 0:
        bits.append(b0 if ( byte & mask ) == 0 else b1)
        mask >>= 1
    return bits


# transform rgb colors to bits sequence
def SetLedColor(red, green, blue):
    byte2bits(green)
    byte2bits(red)
    byte2bits(blue)


spi = spidev.SpiDev()
spi.open(2, 0)
spi.max_speed_hz = 3200000
spi.mode = 0b01
spi.xfer2([0])

led_cnt = 64
k = 8
matrix = get_matrix()

try:
    bits = []
    while True:
        m = matrix.__next__()
        # transform color matrix to spi bits sequence
        for i in range(0, led_cnt):
            (r, g, b) = m[i // k][i % k]
            SetLedColor(r, g, b)
        # send bits sequence to spi interface pin
        spi.xfer(bits)
        bits = []
except KeyboardInterrupt:
    spi.xfer2([0x1 for i in range(1536)])
    spi.close()
    print("\n --- Done. ---")
