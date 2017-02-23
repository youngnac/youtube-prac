import json
import os
from pprint import pprint
import requests

# 1. .conf폴더에서 settings_local.json을 읽어온다(abspath:현재 dirname: 부모 join 하위)
current_pwd = os.path.abspath(__file__)
conf = os.path.join(os.path.dirname(os.path.dirname(current_pwd)), '.conf')
# json.load로 읽기
target = os.path.join(conf, 'settings_local.json')
f = open(os.path.join(conf, 'settings_local.json'))
key_ = json.loads(open(os.path.join(conf, 'settings_local.json')).read())

# option1
# key_ = json.loads(f.read())
# f.close()

# ##option 2
# ## 파일 열고 닫고 따로 안해도 됨 확실히 닫힘
# # with open(target,'r') as f:
# #     config_str = f.read()

# parameter 설정
part = "snippet"
keyword = "유지태"
r_key = key_['youtube']['API_KEY']
objects_number = 50

my_param = {'part': part, 'q': keyword, 'key': r_key, 'maxResults': objects_number}
youtube_url ="https://www.googleapis.com/youtube/v3/search"
# url = "https://www.googleapis.com/youtube/v3/search?part=" + part + "&q=" + keyword + "&key=" + r_key

r = requests.get(youtube_url,params =my_param)
print(r.url)
r_text = json.loads(r.text)
# pprint(r_text)

item = r_text["items"]

for index,i in enumerate(item):
    title = i["snippet"]["title"]
    video_id = i["id"]["videoId"]
    channel_id = i["snippet"]["channelId"]
    channel_title = i["snippet"]["channelTitle"]
    print(channel_id,channel_title)

