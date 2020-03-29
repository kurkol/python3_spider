import json

str = '''
[{
    "name": "Bob",
    "gender": "male",
    "birthday": "1992-10-18"
},{
    "name": "Selina",
    "gender": "female",
    "birthday": "1995-10-18"
}]
'''
#JSON字符串表示必须用双引号，否则loads()方法会出错

#将文本字符串转为JSON对象，再用索引获取
print(type(str))
data = json.loads(str)
print(data)
print(type(data))


print(data[0].get('name'))
#也可print(data[0]['name']),最好用get，如果key不存在不会报错，返回None，还可设置默认值
print(data[0].get('age'))
print(data[0].get('age',28))

#从.json文件读取
with open('data.json', 'r') as file:
    str = file.read()
    data = json.loads(str)
    print(data)
