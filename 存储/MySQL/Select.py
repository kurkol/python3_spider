import pymysql

db = pymysql.connect(host='localhost', user='root', password='password', db='spiders')
cursor = db.cursor()

sql = 'SELECT * FROM students WHERE age >= 18'

try:
    cursor.execute(sql)
    print('Count:', cursor.rowcount)
    #数据条数
    one = cursor.fetchone()
    print('One:', one)
    #第一条数据
    results = cursor.fetchall()
    print('Results:', results)
    #全部数据，因为已经调用过fetchone()指针偏移到第二条数据
    print('Results Type:', type(results))
    for row in results:
        print(row)
except:
    print('Error')


cursor.execute(sql)
row = cursor.fetchone()
while row:
    print('Row:', row)
    row = cursor.fetchone()
#由于fetchall()会将结果全部一起以tuple形式返回，如果数据量大，占用开销非常高
#可以用while逐条取数据
