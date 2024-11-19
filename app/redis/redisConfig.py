import os
import redis
from dotenv import load_dotenv

load_dotenv()
redis_host = os.getenv("REDIS_DB_CONN")
redis_port = os.getenv("REDIS_DB_PORT")
redis_password = os.getenv("REDIS_DB_PASSWORD")
# print(redis_port,redis_host,redis_password)


def get_redis_database():
    try:
        print(f"Pinging Redis...")
        r = redis.Redis(host=redis_host, port=redis_port, password=redis_password)
        r.ping()  # Check connection
        print("Redis Connected...")
        return r
    except redis.ConnectionError as e:
        print(f"Redis connection error: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None
