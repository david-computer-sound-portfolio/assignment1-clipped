import numpy as np
from scipy.io import wavfile


SAMPLE_RATE = 48000
DURATION = 1
TOTAL_SAMPLES = SAMPLE_RATE * DURATION
FREQUENCY = 440
AMPLITUDE = 8193


array = np.linspace(
    0.0, DURATION, SAMPLE_RATE
)

pure_wave = 8192 * np.sin(2 * np.pi * FREQUENCY * array)
pure_wave_16bit = pure_wave.astype(np.int16)
print(pure_wave_16bit)

def make_wave(frequency, duration, amplitude, sample_rate=48000):
    total_samples = sample_rate*duration
    array = np.linspace(
        0.0, duration, total_samples
    )
    pure_wave = amplitude * np.sin(2 * np.pi * frequency * array)

    #convert to a 16bit format
    pure_wave_16bit = pure_wave.astype(np.int16)

    return pure_wave_16bit
    
sin_wave = make_wave(440,1,8192)

wavfile.write("sine.wav", SAMPLE_RATE, sin_wave)