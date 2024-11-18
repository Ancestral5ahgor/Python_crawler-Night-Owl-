import numpy as np
import matplotlib.pyplot as plt
import pyaudio
from scipy.fft import fft

# 初始化PyAudio
p = pyaudio.PyAudio()

# 列出可用的音频设备
for i in range(p.get_device_count()):
    info = p.get_device_info_by_index(i)
    print(f"Device {i}: {info['name']}")

# 请根据输出的信息，找到虚拟音频设备的索引
input_device_index = 1 # 根据你的输出选择设备索引
channels = 2  # 根据设备支持的通道数进行调整

# 参数设置
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 5500  # 采样率

# 打开音频流
stream = p.open(format=FORMAT, channels=CHANNELS,
                 rate=RATE, input=True,
                 frames_per_buffer=CHUNK,
                 input_device_index=input_device_index)

# 设置绘图
plt.ion()
fig, ax = plt.subplots(figsize=(10, 6))
x = np.linspace(20, 20000, int(CHUNK / 2))
bars = ax.bar(x, np.zeros(CHUNK // 2), width=80, color='cyan', edgecolor='black', linewidth=1.5)
ax.set_ylim(0, 255)
ax.set_xlim(20, 20000)
ax.set_title("Real-time Audio Spectrum from Specific Application")
ax.set_xlabel("Frequency (Hz)")
ax.set_ylabel("Amplitude")

# 实时更新频谱
try:
    while True:
        data = stream.read(CHUNK, exception_on_overflow=False)
        samples = np.frombuffer(data, dtype=np.int16)
        
        yf = fft(samples)
        yf = np.abs(yf[:CHUNK // 2])
        
        for bar, height in zip(bars, yf):
            bar.set_height(height * 0.8)
            alpha = min(1, max(0, 0.5 + 0.5 * (height / 255)))
            bar.set_alpha(alpha)

        plt.draw()
        plt.pause(0.01)
except KeyboardInterrupt:
    print("Stopping.")

# 清理
stream.stop_stream()
stream.close()
p.terminate()
plt.ioff()
plt.show()
