import pymysql

id = '20200330'
user = 'Kurkol'
age = 20

db = pymysql.connect(host='localhost', user='root', password='password', db='spiders')
cursor = db.cursor()

sql = 'INSERT INTO students (id , name, age) values(%s, %s, %s)'
#构造插入的sql语句

try:
    cursor.execute(sql, (id, user, age))
    #values值用元组传入
    db.commit()
    #commit()之后数据才提交到数据库执行
except:
    db.rollback()
    #执行失败，数据回滚
db.close()
