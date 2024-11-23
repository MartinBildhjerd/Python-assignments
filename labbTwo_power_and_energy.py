#AUTHOR: Martin C. Bildhjerd

#LIBRARYS
import numpy as np
import scipy as sp
import scipy.signal
#import sympy as sp
from scipy.stats import norm, expon
from scipy.fftpack import fft, rfft, irfft, fftfreq, rfftfreq
from scipy.integrate import quad
import matplotlib.pyplot as plt
###

##GENERIC DEFS:
f = 4000
T = 1/f
t = np.linspace(0, 10*T, 1000) ##AS DESCRIBED IN EXAMPLE
sig = np.sin(2*np.pi*f*t)
z = 1/(2*T) #USED TO COMPUTE POWER
###

##BOUNDRARY DEFS:
a = -np.inf
b = np.inf
c = -T/2
d = T/2
###

##ENERGY/POWER SEQUENCE LOADER:
def sequence(t):
    return np.sin(2*np.pi*f*t)
###

##ENERGY CALC //FORMULA:
def energyCalc(signal):
    signal = np.sin(2*np.pi*f*t)
    energy_result = np.sum(signal**2)
    return energy_result
###

##POWER CALC //FORMULA:
def powerCalc(function, c, d):
    def integral_calc(x):
        return (abs(function(x))**2) ##-------------------> 1/(2T)*INTEGRAL(|x|^2)
    power_result_first, _ = quad(integral_calc, c, d)
    power_result = (z*power_result_first) / np.inf
    return power_result
###

autocorr = np.correlate(sig, sig, mode = "full")
lag = np.arange(-len(sig)+1, len(sig))

freq = np.fft.fftfreq(len(sig), d=1/f)
spectrum = np.fft.fft(sig)

plt.figure(figsize = (12, 6))


##MAIN:

##AUTOCORRELATION FUNCTION
plt.plot(lag, autocorr)
plt.title("Autocorrelation Function")
plt.xlabel("+/-LAG")
plt.ylabel("AUTOCORRELATION")
plt.grid(True)
plt.show()
###

##POWER/ENERGY 
plt.plot(freq, np.abs(spectrum)**2/1000)
plt.title("ENERGY/POWER")
plt.xlabel("FREQ")
plt.ylabel("MAG")
plt.grid(True)
plt.show()
###


##ENERGY & POWER PRINTER
E = energyCalc(sequence)
P = powerCalc(sequence, c, d)

print(f"ENERGY: {E}") #IN THIS CASE TOTAL ENERGY
print(f"POWER, {P}") #IN THIS CASE AVERAGE POWER 
###
