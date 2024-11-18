## 爬取pornhub视频
import requests
import re
import os
import json
import urllib.parse
from tqdm import tqdm
from bs4 import BeautifulSoup
from urllib.parse import urlparse, parse_qs
from tqdm import tqdm  # 用于显示进度条
from datetime import datetime

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
    "Referer": "https://www.pornhub.com/",
    "sec-ch-ua": '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    "origin": "https://www.pornhub.com",
}


def get_video_url(
    url, parameters, file_path, selected_quality, session=requests.session()
):

    response = session.get(url, params=parameters, headers=headers)

    soup = BeautifulSoup(response.text, "html.parser")

    script = soup.find_all("script", type="text/javascript")[11]
    # video title
    video_title_decoded = title_check(script)

    flashvars_pattern = r"var\s+flashvars_\d{9}\s*=\s*(\{.*?\});"

    if script.string:  # 确保 script 标签有内容
        match = re.search(flashvars_pattern, script.string, re.DOTALL)
        if match:
            flashvars_json = match.group(1)  # 获取 flashvars 的部分
            # 将 JSON 字符串转换为字典
            try:
                flashvars_dict = json.loads(flashvars_json)
                media_definitions = flashvars_dict.get("mediaDefinitions")

                if media_definitions:  # 确保 media_definitions 不为空

                    if selected_quality == "1080P":
                        video_url = media_definitions[0]["videoUrl"]
                    elif selected_quality == "720P":
                        video_url = media_definitions[3]["videoUrl"]
                    elif selected_quality == "480P":
                        video_url = media_definitions[2]["videoUrl"]
                    elif selected_quality == "240P":
                        video_url = media_definitions[1]["videoUrl"]
                    else:
                        print(
                            "Can't find a video with the corresponding quality, please select again"
                        )

                    # 检测网址后缀有几个部分
                    process_url(video_url, session, video_title_decoded, file_path)

                else:
                    print("No mediaDefinitions found")
            except json.JSONDecodeError:
                print("Failed to decode JSON.")
        else:
            print("No flashvars found")


def process_url(video_url, session, file_path, video_title_decoded):
    if "hv-h" in video_url:
        handle_hv_h(video_url, session, file_path, video_title_decoded)

    elif "cv-h" in video_url:
        handle_cv_h(video_url, session, file_path, video_title_decoded)

    elif "iv-h" in video_url:
        handle_iv_h(video_url, session, file_path, video_title_decoded)

    elif "ev-h" in video_url:
        handle_ev_h(video_url, session, file_path, video_title_decoded)

    else:
        print("Unknown URL format")


def handle_hv_h(video_url, session, file_path, video_title_decoded):
    # 使用正则表达式提取所需部分
    pattern = r"/hls/videos/(.*?)\.mp4"
    url_match = re.search(pattern, video_url)
    video_info = url_match.group(1)

    response = session.get(video_url, headers=headers)

    # 检查响应状态码
    if response.status_code == 200:
        # 使用正则表达式提取 .m3u8 文件链接
        match = re.search(r"(index-v1-a1\.m3u8\?.*)", response.text)
        m3u8_link = match.group(1)
        index_url = f"https://cv-h.phncdn.com/hls/videos/{video_info}.mp4"
        index_v1_url = index_url + "/" + m3u8_link
        seg_response = session.get(index_v1_url, headers=headers)
        print(seg_response.text)
        # 使用正则表达式提取以 seg- 开头的链接及其参数
        segments = re.findall(
            r"(seg.*?\n)",
            seg_response.text,
        )
        download_video(
            segments, index_url, file_path, video_title_decoded, new_hash=None
        )


