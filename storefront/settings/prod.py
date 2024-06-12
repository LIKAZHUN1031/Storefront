import os
from .common import *
import dj_database_url

DEBUG = False
SECRET_KEY = os.environ['SECRET_KEY']
ALLOWED_HOSTS = ['leebuy-prod-1f52e7c7487e.herokuapp.com']

DATABASES = {
    'default': dj_database_url.config(default=os.getenv('JAWSDB_URL'))  # 查找数据库url的环境变量，它将解析连接字符串返回一个字典
}

REDIS_URL = os.getenv('REDISCLOUD_URL')

CELERY_BROKER_URL = REDIS_URL

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": REDIS_URL,
        'TIMEOUT': 10 * 60,
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}