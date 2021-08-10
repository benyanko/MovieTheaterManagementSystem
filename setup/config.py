import os

DEBUG = True

PORT = os.environ['PORT'] or '5000'
POSTGRES_USER = os.environ["POSTGRES_USER"] or 'postgres'
POSTGRES_PASSWORD = os.environ["POSTGRES_PASSWORD"] or 'postgres'
POSTGRES_HOSTNAME = os.environ["POSTGRES_HOSTNAME"] or 'postgres'
POSTGRES_PORT = os.environ["POSTGRES_PORT"] or '5432'
POSTGRES_DB = os.environ["POSTGRES_DB"] or 'postgres'
SQLALCHEMY_DATABASE_URI = (f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOSTNAME}:{POSTGRES_PORT}/{POSTGRES_DB}")
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = os.environ['SECRET_KEY'] or 'planck'
CACHE_TYPE = os.environ['CACHE_TYPE'] or 'redis'
CACHE_REDIS_HOST = os.environ['CACHE_REDIS_HOST'] or 'redis'
CACHE_REDIS_PORT = os.environ['CACHE_REDIS_PORT'] or '6379'
CACHE_REDIS_DB = os.environ['CACHE_REDIS_DB'] or '0'
CACHE_REDIS_URL = os.environ['CACHE_REDIS_URL'] or 'redis://redis:6379/0'
CACHE_DEFAULT_TIMEOUT = os.environ['CACHE_DEFAULT_TIMEOUT'] or '500'
TIMEOUT = (60 * 5)