def handle_cv_h(video_url, session, file_path, video_title_decoded):

    # 使用正则表达式提取所需部分
    pattern = r"/hls/videos/(.*?)\.mp4"
    url_match = re.search(pattern, video_url)

    video_info = url_match.group(1)

    response = session.get(video_url, headers=headers)
    # 检查响应状态码
    if response.status_code == 200:
        # 使用正则表达式提取 .m3u8 文件链接
        match = re.search(r"(index-v1-a1\.m3u8\?.*)", response.text)
        m3u8_link = match.group(1)
        index_url = f"https://cv-h.phncdn.com/hls/videos/{video_info}.mp4"
        index_v1_url = index_url + "/" + m3u8_link
        seg_response = session.get(index_v1_url, headers=headers)
        # 使用正则表达式提取以 seg- 开头的链接及其参数
        segments = re.findall(
            r"(seg.*?\n)",
            seg_response.text,
        )
        download_video(
            segments, index_url, file_path, video_title_decoded, new_hash=None
        )


def handle_iv_h(video_url, session, file_path, video_title_decoded):
    # 正则表达式
    pattern = r"\/([^\/]+?,\d+)\/"
    # 提取链接中的参数
    code_match = re.search(pattern, video_url)
    code = code_match.group(1)

    # 使用正则表达式提取所需部分
    pattern = r"/hls/videos/(.*?)\.mp4"
    url_match = re.search(pattern, video_url)

    video_info = url_match.group(1)

    response = session.get(video_url, headers=headers)
    print(response)
    print(response.text)
    # 检查响应状态码
    if response.status_code == 200:
        # 使用正则表达式提取 .m3u8 文件链接
        match = re.search(r"(index-v1-a1\.m3u8.*)", response.text)
        if match:
            m3u8_link = match.group(1)
            index_url = f"https://iv-h.phncdn.com/{code}/hls/videos/{video_info}.mp4"
            index_v1_url = index_url + "/" + m3u8_link
            seg_response = session.get(index_v1_url, headers=headers)
            print(seg_response.text)
            # 使用正则表达式提取以 seg- 开头的链接及其参数
            segments = re.findall(
                r"seg-\d+-v1-a1\.ts",
                seg_response.text,
            )

            download_video(segments, index_url, file_path, video_title_decoded)


def handle_ev_h(video_url, session, file_path, video_title_decoded):
    # 使用正则表达式提取hash部分
    hash_match = re.search(r"hash=[^&]+", video_url)
    new_hash = hash_match.group(0)

    # 使用正则表达式提取所需部分
    pattern = r"/hls/videos/(.*?)\.mp4"
    url_match = re.search(pattern, video_url)

    video_info = url_match.group(1)
    response = session.get(video_url, headers=headers)
    # 检查响应状态码
    if response.status_code == 200:
        # 使用正则表达式提取 .m3u8 文件链接
        match = re.search(r"(index-v1-a1\.m3u8\?[^\\n]+)", response.text)
        if match:
            m3u8_link = match.group(1)
            index_url = f"https://ev-h.phncdn.com/hls/videos/{video_info}.mp4"
            index_v1_url = index_url + "/" + m3u8_link
            seg_response = session.get(index_v1_url, headers=headers)
            # 使用正则表达式提取以 seg- 开头的链接及其参数
            segments = re.findall(
                r"(seg-\d+-v\d+-a\d+\.ts\?validfrom=\d+&validto=\d+&ipa=\d+\.\d+\.\d+\.\d+&hdl=-1&hash=.*)",
                seg_response.text,
            )
            download_video(
                segments, index_url, file_path, video_title_decoded, new_hash
            )


def title_check(script):
    # 正则表达式用于匹配 video_title
    video_title_pattern = r'"video_title":"(.*?)"'
    match_title = re.search(video_title_pattern, script.string, re.DOTALL)

    if match_title:
        video_title = match_title.group(1)
        # 使用 json.loads 处理字符串
        video_title_decoded = json.loads(f'"{video_title}"')

        # 定义非法字符的正则表达式
        illegal_chars_pattern = r'[<>:"/\\|?*\'"]'  # 添加空格到非法字符列表

        # 去除非法字符
        video_title_decoded_cleaned = re.sub(
            illegal_chars_pattern, "", video_title_decoded
        )

        # 去除多余的空格
        video_title_decoded_cleaned = video_title_decoded_cleaned.strip()

        return video_title_decoded_cleaned
    else:
        print("No video title found")


