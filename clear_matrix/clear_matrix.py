import spidev
spi = spidev.SpiDev()
spi.open(2, 0)
spi.max_speed_hz = 3200000
spi.mode = 0b01
spi.xfer2([0x1 for i in range(1536)])
spi.close()
