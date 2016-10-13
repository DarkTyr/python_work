import numpy as np
import pylab as pl
from scipy import signal
import roach2_data as r2
import pyqtgraph as pg

pl.ion()
pg.setConfigOption('leftButtonPan', False)
'''File locations for at work'''
#file0 = '/home/pcuser/Documents/firmware/pfb_rev0_2/asc_poster2/1472228209_DM5_raw_res'
#file1 = '/home/pcuser/Documents/firmware/pfb_rev0_2/asc_poster2/1472228260_DM2_bin_472'
#file2 = '/home/pcuser/Documents/firmware/pfb_rev0_2/asc_poster2/1472231012_DM4_bin_472_mix_on'
'''File locations for at home'''
file0 = '/home/darktyr/Documents/asc_poster2/1472228209_DM5_raw_res'
file1 = '/home/darktyr/Documents/asc_poster2/1472228260_DM2_bin_472'
file2 = '/home/darktyr/Documents/asc_poster2/1472231012_DM4_bin_472_mix_on'

'''Read in data using the Roach2_data class'''
raw_ac_res = r2.R2Data(fname=file0, fs=256e6, fr=62.5e3)
pfb_bin = r2.R2Data(fname=file1, fs=2e6, fr=10.0e3)
ddc_mix_on = r2.R2Data(fname=file2, fs=2e6, fr=10.0e3)
'''Calculate the FFT's of the data sets'''
f_raw_ac_res, Pxx_raw_ac_res = signal.periodogram(raw_ac_res.data[:, 0] + 1j*raw_ac_res.data[:, 1],
                                                  raw_ac_res.fs, window='hann', nfft=int(100e3))
f_pfb_bin, Pxx_pfb_bin = signal.periodogram(pfb_bin.data[:, 0] + 1j*pfb_bin.data[:, 0], fs=pfb_bin.fs,
                                            window='hann', nfft=int(100e3))
f_ddc_mix_on, Pxx_ddc_mix_on = signal.periodogram(ddc_mix_on.data[:, 0] + 1j*ddc_mix_on.data[:, 0],
                                                  ddc_mix_on.fs, window='hann', nfft=int(10e3))

# This is for pylab
'''Probing AC Bias resonator Fr = 10.0kHz, 4Phi_not, RAW ADC'''
pl.figure()
pl.plot(raw_ac_res.data[:10000,:], 'k')
pl.xlabel('$x$ [Sample Number]', fontsize=16)
pl.ylabel('$y$ [ADC Units]', fontsize=16)
pl.title('Res, $F_r$ = 10.0kHz, 4$\Phi_o$, RAW ADC', fontsize=18)

pl.figure()
pl.plot(f_raw_ac_res/1e6, Pxx_raw_ac_res, 'k')
pl.xlabel('$f$ in MHz [Frequency Bin]', fontsize=16)
pl.ylabel('$Pxx$ [Arb Units]', fontsize=16)
#pl.ylim(1e-7, 1e-3)
pl.xlim(-42, -38)
pl.title('Res, $F_r$ = 10.0kHz, 4$\Phi_o$, RAW ADC FFT', fontsize=18)


# PyQtGraph
win0 = pg.GraphicsWindow(title='Raw ADC Time Stream and FFT')
pTime0 = win0.addPlot(row=1, col=0, title='Raw ADC Time Stream')  # Time Stream
pTime0.addLegend()  # Has to be called before adding the plots
pFft0 = win0.addPlot(row=2, col=0, title='RAW ADC FFT')  # FFT

pTime0.plot(np.real(raw_ac_res.data[:20000, 0]), pen="r", name='I')
pTime0.plot(np.real(raw_ac_res.data[:20000, 1]), pen="g", name='Q')

pFft0.plot(x=f_raw_ac_res, y=Pxx_raw_ac_res, pen="b")


'''Probing AC Bias resonator Fr = 10.0kHz, 4Phi_not, PFb Output'''
#pl.figure(figsize=(15,9))
pl.figure()
pl.plot(np.real(pfb_bin.data[:200, 0]), 'b', label='Real')
pl.plot(np.imag(pfb_bin.data[:200, 0]), 'g', label='Imag')
pl.xlabel('$x$ [Sample Number]', fontsize=16)
pl.ylabel('$y$ [Arb Units]', fontsize=16)
pl.xlim(0, 200)
#pl.ylim(-1.5,1.5)
pl.title('PFB Bin 473 Output', fontsize=18)
pl.legend()

