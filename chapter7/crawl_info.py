'''
封装网络获取的信息
'''
import requests
from bs4 import BeautifulSoup

def get_info(url):
    response = requests.get(url)
    if response.status_code ==200:
        soup = BeautifulSoup(response.text,'lxml')
        print(soup.title.string)