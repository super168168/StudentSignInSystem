import glob
from sklearn.mixture import GaussianMixture
import python_speech_features as feature
import numpy as np
import wave

def getWaveData(filename):
    fw = wave.open(filename,'rb')
    params = fw.getparams()
    #print(params)
    nchannels, sampwidth, framerate, nframes = params[:4]
    str_data = fw.readframes(nframes)
    wave_data = np.fromstring(str_data, dtype=np.int16)
    wave_data = wave_data * 1.0 / (max(abs(wave_data)))  # wave幅值归一化
    fw.close()
    return wave_data

def getGMM(filename):

    data = feature.mfcc(filename,samplerate=8000)
    gmm = GaussianMixture(5)
    gmmem = gmm.fit(data)
    return gmmem

def gmmem():
    names = ['ganjiahao', '廖俊杰', 'zhangwentao', 'laijintao']
    count = 1
    files = glob.glob('wavlib/' + str(count) + '*.wav')
    GMMs = []
    while (len(files) != 0):
        audio = []
        for file in files:
            temp = getWaveData(file);
            audio.extend(temp)
        audio = np.array(audio)
        count += 1
        files = glob.glob('wavlib/' + str(count) + '*.wav')
        gmm = getGMM(audio)
        GMMs.append(gmm)
    sampleData = getWaveData('temp.wav')
    sampleData = feature.mfcc(sampleData, samplerate=8000)
    maxPro = GMMs[0].score(sampleData)
    maxName = '廖俊杰'
    for index, GMM in enumerate(GMMs):
        probility = GMM.score(sampleData)
        print(probility)
        if maxPro < probility:
            maxPro = probility
            maxName = names[index]
    print("the max probability :{0}, name :{1}".format(maxPro, maxName))
    return maxName

if __name__=="__main__":
    a=gmmem()
    # names=['ganjiahao', 'liaojunjie', 'zhangwentao', 'laijintao' ]
    # count = 1
    # files = glob.glob('wavlib/'+str(count)+'*.wav')
    # GMMs = []
    # while(len(files) != 0):
    #     audio = []
    #     for file in files:
    #         temp = getWaveData(file);
    #         audio.extend(temp)
    #     audio=np.array(audio)
    #     count+=1
    #     files = glob.glob('wavlib/' + str(count) + '*.wav')
    #     gmm=getGMM(audio)
    #     GMMs.append(gmm)
    # sampleData = getWaveData('temp.wav')
    # sampleData = feature.mfcc(sampleData,samplerate=8000)
    # maxPro = GMMs[0].score(sampleData)
    # for index, GMM in enumerate(GMMs):
    #     probility = GMM.score(sampleData)
    #     print(probility)
    #     if maxPro < probility:
    #         maxPro = probility
    #         maxName = names[index]
    #     print("the max probability :{0}, name :{1}".format(maxPro, maxName))
