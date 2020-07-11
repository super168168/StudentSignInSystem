import wave
from pyaudio import PyAudio, paInt16

# 采样率
framerate = 8000
# 一个缓存能存多少个采样点(采样点)
Num_SAMPLES = 2000
#声道数
channels = 1
#2个字节 => 16位
sampwidth = 2
TIME = 2

# 写文件
def save_wave_file(filename, data):

    wf = wave.open(filename, 'wb')
    wf.setnchannels(1)
    wf.setsampwidth(2)
    wf.setframerate(8000)
    wf.writeframes(b"".join(data))
    wf.close()

# 读文件
def my_record():
    # 实例化一个PyAudio对象
    pa = PyAudio()
    # 打开声卡读文件 rate是采样率
    stream = pa.open(format = paInt16, channels = 1,
                     rate = framerate, input = True,
                     frames_per_buffer = Num_SAMPLES)
    my_buf=[]  # 存放数据
    count = 0
    while count < TIME*5: #一定时间内读取数据
        # 一次读2000个采样点的数据
        string_audio_data = stream.read(Num_SAMPLES)
        if count > 0:
            my_buf.append(string_audio_data)
        count += 1
        print('.')
    save_wave_file('testwav.wav', my_buf) #保存音频
    stream.close()

my_record()
print("OK")
