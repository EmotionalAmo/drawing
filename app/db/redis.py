import redis

# 连接到Redis服务器
mail_redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

live_redis_client = redis.StrictRedis(host='localhost', port=6379, db=1)
