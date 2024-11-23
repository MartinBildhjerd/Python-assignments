#LIBRARYS
import numpy as np
import scipy as sp
import scipy.signal
from scipy.stats import norm, expon
from scipy.fftpack import fft, rfft, irfft, fftfreq, rfftfreq
import matplotlib.pyplot as plt
###

##########################################TASK ONE########################################
#Name, age, height[cm], weight[kg]
tribute_one = ("Martin", 24, 178, 74)
tribute_two = ("Hulk", 54,  305, 635)

concatination = tribute_one + tribute_two
print(concatination)

name_extraction = (concatination[0], concatination[4])
print(name_extraction)
##########################################################################################

##########################################TASK TWO########################################
#strings, float, char, integer
set_one = {'w', "Ah you think darkess is your ally?", "Autobots roll out"}
set_two = {"Decepticons entered the game", 100, "This is how i win"}

set_one.add(11)
set_two.add(5.55)

fusion_card = set_one.union(set_two)
print(fusion_card)
##########################################################################################

########################################TASK THREE########################################
#If you cant explain % dont use it.

for number_police in range(51):  # 0, 1, 2, 3, ..., 50
    if number_police < 2: #ty 0, 1. That aint the flavor...
        prime_number_detector = False
    else:
        prime_number_detector = True
        for i in range(2, number_police // 2 + 1):
            if number_police % i == 0: #(%): CHECKS FOR EVEN DIV
                prime_number_detector = False
                break
    if prime_number_detector: 
        print(number_police)

##########################################################################################

#########################################TASK FOUR########################################
#2x2 matrix multiplication. LAMBADA

x = np.array([
    [1, 2],
    [3, 4]
])

d = np.array([
    [4, 3],
    [2, 1]
])

x_transposererad = x.T
d_transposererad = d.T

red_or_blue_pill = np.multiply(x, d)

print(red_or_blue_pill)

##########################################################################################

#########################################TASK FIVE########################################
x = np.linspace(0, 720, 720)
d = np.deg2rad(x) #CONV TO RADS

plot = 0.4*np.cos(2*np.pi*2*d) + 0.3*np.cos(2*np.pi*0.8*d) + 0.2*np.cos(2*np.pi*0.2*d) 

plt.plot(d, plot)
plt.title('THREE FREQ TOGETHER AS ONE <3')
plt.show()

d = np.linspace(-4, 4, 420) #AS DESCRIBED IN TASK
sinc_function = np.sinc(d) #AS DESCRIBED IN TASK

plt.plot(d, sinc_function)
plt.title('SINC')
plt.show()

sinc_function_shifted = np.sinc(d - 0.5) #PAPAS LITTLE CHEAT CODE FOR OFFSET ///// [-] ->, [+] <- /////

plt.plot(d, sinc_function_shifted)
plt.title('SINC WITH OFFSET (0.5)')
plt.show()
##########################################################################################

##########################################TASK SIX########################################

t = np.linspace(0, 1, int(1000), endpoint=False)
complex_signal = np.exp(1j * 2 * np.pi *1000* t) + np.exp(1j * 2 * np.pi *10* t) #AS DESCRIBED IN TASK

plt.figure(figsize=(14, 6)) #AS DESCRIBED IN TASK
plt.plot(t, np.abs(complex_signal)) #AS DESCRIBED IN TASK
plt.title("COMPLEX PLOT")
plt.xlabel('Real Part') #AS DESCRIBED IN TASK
plt.ylabel('Imaginary Part') #AS DESCRIBED IN TASK
plt.grid(True)
plt.ylim(-1, 1) 
plt.show()
##########################################################################################

########################################TASK SEVEN########################################

x = np.linspace(0, 10, 1000)
pdf_exponential = expon.pdf(x, scale=1) #AS DESCRIBED IN TASK
mean_exponential = expon.mean(scale=1) #AS DESCRIBED IN TASK
var_exponential = expon.var(scale=1) #AS DESCRIBED IN TASK

plt.figure(figsize=(12, 6)) #AS DESCRIBED IN TASK
plt.plot(x, pdf_exponential, label='PDF EXPO')
plt.title('EXPONENTIAL PLOT')
plt.xlabel('x') #AS DESCRIBED IN TASK
plt.ylabel('Density') #AS DESCRIBED IN TASK
plt.grid(True) #AS DESCRIBED IN TASK
plt.legend() #AS DESCRIBED IN TASK
plt.text(6, 0.35, f'Mean: {mean_exponential:.2f}\nVariance: {var_exponential:.2f}') #AS DESCRIBED IN TASK

plt.tight_layout()
plt.show()
##########################################################################################
