import os
import redis
redis_host=os.getenv('REDIS_DB_CONN')
redis_port=os.getenv('REDIS_DB_PORT')
redis_password=os.getenv('REDIS_DB_PASSWORD')
# print(redis_port,redis_host,redis_password)

def get_redis_database():
    try:
        r=redis.Redis(host=redis_host,port=redis_port,password=redis_password)
        # print('Redis Connected...')
        return r
    except Exception as e:
        print(e)
        return None