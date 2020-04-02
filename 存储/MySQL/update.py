import pymysql

db = pymysql.connect(host='localhost', user='root', password='password', db='spiders')
cursor = db.cursor()

sql = 'UPDATE students SET age = %s Where name = %s'
#基本的更新

try:
    cursor.execute(sql, (25,'kurkol'))
    db.commit()
except:
    db.rollback()
db.close()

