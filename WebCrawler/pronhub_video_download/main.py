from pornhub_video_download import get_video_url


def main():
    while True:
        # 获取用户输入的视频网址
        url = input(
            "请输入需要下载的视频的网址（例如：https://www.pornhub.com/view_video.php?viewkey=6485417b2fcf6）："
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
