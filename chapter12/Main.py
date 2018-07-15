# coding=gbk
import requests
from bs4 import BeautifulSoup
from chapter12.vertify_code import get_view
import time
from chapter12.test import insert_info
username='XXXXXX'
password='XXXXXX'
url = 'http://XXX.XXXX.edu.cn/(11u1r0nxil4tad2fqw315a55)/default_ysdx.aspx'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36",
}
s = requests.session()
response = s.get(url)
soup = BeautifulSoup(response.text,'lxml')
viewState = soup.find('input', attrs={'name': '__VIEWSTATE'})['value']
RadioButtonList1 = u"学生".encode('gb2312','replace')
data = {
    '__VIEWSTATE':viewState,
    'TextBox1':username,
    'TextBox2':password,
    'RadioButtonList1':RadioButtonList1,
    'Button1':''
}
web_data = s.post(url=url,data=data)
print("成功登陆教务系统！")
baseUrl = 'http://jwxt.XXXX.edu.cn/(11u1r0nxil4tad2fqw315a55)/xs_main.aspx?xh=1141314818'
main_title = s.get(baseUrl)
chengji_page = 'http://jwxt.XXXX.edu.cn/(11u1r0nxil4tad2fqw315a55)/xscj_gc.aspx?xh=1141314818&xm=%D6%DC%C3%FA%BD%DC&gnmkdm=N121605'
header = {
    'Referer':'http://jwxt.XXXX.edu.cn/(11u1r0nxil4tad2fqw315a55)/xscj_gc.aspx?xh=1141314818&xm=%D6%DC%C3%FA%BD%DC&gnmkdm=N121605',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36'


}
response = s.get(chengji_page,headers=header)
__VIEWSTATE= get_view(response)
data1 = {
            "__VIEWSTATE":__VIEWSTATE,
            "ddlXN":"2016-2017",
            "ddlXQ":"2",
            "Button1":""
}
time.sleep(3)
chengji = s.post(chengji_page,data=data1)
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
        send_mail(year, term, name, type, credit, gradePoint, grade)
        juage.append(name)
    else:
        print("已经存在，不发送短信")

    int result = select_info(name)
    if result!=0:
        time.sleep(60*60)
    else:
        send_mail(year,term,name,type,credit,gradePoint,grade)
    insert_info(year,term,name,type,credit,gradePoint,grade)
