import wave,math
import matplotlib.pyplot as plt
import numpy as np


wav200=wave.open('10-sine_wave_signals-20hz-mono.wav','r')

raw200=wav200.readframes(-1)
raw200=np.fromstring(raw200,'Int16')
print(raw200)
if wav200.getnchannels() == 2:
    print("Just mono files")

print(wav200.getframerate())
# print("this is it",raw200[488040])
print('length',raw200.shape)

maxx=math.ceil(raw200.shape[0]/wav200.getframerate())
diff=maxx*wav200.getframerate()-raw200.shape[0]
u=np.zeros(diff,'Int16')

raw200=np.concatenate((raw200,u))
print(type(raw200))

print(type(u))
time=np.linspace(0,maxx,maxx*wav200.getframerate())

print('time',time.shape[0])
plt.figure(1)
plt.title("Signal Wave...")

plt.plot(time,raw200)
plt.show()


def exportwav():
    return [raw200,time]

np.save('eeg2.npy',raw200)