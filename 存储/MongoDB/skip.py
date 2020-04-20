import pymongo

client = pymongo.MongoClient(host='localhost', port=27017)
#client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client.test
collection = db.students

results = collection.find().sort('name', pymongo.ASCENDING).skip(1).limit(1)
#skip(1)略过第一个元素,limit(1)取一个元素
print([result['name'] for result in results])

#当数据量非常庞大时大的偏移量可能导致内存溢出，可用如下方式查询
from bson.objectid import ObjectId
result_ = collection.find({'_id':{'$gt':ObjectId('5e8ad7218225689f6d8ffa39')}})
print(result_)
for result in result_:
    print(result)
