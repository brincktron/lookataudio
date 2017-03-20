import scipy.io.wavfile
import numpy as np
import matplotlib.pyplot as plt
path="p50 male speech 44.1kHz stereo.wav";
[fs,wavdata]=scipy.io.wavfile.read(path);
print('test')