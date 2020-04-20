import pymongo

client = pymongo.MongoClient(host='localhost', port=27017)
#client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client.test
collection = db.students

result = collection.remove_one({'age':{'$lt':20}})
#多条可用remove_many()
print(result)
