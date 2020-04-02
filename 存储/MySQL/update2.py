import pymysql

db = pymysql.connect(host='localhost', user='root', password='password', db='spiders')
cursor = db.cursor()

data = {
    'id':'20120001',
    'name':'Bob',
    'age':'22'
}

table = 'students'
keys = ', '.join(data.keys())
values = ', '.join(['%s'] * len(data))

sql = 'INSERT INTO {table}({keys}) VALUES ({values}) ON DUPLICATE KEY UPDATE'.format(table=table, keys=keys, values=values)
#如果key已经存在则更新数据;不存在则插入数据

update = ', '.join([" {key} = %s".format(key=key) for key in data])
sql += update
try:
    if cursor.execute(sql, tuple(data.values())*2):
        print('Successful')
        db.commit()
except:
    print('Failed')
    db.rollback()
db.close()
