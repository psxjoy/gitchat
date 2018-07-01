import requests
import json


def get_info(url):
    web_data = requests.get(url)
    result = web_data.text
    fin = json.loads(result)
    pm=fin["results"][0]["pm25"]
    temperature=fin["results"][0]["weather_data"][0]["temperature"]  ##今天的温度
    weather=fin["results"][0]["weather_data"][0]["weather"]  ##今天的天气情况
    wind=fin["results"][0]["weather_data"][0]["wind"]  ##今天的风向
    return "temperature:{0},pm2.5:{1}".format(temperature,pm)