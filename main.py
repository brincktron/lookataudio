import numpy as np
import matplotlib.pyplot as plt
import math
import soundfile as sf
import sys

try:
    path=sys.argv[1]
except:
    path = "p50 male speech 44.1kHz stereo.wav"
    print "No file dragged - using test-wav-file"

sig, fs = sf.read(path)  # use the Soundfile package to read audio

def rms_flat(a):
    """
    Return the root mean square of all the elements of *a*, flattened out.
    from: http://stackoverflow.com/questions/9763471/audioop-rms-why-does-it-differ-from-normal-rms
    """
    # noinspection PyTypeChecker
    return np.sqrt(np.mean(np.absolute(a) ** 2))

rms_val = rms_flat(sig)
rms_val_db = 20 * math.log10(rms_val) # Amplitude rato, 20log10


print "RMS value: ", str(round(rms_val, 4)), "equals", round(rms_val_db,4), "dBFS";
print "Peak values", round(sig.max(),4), "and", round(sig.min(),4)

x = np.linspace(0, len(sig) / fs, num=len(sig))  # create an x-axis in seconds
plt.figure(1)
plt.title('Signal Wave...')
plt.plot(x,sig)
plt.show()
plt.legend("RMS: ", str(4))