pl.figure()
pl.plot(f_pfb_bin/1e3, Pxx_pfb_bin, 'k')
pl.xlim(-1000, 1000)
pl.xlabel('$f$ in kHz [Frequency Bin]', fontsize=16)
pl.ylabel('$Pxx$ [Arb Units]', fontsize=16)
pl.title('PFB Bin 473 FFT', fontsize=18)

pl.figure()
pl.semilogy(f_pfb_bin/1e3, Pxx_pfb_bin, 'k')
pl.xlabel('$f$ in kHz [Frequency Bin]', fontsize=16)
pl.ylabel('$Pxx$ [Arb Units]', fontsize=16)
#pl.ylim(1e0, 1e8)
pl.xlim(-1000, 1000)
pl.title('PFb Bin 473 FFT', fontsize=18)

'''DM4 mix on Fr = 62.5kHz, 2Phi_not, PFb Output'''
#pl.figure(figsize=(15,9))
pl.figure()
pl.plot(np.real(ddc_mix_on.data[:200, 0]), 'b', label='Real')
pl.plot(np.imag(ddc_mix_on.data[:200, 0]), 'g', label='Imag')
pl.xlabel('$x$ [Sample Number]', fontsize=18)
pl.ylabel('$y$ [Arb Units]', fontsize=18)
pl.xlim(0.0,200)
#pl.ylim(-1.5,1.5)
pl.title('ddc_mix_on Bin 473 Output', fontsize=18)
pl.legend()

pl.figure()
pl.plot(f_ddc_mix_on/1e3, Pxx_ddc_mix_on, 'k')
pl.xlim(-1000, 1000)
pl.xlabel('$f$ in kHz [Frequency Bin]', fontsize=16)
pl.ylabel('$Pxx$ [Arb Units]', fontsize=16)
pl.title('ddc_mix_on Bin 473 FFT', fontsize=18)

pl.figure()
pl.semilogy(f_ddc_mix_on/1e3, Pxx_ddc_mix_on, 'k')
pl.xlabel('$f$ in kHz [Frequency Bin]', fontsize=16)
pl.ylabel('$Pxx$ [Arb Units]', fontsize=16)
#pl.ylim(1e0, 1e8)
pl.xlim(-1000, 1000)
pl.title('ddc_mix_on Bin 473 FFT', fontsize=18)

'''Plot Resonator ARC'''
x0, y0, r0, xvals, yvals = r2.fit_circle(np.real(ddc_mix_on.data[:, 0]), np.imag(ddc_mix_on.data[:, 0]), method='taubin')

pl.figure()
pl.plot(np.real(ddc_mix_on.data[:10000, 0]), np.imag(ddc_mix_on.data[:10000, 0]), 'k', label='IQ Plane Arc')
pl.axis('equal')
pl.plot(0, 0, 'g*', label='IQ Plane Origin')
pl.plot(x0, y0, 'b*', label='Fit Arc Center')
pl.plot(xvals, yvals, 'r', label='Fit Arc Circle')
pl.ylabel('$\Re$ [Arb Units]', fontsize=16)
pl.xlabel('$\Im$ [Arb Units]', fontsize=16)
pl.title('Resonator Arc on IQ Plane', fontsize=18)

'''Translate the arc to IQ origin'''
translated = ddc_mix_on.data[:,0] - (x0 + 1j*y0)
x0, y0, r0, xvals, yvals = r2.fit_circle(np.real(translated), np.imag(translated), method='taubin')

pl.figure()
pl.plot(np.real(translated[:1000]), np.imag(translated[:1000]), 'k', label='IQ Plane Arc')
pl.axis('equal')
pl.plot(0, 0, 'g*', label='IQ Plane Origin')
pl.plot(xvals, yvals, 'r', label='Fit Arc Circle')
pl.ylabel('$\Re$ [Arb Units]', fontsize=16)
pl.xlabel('$\Im$ [Arb Units]', fontsize=16)
pl.title('Translated Resonator Arc on IQ Plane', fontsize=18)

