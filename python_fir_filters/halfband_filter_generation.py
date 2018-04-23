import pylab as pl
import numpy as np
from scipy import signal
pl.ion()

#Filter order (N+1 for number of coefficents)
N = 30

#ADC sampling frequency in MHz
fs = 1000

'''
First type of possible half band filter is a Parks-McClellan Remez.
'''
bands = np.array([0.00, 0.22, 0.28, 0.50])
h = signal.remez(N+1, bands, [1,0],[1,1])

w, H = signal.freqz(h)

'''
Second type of possible half band filter is a windows Freq.
'''
b = signal.firwin(N+1, 0.5)
wb, Hb = signal.freqz(b)

'''
Plot the Impulse reponse and frequency reponse
'''

fig0 = pl.figure(0)
ax0 = fig0.add_subplot(211)
ax0.stem(np.arange(len(h)),h)
ax0.grid(1)
ax0.set_title('Remez Impulse Response')

ax1 = fig0.add_subplot(212)
ax1.stem(np.arange(len(b)),b)
ax1.grid(1)
ax1.set_title('Windowed firwin Impulse Response')

fig1 = pl.figure(1)
ax2 = fig1.add_subplot(111)
ax2.plot(w/(2*np.pi)*fs, 20*np.log10(np.abs(H)))
ax2.plot(w/(2*np.pi)*fs, 20*np.log10(np.abs(Hb)))
ax2.legend(['Remez', 'firwin'])
ax2.grid(1)
ax2.axis([0, 500, -66, 6])
ax2.axvline(250)
ax2.set_ylabel('Magnitude [dB]')
ax2.set_xlabel('Frequnecy [MHz]')
ax2.set_title('Halfband FIR Frequency Repsonses')
