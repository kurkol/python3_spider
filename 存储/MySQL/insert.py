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

#作为一个事物应当具有ACID特性
#atomicity,原子性，要么都做要么不做
#consistency,一致性，从一个一致性状态到另一个一致性状态，如总量不变的样本
#isolation,隔离性，事物之间不互相干扰
#durability,持久性，事物一旦提交对数据库的改变时永久的

#数据库标准操作可以写为：
#try:
#   cursor.execute(sql)
#   db.commit()
#except:
#   db.rollback()
