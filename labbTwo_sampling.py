#AUTHOR: Martin C. Bildhjerd

#LIBRARYS
import numpy as np
import scipy as sp
import scipy.signal
from scipy.stats import norm, expon
from scipy.fftpack import fft, rfft, irfft, fftfreq, rfftfreq
from scipy.integrate import quad
import matplotlib.pyplot as plt
###

##DEFS
f1 = 10 
f2 = 60 
fs = 200 
Ts = 1/fs

t = np.arange(0, 1+Ts, Ts)
t2 = np.arange(0, 1+2*Ts, Ts)

fs_one = 5
fs_two = 15
fs_three = 80
fs_four = 300

signal_one = np.sin(2 * np.pi * f1 * t)
signal_two = np.sin(2 * np.pi * f2 * t)
signal_final = signal_one + signal_two

frequency_domain_signal = np.fft.fft(signal_final)
freq1 = np.fft.fftfreq(len(frequency_domain_signal), Ts)
###

##PLOTTER FUNCTION
def plot_twister(fs):
    Ts = 1/fs
    t2 = np.arange(0, 1+2*Ts, Ts)
    signal_to_sample = np.sin(2 * np.pi * f1 * t2) + np.sin(2 * np.pi * f2 * t2)
    frequency_domain_signal = np.fft.fft(signal_to_sample)
    freq1 = np.fft.fftfreq(len(frequency_domain_signal), Ts)
    plt.figure()
    plt.plot(freq1, np.abs(frequency_domain_signal))
    plt.title(f'2- tone at {fs} Hz')
    plt.xlabel('TIME [s])')
    plt.ylabel('AMP')
    plt.grid(True)
    plt.show()
### 

#MAIN:
plot_twister(fs_one) # = 5Hz
plot_twister(fs_two) # = 15Hz
plot_twister(fs_three) # = 80Hz
plot_twister(fs_four) # = 300zHz
###