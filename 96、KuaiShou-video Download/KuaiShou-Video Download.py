## 下载快手视频

import requests
import os
import re
import time
import json

headers = {
'content-type':'application/json',
'cookie':'kpf=PC_WEB; clientid=3; did=web_72b4fc87f9f062980cb6332c8a26aa80; kpn=KUAISHOU_VISION',
'host':'www.kuaishou.com',
'origin':'https://www.kuaishou.com',
'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
}

session=requests.session()

def download(file_path,key):
    
    home_url = 'https://www.kuaishou.com/?isHome=1'

    ## https://www.kuaishou.com/search/video?searchKey=%E9%A3%8E%E6%99%AF
    search_url = f'https://www.kuaishou.com/search/video?searchKey={key}'
    # 获取视频Json文件
    real_url = 'https://www.kuaishou.com/graphql'

    session.get(home_url,headers=headers)
    # search_re = session.post(search_url,headers=headers,verify=False)
    # payload = {"operationName":"graphqlSearchUser","variables":{"keyword":"风景"},"query":"query graphqlSearchUser($keyword: String, $pcursor: String, $searchSessionId: String) {\n  visionSearchUser(keyword: $keyword, pcursor: $pcursor, searchSessionId: $searchSessionId) {\n    result\n    users {\n      fansCount\n      photoCount\n      isFollowing\n      user_id\n      headurl\n      user_text\n      user_name\n      verified\n      verifiedDetail {\n        description\n        iconType\n        newVerified\n        musicCompany\n        type\n        __typename\n      }\n      __typename\n    }\n    searchSessionId\n    pcursor\n    __typename\n  }\n}\n"}
    data = {
        'operationName': "visionSearchPhoto",
        'variables': {'keyword': f"{key}", 'pcursor': "", 'page': "search"},
        'query':"fragment photoContent on PhotoEntity {\n  __typename\n  id\n  duration\n  caption\n  originCaption\n  likeCount\n  viewCount\n  commentCount\n  realLikeCount\n  coverUrl\n  photoUrl\n  photoH265Url\n  manifest\n  manifestH265\n  videoResource\n  coverUrls {\n    url\n    __typename\n  }\n  timestamp\n  expTag\n  animatedCoverUrl\n  distance\n  videoRatio\n  liked\n  stereoType\n  profileUserTopPhoto\n  musicBlocked\n  riskTagContent\n  riskTagUrl\n}\n\nfragment recoPhotoFragment on recoPhotoEntity {\n  __typename\n  id\n  duration\n  caption\n  originCaption\n  likeCount\n  viewCount\n  commentCount\n  realLikeCount\n  coverUrl\n  photoUrl\n  photoH265Url\n  manifest\n  manifestH265\n  videoResource\n  coverUrls {\n    url\n    __typename\n  }\n  timestamp\n  expTag\n  animatedCoverUrl\n  distance\n  videoRatio\n  liked\n  stereoType\n  profileUserTopPhoto\n  musicBlocked\n  riskTagContent\n  riskTagUrl\n}\n\nfragment feedContent on Feed {\n  type\n  author {\n    id\n    name\n    headerUrl\n    following\n    headerUrls {\n      url\n      __typename\n    }\n    __typename\n  }\n  photo {\n    ...photoContent\n    ...recoPhotoFragment\n    __typename\n  }\n  canAddComment\n  llsid\n  status\n  currentPcursor\n  tags {\n    type\n    name\n    __typename\n  }\n  __typename\n}\n\nquery visionSearchPhoto($keyword: String, $pcursor: String, $searchSessionId: String, $page: String, $webPageArea: String) {\n  visionSearchPhoto(keyword: $keyword, pcursor: $pcursor, searchSessionId: $searchSessionId, page: $page, webPageArea: $webPageArea) {\n    result\n    llsid\n    webPageArea\n    feeds {\n      ...feedContent\n      __typename\n    }\n    searchSessionId\n    pcursor\n    aladdinBanner {\n      imgUrl\n      link\n      __typename\n    }\n    __typename\n  }\n}\n"
    }
    data =json.dumps(data)
    response = session.post(real_url, headers=headers, data=data)
    # print(response.status_code)
    print(response.text)
    feeds = response.json()['data']['visionSearchPhoto']['feeds']
    if not os.path.exists(file_path):
                os.mkdir(file_path)
    for feed in feeds:
        title = feed['photo']['caption']
        title = re.sub(r'[|/<>?\\]','',title)
        play_url = feed['photo']['videoResource']['h264']['adaptationSet'][0]['representation'][0]['url']

        if 'm3u8' in play_url:
            m3u8_url = requests.get(play_url).text
            ts_files = re.sub('#.*','',m3u8_url).split()
            url = play_url.split('/')[:-1]
            url = '/'.join(url) + '/'
            with open(f'{file_path}/{title}.mp4','ab') as f:
                for ts_file in ts_files:
                    ts_url = url + ts_file
                    ts_content = requests.get(ts_url).content
                    f.write(ts_content)
            print(f'长视频{title}下载完成')
        else:
            
            video_content = requests.get(play_url).contents
            with open(f'{file_path}/{title}.mp4','wb') as f:
                f.write(video_content)
                print(f'{title}下载完成')

if __name__ == '__main__':
     file_path = r'D:\Code\DarkCatPython\WebCrawler\KuaiShou-video Download\video'
     # 关键词 ：风景
     key = '日本'
     download(file_path,key)


