from redis import StrictRedis

redis = StrictRedis(host='localhost', port=6379, db=0, password='fy123456')
redis.set('name', 'Bob')
print(redis.get('name'))

redis.hexists("room", "a")