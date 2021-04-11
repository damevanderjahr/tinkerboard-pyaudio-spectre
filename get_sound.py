import pyaudio
import numpy as np


# get <chunk> samples from stream
# stream is monitor of default output
# errors are from PyAudio.__init__
def get_level():
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    chunk = 2048

    pa = pyaudio.PyAudio()
    SPEAKERS = pa.get_default_output_device_info()["hostApi"]
    stream = pa.open(format=FORMAT,
                     channels=CHANNELS,
                     rate=RATE,
                     input=True,
                     frames_per_buffer=chunk,
                     input_host_api_specific_stream_info=SPEAKERS)
    while True:
        try:
            data = np.fromstring(stream.read(chunk), dtype=np.int16)
            yield data
        except KeyboardInterrupt:
            break
    stream.close()
    return
