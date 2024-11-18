import requests
import pprint
from urllib.parse import quote

headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'
    }

url = 'https://api.freemp3cn.com/search'
## https://api.freemp3cn.com/getPlayUrl/z1iZfxhQ-eg
music_url = 'https://api.freemp3cn.com/getPlayUrl/'

def get_music(song_name):
    track_info = []
    success_flag = True
    param = {
        'query': song_name
    }

    try:
        r = requests.get(url,headers=headers,params=param)
        # print(r)
        if r.status_code != 200:
            success_flag = False
            return track_info,success_flag
        info = r.json()
        # pprint.pprint(info)
        
        items = info['items']
        # pprint.pprint(items)

        for more_info in items:
            mudic_info = more_info['title']
            music_id = more_info['id']
            ## {'downloadUrl': 'https://api.freemp3cn.com/download/_y88PDkP-vQ.mp3', 'playUrl': 'https://api.freemp3cn.com/mp3/_y88PDkP-vQ.mp3'}
            downloadUrl = f'https://api.freemp3cn.com/download/{music_id}.mp3'
            playUrl = f'https://api.freemp3cn.com/mp3/{music_id}.mp3'
            # print(mudic_info,downloadUrl,playUrl)
            track_info.append([mudic_info,downloadUrl,playUrl])
    except:
        success_flag = False  
    return track_info,success_flag

if __name__ == '__main__':
    song_name = '黄昏'
    track_info,success_flag = get_music(song_name)
    print(track_info)

