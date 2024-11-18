import pygame
import wave
import struct
import numpy as np

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("动态音频可视化")
clock = pygame.time.Clock()

# 加载音频文件
def load_audio(filename):
    wave_file = wave.open(filename, 'r')
    sample_rate = wave_file.getframerate()
    n_samples = wave_file.getnframes()
    audio = wave_file.readframes(n_samples)
    wave_file.close()
    
    samples = struct.unpack('{n}h'.format(n=n_samples), audio)
    samples = np.array(samples)
    return samples, sample_rate

audio_samples, sample_rate = load_audio(r'D:\Code\DarkCatPython\WebCrawler\PyQt5案例-音乐下载器\音乐下载\爱情转移陈奕迅歌词版.mp3')

# 实现音频可视化
def visualize_audio(screen, samples, sample_rate):
    width, height = screen.get_size()
    n_samples = len(samples)
    x_scale = width / n_samples
    y_scale = height / 2 / max(abs(samples))
    
    for i in range(n_samples - 1):
        x1 = int(i * x_scale)
        y1 = int(height / 2 - samples[i] * y_scale)
        x2 = int((i + 1) * x_scale)
        y2 = int(height / 2 - samples[i + 1] * y_scale)
        pygame.draw.line(screen, (255, 255, 255), (x1, y1), (x2, y2))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((0, 0, 0))
    visualize_audio(screen, audio_samples, sample_rate)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()