## 下载视频
def download_video(segments, index_url, video_title_decoded, file_path, new_hash):
    # 获取当前日期和时间，格式为 YYYYMMDD_HHMM
    date_folder = datetime.now().strftime("%Y%m%d_%H%M")

    # 创建以日期命名的保存路径
    title_folder = os.path.join(file_path, date_folder)
    os.makedirs(title_folder, exist_ok=True)

    if segments is None:
        print("No segments found")
        return

    # 下载每个段并显示进度条
    for i, segment in enumerate(segments):
        # 设置目标文件路径
        target_file = os.path.join(title_folder, f"segment_{i + 1}.ts")

        download_url = index_url + "/" + segment

        if new_hash is not None:
            # 替换掉旧的 hash
            updated_download_url = re.sub(r"hash=[^&]+", new_hash, download_url)

            # 下载文件
            response = requests.get(updated_download_url, stream=True)
        else:
            # 下载文件
            response = requests.get(download_url, stream=True)

        total_size = int(response.headers.get("content-length", 0))

        with open(target_file, "wb") as file:
            # 使用 tqdm 创建进度条
            with tqdm(
                total=total_size,
                unit="B",
                unit_scale=True,
                desc=f"Downloading segment {i + 1}",
            ) as pbar:
                for data in response.iter_content(chunk_size=4096):
                    file.write(data)
                    pbar.update(len(data))

    # 合并 .ts 文件
    merge_ts_files(file_path, date_folder)


## 合并视频
def merge_ts_files(file_path, video_title_decoded):
    # 创建以 video_title_decoded 命名的保存路径
    title_folder = os.path.join(file_path, video_title_decoded)
    # 输出文件名
    output_file = os.path.join(title_folder, f"{video_title_decoded}.mp4")

    # 获取所有.ts文件
    ts_files = [f for f in os.listdir(title_folder) if f.endswith(".ts")]
    ts_files.sort(key=lambda x: int(re.search(r"\d+", x).group()))  # 按数字顺序排序

    # 创建合并列表
    with open(os.path.join(title_folder, "file_list.txt"), "w") as f:
        for ts_file in ts_files:
            f.write(f"file '{ts_file}'\n")

    # 使用 ffmpeg 合并文件
    os.system(
        f"ffmpeg -f concat -safe 0 -i {os.path.join(title_folder, 'file_list.txt')} -c copy {output_file}"
    )

    # 清理临时文件
    os.remove(os.path.join(title_folder, "file_list.txt"))

    print(f"视频已合并，输出文件: {output_file}")


def main():
    while True:
        # 获取用户输入的视频网址
        url = input(
            "请输入需要下载的视频的网址,退出请输入exit（例如：https://www.pornhub.com/view_video.php?viewkey=6485417b2fcf6）："
            # https://www.pornhub.com/view_video.php?viewkey=660972182ae55
        )

        # 用户选择退出
        if url.lower() == "exit":
            print("程序已退出。")
            return

        # 提取 viewkey 参数
        parameters = {}
        if "viewkey=" in url:
            parameters["viewkey"] = url.split("viewkey=")[-1]
            break  # 如果提取成功，退出循环
        else:
            print("无效的网址，请确保包含 viewkey 参数。")

    # 获取用户选择的清晰度
    print("请选择下载视频的清晰度：")
    print("1. 1080P")
    print("2. 720P")
    print("3. 480P")
    print("4. 240P")

    choice = input("请输入对应的数字（1-4）：")

    # 根据用户的选择设置清晰度参数
    quality_mapping = {"1": "1080P", "2": "720P", "3": "480P", "4": "240P"}

    selected_quality = quality_mapping.get(choice)
    if selected_quality:
        print(f"您选择的清晰度是：{selected_quality}")
    else:
        print("无效的选择，程序结束。")
        return

    # 设置文件保存路径
    file_path = r"D:\Code\DarkCatPython\WebCrawler\pronhub_video_download\video"

    # 调用下载函数
    get_video_url(url, parameters, file_path, selected_quality)


if __name__ == "__main__":
    main()
