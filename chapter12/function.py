from bs4 import BeautifulSoup

def get_VIEWSTATE(response):
    soup = BeautifulSoup(response.text,'lxml')
    _VIEWSTATE=soup.find('input', attrs={'name': '__VIEWSTATE'})['value']
    return _VIEWSTATE
def getGrade(response):
    soup = BeautifulSoup(response.text, "lxml")
    trs = soup.find(id="Datagrid1").findAll("tr")[1:]
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
    return Grades