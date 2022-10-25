from locale import atof
import math
import struct
import numpy as np
import subprocess
from scipy.signal import butter, lfilter, freqz
import matplotlib.pyplot as plt
import random


def butter_lowpass(cutoff, fs, order=5):
    nyq = 0.5 * fs # Nyquist Frequency
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a

def butter_lowpass_filter(data, cutoff, fs, order=5):
    b, a = butter_lowpass(cutoff, fs, order=order)
    y = lfilter(b, a, data)
    return y

# Setting standard filter requirements.
order = 10 # sin wave can be approx represented as quadratic, symb rate
fs = 600.0     # total no. of samples 
cutoff = 6  # desired cutoff frequency of the filter, Hz ,      slightly higher than actual 1.2 Hz

b, a = butter_lowpass(cutoff, fs, order)


# generate Signal for input
T = 1.0       # value taken in seconds
n = int(T * fs) # indicates total samples
t = np.linspace(0, T, n, endpoint=False)
data = np.ndarray(10000, dtype=float) # 600= 6 symbol and 100 samples per symbol 
sampled_data = np.ndarray(400, dtype=float)
symb = np.ndarray(100, dtype=float)
#symb = np.random.randint(2, size=100)

for i in range(0,100):
    symb[i] = random.choice([-1,1])

for i in range(len(symb)):
    data[i*100:100*(i+1)] = symb[i]

#print(symb) 
#print(type(symb))

# Filtering and plotting
y = butter_lowpass_filter(data, cutoff, fs, order)

sampled_data = y[1::25]
#print(sampled_data)
print(type(y))
print(len(y))
proc = subprocess.Popen([
    "C:\\Users\Karthik Lokesh\\Desktop\\Proj_Arb\\generate\\wrp\\time_error.exe", "%f" % (len(sampled_data))],
    stdout=subprocess.PIPE, stdin=subprocess.PIPE)

# Generate Input
bytes = b""
for sample in sampled_data:
    bytes += b"%f\n" % (np.real(sample)) # each sample of symbol type converting it to float and sending it in bytes (instead of string)

stdout, stderr = proc.communicate(bytes) # wrtings argument to std in to C prog, then wait till excu of process, ret to py.
print(stdout)
print(len(stdout))
print(type(stdout))
output=(stdout.decode("utf-8")) # convert Python bytes object to String

print(type(output))
print(len(output))
output_fl=(output.split())
plot_fl = []

plot_fl = [float(x) for x in output_fl]
print(plot_fl)
#print([float(x) for x in output_fl])

#float_op= atof(output)
#print(float(output[-1]))
#for i in symb:
    #print(float_op[i])

#er = stdout.split(b"\t")
   
#error= float(er[-1])
    
#print((er[-1]))
#err=struct.unpack('b',b'5.0817e-0080.6709371.01240.9985311.000520.20916')
#print(err)
#print(error)
y_axis = plot_fl
x_axis =  np.arange(int(100)) #
    #mul_error[num]=output[-1]

#print(y_axis)
#print(x_axis)
plt.plot(x_axis, y_axis , marker="s")
plt.show()
