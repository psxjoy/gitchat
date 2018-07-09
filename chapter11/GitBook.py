import requests
import json
import re
from bs4 import BeautifulSoup
orignal_url = 'https://gitbook.cn/chat/activity/80/100?'

response = requests.get(orignal_url)
content  = json.loads(response.text)
data = content['data']
final_url = re.findall('/gitchat/activity/\S{24}',data)

def get_title(url):
    web_data = requests.get(url,verify=True)
    soup = BeautifulSoup(web_data.text,'lxml')
    title = soup.title.string
    print("Gitbook网址："+url,end='\t')
    print("GitBook课程名："+title)

for i in final_url:
    url = 'https://gitbook.cn'+i
    get_title(url)
