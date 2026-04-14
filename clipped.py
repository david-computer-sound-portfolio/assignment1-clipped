import numpy as np
from scipy.io import wavfile
import sounddevice as sd


def make_wave(amplitude, frequency=440, duration=1, sample_rate=48000):
    total_samples = sample_rate*duration
    array = np.linspace(
        0.0, duration, total_samples
    )
    pure_wave = amplitude * np.sin(2 * np.pi * frequency * array)

    #convert to a 16bit format
    pure_wave_16bit = pure_wave.astype(np.int16)

    return pure_wave_16bit
    
sin_wave = make_wave(8192)
wavfile.write("sine.wav", sin_wave)

#make a bigger wave but we will clip us numpy
louder_wav = make_wave(16384)

#clip it at +-8192
clip_wave = np.clip(louder_wav,-8192,8192)
wavfile.write("clipped.wav", clip_wave)

print("Playing clipped wave")
sd.play(clip_wave)
sd.wait()
print("Finished Playing")