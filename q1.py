import numpy as np
import matplotlib.pyplot as plt
import scipy 

#Load txt file
data = np.loadtxt('qiti-iqc-Yb-rabi-data.txt', delimiter='\t')
print(data.shape)

#Take average of columns
averages=np.mean(data, axis=0)
print(averages)
print(averages.shape)

#plot stuff
steps=np.arange(0, 200, 2)
print(steps)
plt.plot(steps, averages, marker='o', label='test')


def functionone(t, offset, amp, freq, phase):
    return offset+amp*np.sin(2*np.pi*freq*t + phase)

p0=[averages.mean(), (averages.max()-averages.min())/2, 1/(20), -np.pi/2]
popt, pcov = scipy.optimize.curve_fit(functionone, steps, averages, p0)
print(popt)
fit=popt[2]
pulse = 0.5/fit
print(f"The pi pulse length is {pulse} microseconds.")
plt.legend()
plt.show() 

