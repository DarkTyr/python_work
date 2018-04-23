import pylab as pl
import numpy as np
from scipy import signal
pl.ion()

N=4096
file_list=['constrained_equiripple_4-10', 'equiripple_4-10', 'windows_blackman_4-10', 'windows_blackman_2-10', 'windows_taylor_4-10', 'tfilter_4-10']
file_list1=['windows_blackman_4-10', 'windows_hamming_2-10', 'windows_taylor_4-10', 'constrained_equiripple_2-10', 'equiripple_2-10']
file_list0=['windows_taylor_2-10']
fig = pl.figure(0)
ax1 = fig.add_subplot(111)

f = np.arange(N/2)*500.0/(N/2.0)

for index in xrange(len(file_list)):
	b = np.loadtxt('fir_' + file_list[index] + '.coe', delimiter=',')

	X = np.fft.fft(b, N)
	Xm = np.abs(X)
	#Xdb = 20.0*np.log10(Xm/Xm.max())
	xdb_offset = 20.0*np.log10(Xm[0])
	Xdb = 20.0*np.log10(Xm) + xdb_offset
	pl.plot(f, Xdb[:N/2], label=file_list[index])

pl.axvline( 2, color='k', linestyle='--')
pl.axvline( 4, color='k', linestyle='--')
pl.axvline(10, color='k', linestyle='--')
pl.axvline(14, color='k', linestyle='--')
pl.axvline(18, color='k', linestyle='--')
pl.axhline(-3, color='k', linestyle='--')
pl.axhline(3, color='k', linestyle='--')

pl.ylim(-80, 10)
pl.xlim(0, 50)

pl.title('X-Ray FIR filter responses')
pl.xlabel('Frequency [MHz]')
pl.ylabel('Response [dB]')
pl.legend()
