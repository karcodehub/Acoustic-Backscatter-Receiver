import math
import struct
import numpy as np
import subprocess
from scipy.signal import butter, lfilter, freqz
import matplotlib.pyplot as plt

symrate = 6 #freq or symbol rate (for a duration [1 here] how many symbol are generated)
#cutoffrq = symrate
samplpersym = 100 #(how many samples to be considered for per symbol)
duration = 1 # within this time entire signal should be processed
samprate = symrate * samplpersym #      2 * 4

# generate Signal for input
#no_rept = int(duration * symrate / len(sym))
#signal = np.repeat(np.tile(sym, no_rept), samplpersym)
#time = 1/samprate * np.arange(int(samprate * duration)) #
#timeError=.002
symb = [-1,1,-1,1,1,-1]
digi = np.ndarray(600, dtype=float) # 600= 6 symbol and 100 samples per symbol 

for i in range(len(symb)):
    digi[i*100:100*(i+1)] = symb[i]


print(digi)
#print(x_axis)
plt.plot(np.ndarray(600, dtype=float), digi , marker="s")

plt.show()
