import pymongo

client = pymongo.MongoClient(host='localhost', port=27017)
#client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client.test
collection = db.students

results = collection.find().sort('name', pymongo.ASCENDING)
#降序DESCENDING
print([result['name'] for result in results])
