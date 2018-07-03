from chapter10.crwal_info import get_info
from chapter10.send_sms import send_sms
import time

if __name__ == '__main__':
    url = '	http://api.map.baidu.com/telematics/v3/weather?location=杭州&output=json&ak=你的AK值'
    now_hour = time.strftime('%H',time.localtime(time.time()))
    send_time = int(now_hour)
    if send_time==8:
        text = get_info(url)
        send_sms("要发送的手机号码","Twilio提供的号码",text)
    else:
        time.sleep(60*60)
