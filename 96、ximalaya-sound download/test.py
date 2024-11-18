import requests

# 音频文件的 URL
url = "https://audiopay.cos.tx.xmcdn.com/download/1.0.0/storages/c023-audiopay/5E/B9/GKwRIUEGNykhAEWo6wFA59wA.m4a?sign=835eeee87a7455043690282997bedc05&buy_key=FM&timestamp=1728218665479000&token=3309&duration=563"

# 发送 GET 请求
response = requests.get(url)

# 检查请求是否成功
if response.status_code == 200:
    # 将内容写入文件
    with open("audio.m4a", "wb") as file:
        file.write(response.content)
    print("下载成功！音频文件已保存为 audio.m4a")
else:
    print(f"下载失败，状态码：{response.status_code}")