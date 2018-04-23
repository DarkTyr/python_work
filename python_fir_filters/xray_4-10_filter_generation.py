import pylab as pl
import numpy as np
from scipy import signal
pl.ion()

#Number of Taps 
N = 128

#ADC sampling frequency in MHz
fs = 250

#firwin window
window0 = 3.5
window1 = 4

#
plot_impulse_response = False
'''
First type of possible half band filter is a Parks-McClellan Remez.
'''
bands = np.array([0.00, 0.032, 0.04, 0.50])
h = signal.remez(N, bands, [1,0],[1,40])

w, H = signal.freqz(h)

'''
Second type of possible half band filter is a windows Freq.
'''
b0 = signal.firwin(N, 0.05,window=window0)
wb0, Hb0 = signal.freqz(b0)

b1 = signal.firwin(N, 0.05,window=window1)
wb1, Hb1 = signal.freqz(b1)

'''
Plot the Impulse reponse and frequency reponse
'''
window0 = 'kaiser-alpha='+str(window0)
window1 = 'kaiser-alpha='+str(window1)

if (plot_impulse_response):
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
ax2.plot(w/(2*np.pi)*fs, 20*np.log10(np.abs(Hb0)))
ax2.plot(w/(2*np.pi)*fs, 20*np.log10(np.abs(Hb1)))
ax2.legend(['Remez-'+str(N), window0+'-'+str(N),window1+'-'+str(N) ])
ax2.grid(1)
ax2.axis([0, 25, -66, 6])
#ax2.axvline(375)
#ax2.axvline(250)
#ax2.axvline(125)
ax2.axvline(125.0/16.0, color='r')
ax2.axvline(4, color='k')
ax2.axvline(10, color='m')
ax2.axvline(14, color='m')
ax2.axvline(18, color='m')
#ax2.axvline(125-4)
ax2.set_ylabel('Magnitude [dB]')
ax2.set_xlabel('Frequnecy [MHz]')
ax2.set_title('Halfband FIR Frequency Repsonses')
