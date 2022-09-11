import numpy as np
import matplotlib.pyplot as plt
import math
samplerate=1000

sinewave= np.zeros([1000,2])
# print(sinewave)

pi=22/7

freq=[7,10,11]
amps=[1,5,10]
phases=[pi/4,0,pi/2]
instants=np.arange(0,1,0.001)
# print(instants)

# waves_generated=[[[],]*1000,]*5
# print(waves_generated)
waves_generated1=[[]]*1000
waves_generated2=[[]]*1000
waves_generated3=[[]]*1000

# print(waves_generated1)
# for i in range(5):
#     for j in range(1000):
#         waves_generated[i][j]=amps[i]*math.sin((2*pi*freq[i]*instants[j])+phases[i])
#     print(waves_generated[i][500],i)
for j in range(1000):
    waves_generated1[j]=amps[0]*math.sin((2*pi*freq[0]*instants[j])+phases[0])
print(waves_generated1[500])
for j in range(1000):
    waves_generated2[j]=amps[1]*math.sin((2*pi*freq[1]*instants[j])+phases[1])
print(waves_generated2[500])
for j in range(1000):
    waves_generated3[j]=amps[2]*math.sin((2*pi*freq[2]*instants[j])+phases[2])
print(waves_generated3[500])

# for k in range(5):
#     print(waves_generated[k][500])
# print(waves_generated[0][0])
m=0
# while(True):
#     if keyboard.is_pressed('r'):
#         m+=1
#         continue
#     elif keyboard.is_pressed('z'):
#         break
#     else:
#         plt.plot(waves_generated[m])
#         plt.ylabel('amplitude')
#         plt.xlabel('time')
#         plt.show()
    
# plt.plot(waves_generated[2])
# plt.plot(waves_generated[0])
plt.plot(waves_generated1)
plt.plot(waves_generated2)
plt.plot(waves_generated3)

plt.ylabel('amplitude')
plt.xlabel('time')
plt.show()
# print(waves_generated[0]==waves_generated[1])
# print(waves_generated[1])
combined_wave=np.array([])
combined_wave=np.add(np.add(waves_generated1,waves_generated2),waves_generated3)
plt.plot(combined_wave)
plt.ylabel('amplitude')
plt.xlabel('time in milliseconds')
plt.show()
# np.save('EEGwave',combined_wave)
print(combined_wave)