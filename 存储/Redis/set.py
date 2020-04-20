from redis import StrictRedis

redis = StrictRedis(host='localhost', port=6379, db=0, password='password')
redis.set('name', 'kurkol')
print(redis.get('name'))
#其他命令可查表
