import pymysql

db = pymysql.connect(host='localhost', user='root', password='password', port=3306, db='spiders')
#打开mysql选中spiders数据库
cursor = db.cursor()

sql = 'CREATE TABLE IF NOT EXISTS students (id VARCHAR(255) NOT NULL, name VARCHAR(255) NOT NULL, age INT NOT NULL, PRIMARY KEY (id))'
#新建表

cursor.execute(sql)
db.close()
