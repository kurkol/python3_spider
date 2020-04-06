import pymongo

client = pymongo.MongoClient(host='localhost', port=27017)
client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client.test
collection = db.students

result = collection.find_one({'name':'Bob'})
print(type(result))
print(result)
#单条查找

from bson.objectid import ObjectId
result1 = collection.find_one({'_id':ObjectId('5e8ad7218225689f6d8ffa3b')})
print(result1)
#通过ObjectId查找

result2 = collection.find({'age':20})
print(result2)
for result in result2:
    print(result)
#find多条查找

result3 = collection.find({'age':{'$gt':19}})
print(result3)
for result in result3:
    print(result)
#条件查找
#$lt：小于，$gt:大于,$lte:小于等于,$gte:大于等于,$ne:不等于
#$in:在范围内,$nin:在范围外————,{'$nin':[20,23]}
