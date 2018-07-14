import requests
from bs4 import BeautifulSoup
username='1141314818'
password='psxjoy1995'
url = 'http://jwxt.hyit.edu.cn/(g4a4tc45mpgtlm45ummhkmmu)/default_ysdx.aspx'
HEA = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/'
                     '537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36',
       }

response = requests.get(url,HEA)
if response.status_code=='OK':
    soup = BeautifulSoup(response.text,'lxml')
else:
    hash_url = response.headers['Content-Type']
    url = 'http://jwxt.hyit.edu.cn/('+hash_url+')/default_ysdx.aspx'
    response = requests.get(url,HEA)
    soup = BeautifulSoup(response.text, 'lxml')
viewState = soup.find('input', attrs={'name': '__VIEWSTATE'})['value']
RadioButtonList1 = u"学生".encode('gb2312','replace')
imgUrl = "targeturl"
imgresponse = s.get(imgUrl, stream=True)

image = imgresponse.content
DstDir = os.getcwd()+"\\"
print("保存验证码到："+DstDir+"code.jpg"+"\n")
try:
    with open(DstDir+"code.jpg" ,"wb") as jpg:
        jpg.write(image)
except IOError:
    print("IO Error\n")
finally:
    jpg.close
#手动输入验证码
code = raw_input("验证码是：")
data = {
    '__VIEWSTATE':viewState,
    'TextBox1':username,
    'TextBox2':password,
    'RadioButtonList1':RadioButtonList1,
    'Button1':''
}
web_data = requests.post(url=url,data=data,headers=HEA)
print(web_data.text)