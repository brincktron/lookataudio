import scipy.io.wavfile
import numpy as np
import matplotlib.pyplot as plt
import wave
import sys
path="p50 male speech 44.1kHz stereo.wav";
[fs,wavdata]=scipy.io.wavfile.read(path);
spf = wave.open(path,'r')

#Extract Raw Audio from Wav File
signal = spf.readframes(-1)
signal = np.fromstring(signal, 'Int16')
plt.figure(1)
plt.title('Signal Wave...')
plt.plot(signal)
plt.show()
print(test)