rotate_by = -120
rotated = translated * (np.cos(np.pi*rotate_by/180) + 1j*np.sin(np.pi*rotate_by/180))
pl.figure()
pl.plot(np.real(rotated[:1000]), np.imag(rotated[:1000]), 'k', label='IQ Plane Arc')
pl.axis('equal')
pl.plot(0, 0, 'g*', label='IQ Plane Origin')
pl.plot(xvals, yvals, 'r', label='Fit Arc Circle')
pl.ylabel('$\Re$ [Arb Units]', fontsize=16)
pl.xlabel('$\Im$ [Arb Units]', fontsize=16)
pl.title('Rotated Resonator Arc on IQ Plane', fontsize=18)
pl.plot([0, np.min(xvals)], [0, 0], label='Arc Tan Wrap Line')

'''Take Arctan(Resonator Arc)'''
pl.figure()
pl.plot(np.real(rotated[:1000]), np.imag(rotated[:1000]), 'k', label='IQ Plane Arc')
pl.axis('equal')
pl.plot(0, 0, 'g*', label='IQ Plane Origin')
pl.plot(xvals, yvals, 'r', label='Fit Arc Circle')
pl.ylabel('$\Re$ [Arb Units]', fontsize=16)
pl.xlabel('$\Im$ [Arb Units]', fontsize=16)
pl.title('Rotated Resonator Arc on IQ Plane', fontsize=18)
pl.plot([0, np.min(xvals)], [0, 0])

upper_point = np.argmax(np.imag(rotated))
lower_point = np.argmin(np.imag(rotated))
pl.plot([0, np.real(rotated[upper_point])], [0, np.imag(rotated[upper_point])], 'g')
pl.plot([0, np.real(rotated[lower_point])], [0, np.imag(rotated[lower_point])], 'g')

theta = np.arctan2(np.imag(rotated), np.real(rotated))
pl.figure()
pl.plot(theta[:400], label='Resonator Phase')
pl.plot(ddc_mix_on.sync[:400]*(np.max(theta) - np.min(theta)) + np.min(theta), label='Flux Ramp Sync')
pl.ylabel('$\Theta$ [Radians]', fontsize=16)
pl.xlabel('$x$ [Sample Number]', fontsize=16)
pl.title('Resonator V\Phi from Flux Ramp Response', fontsize=18)


# DM 4 mix on plots and circle fits
win1 = pg.GraphicsWindow(title='Raw ADC Time Stream and FFT')
pTime1 = win1.addPlot(row=1, col=0, title='Resonator Arc Timestream')  # Time Stream
pTime1.addLegend()  # Has to be called before adding the plots
pTime2 = win1.addPlot(row=1, col=1, title='Resonator Arc and fit')  # Time Stream
pTime2.addLegend()
pTime3 = win1.addPlot(row=2, col=1, title='Res Arc Centered and fitted')  # Time Stream
pTime3.addLegend()
pFft1 = win1.addPlot(row=2, col=0, title='Resonator Arc FFT')  # FFT

pTime1.plot(np.real(ddc_mix_on.data[:300, 0]), pen="r", name='I')
pTime1.plot(np.imag(ddc_mix_on.data[:300, 0]), pen="g", name='Q')

x0, y0, r0, xvals, yvals = r2.fit_circle(np.real(ddc_mix_on.data[:, 0]), np.imag(ddc_mix_on.data[:, 0]), method='taubin')

pTime2.plot(x=np.real(ddc_mix_on.data[:3000, 0]), y=np.imag(ddc_mix_on.data[:3000, 0]), pen="r", name='Arc')
pTime2.plot(x=xvals, y=yvals, pen='g', name='Taubin Fit')
pTime2.plot(x=[0], y=[0], symbol='o', symbolBrush=0.25, symbolPen='r', name='Origin')
pTime2.setAspectLocked(True)

translated = ddc_mix_on.data[:, 0] - (x0 + 1j*y0)
rotate_by = -120
rotated = translated * (np.cos(np.pi*rotate_by/180) + 1j*np.sin(np.pi*rotate_by/180))

x0, y0, r0, xvals, yvals = r2.fit_circle(np.real(rotated), np.imag(rotated), method='taubin')
pTime3.plot(x=np.real(rotated[:3000]), y=np.imag(rotated[:3000]), pen="r", name='Arc')
pTime3.plot(x=xvals, y=yvals, pen='g', name='Taubin Fit')
pTime3.plot(x=[0], y=[0], symbol='o', symbolBrush=0.25, symbolPen='r', name='Origin')
pTime3.setAspectLocked(True)

pFft1.plot(x=f_ddc_mix_on/1e3, y=Pxx_ddc_mix_on, pen="b")

frdm_mix = 0