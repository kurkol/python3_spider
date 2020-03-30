import pymysql

db = pymysql.connect(host='localhost',user='root',password='password',port=3306)
#host传人mysql运行IP，user用户名，password密码，port端口默认3306

cursor=db.cursor()
#调用cursor()获得mysql操作游标

cursor.execute('SELECT VERSION()')
data = cursor.fetchone()
#获得当前版本，fetchone()获得第一条数据
print('Database version:', data)

cursor.execute("CREATE DATABASE spiders DEFAULT CHARACTER SET utf8")
#新建一个名为sipders数据库，默认编码为UTF-8
db.close()
