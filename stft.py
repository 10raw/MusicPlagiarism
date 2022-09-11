import librosa
import numpy as np
from os.path import dirname, join
def stft(filename,DOC):
    x,sr=librosa.load(filename)

    hop_length =512
    n_fft=2048
    win_len=1024
    X=librosa.stft(x,n_fft=n_fft,hop_length=hop_length,win_length=win_len)
    spec=librosa.power_to_db(abs(X))
    freqs = np.arange(0, 1 + n_fft / 2) * sr / n_fft
    print(spec.shape,freqs.shape)
    # print(spec)
    j=0
    MX=np.zeros((spec.shape[1],2))
    for i in range(0,spec.shape[0]):
        for k in range(0,spec.shape[1]):
            if spec[i][k]<0:
                spec[i][k]=0
            spec[i][k]=round(spec[i][k],0)
        
        # print(np.amax(spec[i]))

    specT=np.transpose(spec)
    for i in range(0,specT.shape[0]):
        m1,m2=specT[i].argsort()[-2:][::-1]
        MX[i][0]=m1
        MX[i][1]=m2
    # print(spec[1])
    # for j in spec[2]:
    #     print(j,'\n')

    # print(MX[0],MX[88],MX[155])
    f=open( dirname(__file__)+DOC,'w')
    for i in MX:
        f.write(str(int(i[0]))+" "+str(int(i[1])))
    f.close()
# './document_b.txt'
# stft('D:\Summer\OnsetDetection11\Server\Computations\download_B.wav')