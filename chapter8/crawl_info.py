#!/usr/bin/python
# -*- coding: UTF-8 -*-
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
    return "【Git天气】亲爱的Gitic，今天的天气为{0}，温度{1}，风向{2}，PM2.5浓度为{3}".format(weather,temperature,wind,pm)