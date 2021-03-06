import pylab as pl
import numpy as np

pl.ion()

#Signal to do math on
f_res_mult = 2.005
nFrames = 256
L = 256*nFrames
t = np.linspace(0, L-1, L)
x = (np.cos(2*np.pi*t*f_res_mult/L*nFrames)+ 1j*np.sin(2*np.pi*t*f_res_mult/L*nFrames))
plot_bin = 2

#Flags
plot_response = True
plot_log_power_response = True

#Number of Taps 
N = 256
#number of steps
steps = L/N
#ADC sampling frequency in Hz
fs = 200e6

#Output array
X = np.zeros((N,steps), dtype=complex)
# variable to store constants


#Run the DFT algorithum
for k in xrange(steps):
	for n in xrange(N):
		for m in xrange(N):
			X[n][k] += (x[m+N*k] * (np.cos(2*np.pi*n*m/N) - 1j*np.sin(2*np.pi*n*m/N)))

#Scale by something		
X = X/(N)

index=4
if(plot_response):
	fig0 = pl.figure(0)
	ax0 = fig0.add_subplot(311)
	ax0.plot(t, np.real(x))
	ax0.plot(t, np.imag(x))
	ax0.set_title("Input Signal")
	ax0.grid(True)
	ax1 = fig0.add_subplot(312)
	ax1.plot(np.real(X[:,index]))
	ax1.plot(np.imag(X[:,index]))
	ax1.set_title("Output")
	ax1.grid(True)
	ax2 = fig0.add_subplot(313)
	ax2.plot(np.abs(X[:,index]))
	ax2.set_title("Magnitude or power of the output")
	ax2.grid(True)

if(plot_log_power_response):
	fig1 = pl.figure(1)
	ax3 = fig1.add_subplot(111)
	ax3.plot(20*np.log10(np.abs(X[:,index])))
	ax3.set_title("Power of Input in log form")


if(plot_bin!=0):
	fig2 = pl.figure(2)
	ax4 = fig2.add_subplot(111)
	ax4.plot(np.real(X[plot_bin,:]))
	ax4.plot(np.imag(X[plot_bin,:]))
	ax4.set_title("Time sequency of Bin : " + str(plot_bin))

