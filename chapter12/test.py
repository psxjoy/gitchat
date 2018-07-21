'''
用于插入数据
'''

import pymysql
db = pymysql.connect("localhost","root","654321","mysql" )
cursor = db.cursor()

def insert_info(year, term, name, type, credit,gradePonit,grade):
    sql = "INSERT INTO score(year_, term_, name_, type_, credit_,gradePoint_,grade_) VALUES('"+str(year)+"','"+str(term)+"','"+str(name)+"','"+str(type)+"','"+str(credit)+"','"+str(gradePonit)+"','"+str(grade)+"')"
    print(sql)
    cursor.execute(sql)
    db.commit()
def insert_info(year, term, name, type, credit,gradePonit,grade):
    sql = "INSERT INTO score(year_, term_, name_, type_, credit_,gradePoint_,grade_) VALUES('"+str(year)+"','"+str(term)+"','"+str(name)+"','"+str(type)+"','"+str(credit)+"','"+str(gradePonit)+"','"+str(grade)+"')"
    print(sql)
    cursor.execute(sql)
    db.commit()