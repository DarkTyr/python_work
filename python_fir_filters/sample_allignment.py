import pylab as pl
import numpy as np
pl.ion()

pl.figure()

time = pl.linspace(0, 99, 100)
x_combined0 = pl.linspace(0, 399, 400)

x0 = np.cos(time/(2*np.pi)+0.0)
x1 = np.cos(time/(2*np.pi)+0.0)
x2 = np.cos(time/(2*np.pi)+0.0)
x3 = np.cos(time/(2*np.pi)+0.0)



q = 0
for i in xrange(0, 400, 4):
	x_combined0[i+0] = x0[q]
	x_combined0[i+1] = x1[q]
	x_combined0[i+2] = x2[q]
	x_combined0[i+3] = x3[q]
	q += 1

pl.plot(x_combined0)	

x_combined1 = pl.linspace(0, 399, 400)
x0 = np.cos(time/(2*np.pi)-0.00)
x1 = np.cos(time/(2*np.pi)-0.035)
x2 = np.cos(time/(2*np.pi)-0.07)
x3 = np.cos(time/(2*np.pi)-0.105)

q = 0
for i in xrange(0, 400, 4):
	x_combined1[i+0] = x3[q]
	x_combined1[i+1] = x2[q]
	x_combined1[i+2] = x1[q]
	x_combined1[i+3] = x0[q]
	q += 1

pl.plot(x_combined1)

