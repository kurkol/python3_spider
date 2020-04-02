import pymysql

db = pymysql.connect(host='localhost', user='root', password='password', db='spiders')
cursor = db.cursor()

table = 'students'
condition = 'age >= 21'

sql = 'DELETE FROM {table} WHERE {condition}'.format(table=table, condition=condition)

try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()
db.close()
