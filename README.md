# Tinker Board pyaudio-spectre

<img src="https://github.com/damevanderjahr/tinkerboard-pyaudio-spectre/blob/master/img/IMG_20200911_215053.jpg?raw=true" width="400">

The project was created to visualize sound played by some program on Linux.

The current configuration works successfully on Asus Tinker Board. I find it is easy to modify code for other single-board computer (SBC), e.g. Raspberry Pi, that supports SPI (Serial Peripheral Interface) and PortAudio API.

The current configuration utilizes [Waveshare RGB LED HAT (B)](https://www.waveshare.com/product/raspberry-pi/hats/led-buttons/rgb-led-hat-b.htm). The code is written to control 64 WS2812B light-emitting diodes (LED). It can be easily modified for another number of the same LEDs.

The root folder of the project contains the main code. Other folders contain useful scripts and configuration files to automatically start visualization on system boot.

## pulseaudio as service
Very useful instructions: https://raven4.cz/wp/pulseaudio-in-system-wide-mode/
