#!/usr/bin/python
# -*- coding: UTF-8 -*-
from chapter8.crawl_info import get_info
from chapter8.text_sdk import send_sms

if __name__ == '__main__':
    url = '	http://api.map.baidu.com/telematics/v3/weather?location=杭州&output=json&ak=你的ak值'
    text = get_info(url)
    send_sms("自己的接口私钥",text,"发送的手机号")