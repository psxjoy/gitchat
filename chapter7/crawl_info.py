'''
封装网络获取的信息
'''
import requests
from bs4 import BeautifulSoup
import re


def getUrlCoding(data):  # 解决网站的编码问题
    charset = 'utf-8'
    if data.encoding.lower() == 'utf-8' or data.encoding == 'utf8':
        return 'utf-8'
    if data.encoding.lower() == 'gb2312':
        return 'gb2312'
    if data.encoding.lower() == 'gbk':
        return 'gbk'
    if data.encoding.lower() == 'gb18030':
        return 'GB18030'
    m = re.compile('<meta .*(http-equiv="?Content-Type"?.*)?charset="?([a-zA-Z0-9_-]+)"?', re.I).search(data.text)
    if m and m.lastindex == 2:
        charset = m.group(2).lower()
    return charset


def get_info(url):
    response = requests.get(url)
    if response.status_code == 200:
        response.encoding = getUrlCoding(response)
        soup = BeautifulSoup(response.text, 'lxml')
        big_news = soup.select('#js_top_news > h2:nth-of-type(1) > a')[0].get_text()
        url = soup.select('#js_top_news > h2:nth-of-type(1) > a')[0].get('href')
        return "新闻标题："+big_news+"\n新闻地址："+url
