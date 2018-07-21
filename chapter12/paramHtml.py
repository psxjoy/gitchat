'''
输入验证码获取成绩
'''
import requests
from bs4 import BeautifulSoup
from chapter12.function import get_VIEWSTATE
import time
import os
username='XXXX'
password='XXXX'
url = 'http://XXXXX.XXXXX.edu.cn/(XXXXX)/default_ysdx.aspx'
HEA = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/'
                     '537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36',
       }

response = requests.get(url,HEA)
if response.status_code=='OK':
    soup = BeautifulSoup(response.text,'lxml')
else:
    hash_url = response.headers['Content-Type']
    url = 'http://jwxt.xxxx.edu.cn/('+hash_url+')/default_ysdx.aspx'
    response = requests.get(url,HEA)
    soup = BeautifulSoup(response.text, 'lxml')
viewState = soup.find('input', attrs={'name': '__VIEWSTATE'})['value']
RadioButtonList1 = u"学生".encode('gb2312','replace')
imgUrl = "targeturl"
imgresponse = response.get(imgUrl, stream=True)

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
code = input("验证码是：")
data = {
    '__VIEWSTATE':viewState,
    'TextBox1':username,
    'TextBox2':password,
    'RadioButtonList1':RadioButtonList1,
    'Button1':''
}
web_data = requests.post(url=url,data=data,headers=HEA)
print("成功登陆教务系统！")
baseUrl = 'http://jwxt.XXXX.edu.cn/(11u1r0nxil4tad2fqw315a55)/xs_main.aspx?xh=XXXXXX'
main_title = response.get(baseUrl)
chengji_page = 'http://jwxt.XXXX.edu.cn/(11u1r0nxil4tad2fqw315a55)/xscj_gc.aspx?xh=XXXX&xm=%D6%DC%C3%FA%BD%DC&gnmkdm=N121605'
header = {
    'Referer':'http://jwxt.XXXX.edu.cn/(11u1r0nxil4tad2fqw315a55)/xscj_gc.aspx?xh=XXXX&xm=%D6%DC%C3%FA%BD%DC&gnmkdm=N121605',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36'
}
response = response.get(chengji_page,headers=header)
__VIEWSTATE= get_VIEWSTATE(response)
data1 = {
            "__VIEWSTATE":__VIEWSTATE,
            "ddlXN":"2016-2017",
            "ddlXQ":"2",
            "Button1":""
}
time.sleep(3)
chengji = response.post(chengji_page,data=data1)
chengji.encoding='gb2312'
soup = BeautifulSoup(chengji.content, "lxml",from_encoding="gb18030")
trs = soup.find(id="Datagrid1").findAll("tr")
Grades = []
for tr in trs:
    tds = tr.findAll("td")
    tds = tds[:2] + tds[3:5] + tds[6:9]
    oneGradeKeys = ["year", "term", "name", "type", "credit","gradePonit","grade"]
    oneGradeValues = []
    for td in tds:
        oneGradeValues.append(td.string)
    oneGrade = dict((key, value) for key, value in zip(oneGradeKeys, oneGradeValues))
    Grades.append(oneGrade)
i=0
juage = []
for score in Grades:
    year = ""
    year =year.join(score["year"])
    year = str(year)
    term = ""
    term = term.join(score["term"])
    term = str(term)
    name = ""
    name = name.join(score["name"])
    name = str(name)
    type = ""
    type = type.join(score["type"])
    type = str(type)
    credit = ""
    credit = credit.join(score["credit"])
    credit = str(credit)
    gradePoint = ""
    gradePoint = gradePoint.join(score["gradePonit"])
    gradePoint = str(gradePoint)
    grade = ""
    grade = grade.join(str(score["grade"]))
    grade = str(grade)
    if name not in juage:
        juage.append(name)
    else:
        print("已经存在，不发送短信")

