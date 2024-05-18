import numpy as np
import matplotlib.pyplot as plt
T = 100
x = np.arange(0,T)
y=  np.sin(4*np.pi*x/T)+np.cos(8*np.pi*x/T)

# We have thus have a superposition of a sine and cosine with frequencies twice and four-times per step x. We now perform the Fourier Transform:

sp   = np.fft.fft(y)               # the discrete fourier transform
freq = np.fft.fftfreq(y.shape[-1]) # the accompanying frequencies

# Now we can reconstruct the original function 'y' through the fourier transform as a superposition of sines and cosines and check whether we succeeded by plotting.

cos=np.sum([(sp[-i]+sp[i]).real/(2*T)*np.cos(2.*np.pi*freq[i]*x)\
             for i in range(len(freq))],axis=0)
sin=np.sum([(sp[-i]-sp[i]).imag/200.*np.sin(2.*np.pi*freq[i]*x)\
              for i in range(len(freq))],axis=0)

plt.plot(x, y,x,cos+sin)
plt.show()