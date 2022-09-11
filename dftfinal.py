import matplotlib.pyplot as plt
import numpy as np
import math

samplingrate = 1000

ts = 1.0/samplingrate
t = np.arange(0,1,ts)

x=np.load('EEGwave.npy')
plt.figure(figsize = (8, 6))
plt.plot(t, x, 'r')
plt.ylabel('Amplitude')

plt.show()
def DFT(x):

    N = len(x)
    n = np.arange(N)
    k = n.reshape((N, 1))

    e=np.zeros(N)
    e = np.exp(-2j * np.pi * k * t)

    # X = np.dot(e, x)
    summ=0
    for m in range(t.shape[0]):
        summ=summ+(e[m]*x[m])
        
    return summ
X = DFT(x)


N = len(X)
n = np.arange(N)
T = N/samplingrate
freq = n/T 


plt.stem(freq, abs(X), 'b', markerfmt=" ", basefmt="-b")
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.show()

n_oneside = N//2

f_oneside = freq[:n_oneside]

X_oneside =X[:n_oneside]/n_oneside


plt.figure(figsize = (12, 6))
plt.subplot(121)
plt.stem(f_oneside, abs(X_oneside), 'b', markerfmt=" ", basefmt="-b")
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')

plt.subplot(122)
plt.stem(f_oneside, abs(X_oneside), 'b',  markerfmt=" ", basefmt="-b")
plt.xlabel('Frequency (Hz)')

plt.show()