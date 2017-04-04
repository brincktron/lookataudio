import numpy as np
import matplotlib.pyplot as plt
import math
import soundfile as sf
import sys
import ntpath

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

rms_string="RMS value %s equals %s dBFS" % (str(round(rms_val,2)), round(rms_val_db,2))
print rms_string
print "Peak values", round(sig.max(),2), "and", round(sig.min(),2)

x = np.linspace(0, len(sig) / fs, num=len(sig))  # create an x-axis in seconds

chunk_size=fs/50 # 20 ms
trim_ms = 0
threshold = 0.0002
while rms_flat(sig[trim_ms:trim_ms+chunk_size]) < threshold:
    trim_ms += chunk_size

sig_rev=np.flipud(sig)
trim_ms_rev = 0
threshold = 0.0002
while rms_flat(sig_rev[trim_ms_rev:trim_ms_rev+chunk_size]) < threshold:
    trim_ms_rev += chunk_size
print trim_ms
print trim_ms_rev
print trim_ms_rev

sig_chunk=sig[trim_ms:len(sig)-trim_ms_rev]
rms_val_chunk_db=20 * math.log10(rms_flat(sig_chunk))

plt.figure(1)
plt.title(ntpath.basename(path))
plt.plot(x,sig)
plt.ylim([-1,1])
plt.xlim([0,x.max()])
plt.text(0.1,-0.9, "RMS = %s dBFS" % round(rms_val_db,2))
plt.text(0.1,-0.7, "Enveloped RMS= %s dBFS" % round(rms_val_chunk_db,2))
plt.plot((float(trim_ms)/fs,float(trim_ms)/fs), (1, -1), 'k-')
plt.plot((float(len(sig)-trim_ms_rev)/fs,float(len(sig)-trim_ms_rev)/fs), (1, -1), 'k-')
plt.show()