#AUTHOR: Martin C. Bildhjerd

#LIBRARYS
import numpy as np
import scipy as sp
import scipy.signal
from scipy.signal import hilbert, chirp
from scipy.stats import norm, expon
from scipy.fftpack import fft, rfft, irfft, fftfreq, rfftfreq
from scipy.integrate import quad
import matplotlib.pyplot as plt
###

#DEFS
f0 = 5000
T0 = 1/f0
f1 = f0 - 10
f2 = f0 + 10
###

t = np.linspace(0, 1, 50000) #instead of 0
lowpass_variable = -2j * np.pi * f0

signal_one = np.sin(2 * np.pi * f1 * t)
signal_two = np.sin(2 * np.pi * f2 * t)

signal_res = signal_one + signal_two

analytical_signal = hilbert(signal_res)

lowpass_signal = analytical_signal * np.exp(lowpass_variable * t)

freq_domain_sig = np.fft.fft(signal_res)
freq_domain_analytical = np.fft.fft(analytical_signal)
freq_domain_LP = np.fft.fft(lowpass_signal)

freq1 = np.fft.fftfreq(len(freq_domain_sig))
freq2 = np.fft.fftfreq(len(freq_domain_analytical))
freq3 = np.fft.fftfreq(len(freq_domain_LP))

plt.figure(figsize=(12, 6))

#PLOT- TWISTER (X(f))
plt.subplot(3, 1, 1)
plt.plot(freq1, np.abs(freq_domain_sig))
plt.title('(X(f))')
plt.xlabel('Frequency [Hz]')
plt.ylabel('Magnitude')
plt.grid(True)
###

##PLOT- TWISTER (Z(f))
plt.subplot(3, 1, 2)
plt.plot(freq2, np.abs(freq_domain_analytical))
plt.title('(Z(f))')
plt.xlabel('Frequency [Hz]')
plt.ylabel('Magnitude')
plt.grid(True)
###

#PLOT- TWISTER (Xl(f))
plt.subplot(3, 1, 3)
plt.plot(freq3, np.abs(freq_domain_LP))
plt.title('(Xl(f))')
plt.xlabel('Frequency [Hz]')
plt.ylabel('Magnitude')
plt.grid(True)
###

plt.tight_layout()
plt.show()