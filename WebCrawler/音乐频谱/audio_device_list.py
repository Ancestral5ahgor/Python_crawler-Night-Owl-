import pyaudio
import wave

# 设置音频参数
CHUNK = 1024 * 2  # 每次读取的音频数据量
FORMAT = pyaudio.paInt16  # 音频数据格式
CHANNELS = 2  # 音频通道数
RATE = 44100  # 采样率

# 初始化 PyAudio
p = pyaudio.PyAudio()

# 打开音频输入流
stream = p.open(
    format=FORMAT,
    channels=CHANNELS,
    rate=RATE,
    input=True,
    frames_per_buffer=CHUNK
)

# 记录音频数据
frames = []
for i in range(0, int(RATE / CHUNK * 5)):  # 记录 5 秒音频数据
    data = stream.read(CHUNK)
    frames.append(data)

# 停止音频输入流
stream.stop_stream()
stream.close()
p.terminate()

# 保存音频数据到 WAV 文件
wf = wave.open("output.wav", "wb")
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()