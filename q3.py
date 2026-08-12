import numpy as np
import matplotlib.pyplot as plt
import scipy 

#Load txt file
data = np.loadtxt('qiti-iqc-Yb-rabi-data.txt', delimiter='\t')

#Take average of columns
averages=np.mean(data, axis=0)
print("These are the average probabilities")
print(averages)


#plot stuff
steps=np.arange(0, 200, 2)
plt.plot(steps, averages, marker='o', label='average probabilities of 1')


def functionone(t, offset, amp, freq, phase):
    return offset+amp*np.sin(2*np.pi*freq*t + phase)

p0=[averages.mean(), (averages.max()-averages.min())/2, 1/(20), -np.pi/2]
popt, pcov = scipy.optimize.curve_fit(functionone, steps, averages, p0)
fit_freq=popt[2]
pulse = 0.5/fit_freq
print(f"The pi pulse length is {pulse} microseconds.")

#calculate errors
perr = np.sqrt(np.diag(pcov))
freq_error = perr[2]
pulse_error = (0.5/(fit_freq**2) )*freq_error
print(f"The error in pi pulse length is {pulse_error} microseconds.")


def entropy(prob):
    return -prob*np.log2(prob) - (1-prob)*np.log2(prob)

probabilities = entropy(averages)
plt.plot(steps, probabilities, marker='^', label='randomness of outcome')
print("These are the randomness of each outcome based on binary entropy")
print(probabilities)
plt.legend()
plt.show() 
