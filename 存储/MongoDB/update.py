import pymongo

client = pymongo.MongoClient(host='localhost', port=27017)
#client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client.test
collection = db.students

condition = {'name':'kurkol'}
student = collection.find_one(condition)
student['age'] = 25
result = collection.update_one(condition,{'$set':student})
print(result)
print(result.matched_count, result.modified_count)

#多条用update_many()
condition1 = {'age':20}
result = collection.update_many(condition1,{'$inc':{'age':1}})
#'$inc':{'age':1}符合条件的age加1
print(result)
print(result.matched_count, result.modified_count)
