# Assignment 1

This program generates a 1 second, clipped 440 Hz, A note.

## Requirements

The libraries used in this program are `numpy` to generate the sin wave and perform math on the array. `scipy` to create a wavfile based on the numpy array and `sounddevice` to play that sound to the output device.

## Implementation

Following the assignment instructions, I generated a sin wave using the `make_wave` function that I wrote which had one required parameter `amplitude` and other optional parameter `frequency` (440hz default), `duration` (1sec default), `sample_rate` (48000 default).

Another louder wave is generated using `make_wave` function passing in `16384` based on the assignment instruction. This generates a much taller amplitude but it is then clipped using `np.clip` which is a function which clips all numbers at desired max and min.

Finally we generate a wavefile for the louder wave and play to output speaker using `sounddevice` function.

Clipping this wave produces a much more dirtier and distorted sound. This is probably how electric guitar distortion is created.
