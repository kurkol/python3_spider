import pymongo

client = pymongo.MongoClient(host='localhost', port=27017)
//client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client.test
collection = db.students

students = {
    'id':'20200406',
    'name':'kurkol',
    'age':20,
    'gerder':'male'
}

students1 = {
    'id':'20170101',
    'name':'Jordan',
    'age':20,
    'gerder':'male'
}

students2 = {
    'id':'202002062',
    'name':'Bob',
    'age':20,
    'gerder':'male'
}

result = collection.insert_one(students)
print(result)
print(result.inserted_id)
#插入单条

result1 = collection.insert_many([students1, students2])
print(result1)
print(result1.inserted_ids)
#插入多条
