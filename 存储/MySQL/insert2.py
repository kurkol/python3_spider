import pymysql

db = pymysql.connect(host='localhost', user='root', password='password', db='spiders')
cursor = db.cursor()

#构造动态sql语句
data = {
    'id':'20200330',
    'name':'kurkol',
    'age':20
}
table = 'students'
keys = ', '.join(data.keys())
values = ', '.join(['%s'] * len(data))
sql = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(table=table, keys=keys, values=values)


try:
    if cursor.execute(sql, tuple(data.values())):
        print('Successfull')
        db.commit()
except:
    print('Failed')
    db.rollback()
db.close()
