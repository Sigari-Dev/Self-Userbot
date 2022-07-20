import redis
from config import db_number

database = redis.StrictRedis('127.0.0.1', 6379, db_number)

def get_language():
    language = database.get('bot:language')
    if not language:
        set_language('en')
        return 'en'
    return language.decode()

def set_language(lang):
    return database.set('bot:language', lang)