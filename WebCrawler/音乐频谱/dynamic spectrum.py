import numpy as np
import matplotlib.pyplot as plt
import pyaudio
from scipy.fft import fft

# 参数设置
CHUNK = 1024  # 每个数据块的样本数
FORMAT = pyaudio.paInt16  # 音频格式
CHANNELS = 1  # 单声道
RATE = 5500  # 新的采样率，降低至 5.5 kHz

# 初始化 PyAudio
p = pyaudio.PyAudio()

# 打开音频流，确保选择虚拟音频设备作为输入
stream = p.open(format=FORMAT, channels=CHANNELS,
                 rate=RATE, input=True,
                 frames_per_buffer=CHUNK)

# 设置绘图
plt.ion()  # 开启交互模式
fig, ax = plt.subplots(figsize=(10, 6))
x = np.linspace(20, 10000, int(CHUNK / 2))  # 频率范围，从 20 Hz 到 20 kHz
bars = ax.bar(x, np.zeros(CHUNK // 2), width=50, color='cyan', edgecolor='black', linewidth=1.0)  # 矩形条形图
ax.set_ylim(0, 255)  # 频谱的幅度限制
ax.set_xlim(20, 10000)  # X轴频率范围
ax.set_title("Real-time Audio Spectrum (Downsampled to 5.5 kHz)")
ax.set_xlabel("Frequency (Hz)")
ax.set_ylabel("Amplitude")

# 实时更新频谱
try:
    while True:
        # 从音频流读取数据
        data = stream.read(CHUNK, exception_on_overflow=False)
        # 将数据转换为数组
        samples = np.frombuffer(data, dtype=np.int16)
        
        # 计算FFT
        yf = fft(samples)
        yf = np.abs(yf[:CHUNK // 2])  # 只取一半
        
        # 更新条形图
        for bar, height in zip(bars, yf):
            bar.set_height(height * 0.8)  # 调整高度以增加粒子跳动效果
            
            # 限制透明度在0到1之间
            alpha = min(1, max(0, 0.5 + 0.5 * (height / 255)))
            bar.set_alpha(alpha)  # 动态调整透明度以模拟粒子效果

        plt.draw()
        plt.pause(0.01)  # 暂停以更新图形
except KeyboardInterrupt:
    print("Stopping.")

# 清理
stream.stop_stream()
stream.close()
p.terminate()
plt.ioff()  # 关闭交互模式
plt.show()
