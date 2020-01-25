import redis

pool = redis.ConnectionPool()
r = redis.Redis(connection_pool=pool)

pipe = r.pipeline()
pipe.set('fans', 50)
pipe.incr('fans')
pipe.incrby('fans', 50)
result = pipe.execute()
print(result)

pipe.get('fans')
pipe.get('pwd')
result = pipe.execute()

print(result)
