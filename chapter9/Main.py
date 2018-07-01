from chapter9.crwal_info import get_info
from chapter9.send_sms import send_sms

if __name__ == '__main__':
    url = '	http://api.map.baidu.com/telematics/v3/weather?location=杭州&output=json&ak=你的AK值'
    text = get_info(url)
    send_sms("要发送的手机号码","Twilio提供的号码",text)