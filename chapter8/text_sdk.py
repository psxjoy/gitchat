#!/usr/bin/python
# -*- coding: UTF-8 -*-
import urllib
import time
import sys
import httplib

def send_sms(apikey, text, mobile):
    sms_host = "sms.XXXXX.com"
    port = 443
    version = "v2"
    sms_send_uri = "/" + version + "/sms/single_send.json"
    params = urllib.urlencode({'apikey': apikey, 'text': text, 'mobile': mobile})
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    conn = httplib.HTTPSConnection(sms_host, port=port, timeout=30)
    conn.request("POST", sms_send_uri, params, headers)
    response = conn.getresponse()
    response_str = response.read()
    conn.close()
    return response_str