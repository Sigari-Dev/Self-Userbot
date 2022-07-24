import redis
from config import db_number

database = redis.StrictRedis(
    '127.0.0.1', 6379, db_number, charset='UTF-8', decode_responses=True)


def get_language():
    language = database.get('bot:language')
    if not language:
        set_language('en')
        return 'en'
    return language


def set_language(lang):
    return database.set('bot:language', lang)


def set_action_mode(action):
    return database.set('bot:action', action)


def get_action_mode():
    action = database.get('bot:action')
    if not action:
        set_action_mode('off')
        return 'off'
    return action


def set_action_type(action_type):
    return database.set('bot:actiontype', action_type)


def get_action_type():
    action_type = database.get('bot:actiontype')
    if not action_type:
        set_action_type('typing')
        return 'typing'
    return action_type


def add_to_action_chats(chat_id):
    return database.sadd('bot:actionchats', str(chat_id))

def remove_from_action_chats(chat_id):
    return database.srem('bot:actionchats', str(chat_id))
    
def get_action_chats():
    return database.smembers('bot:actionchats')


def is_in_action_chats(chat_id):
    return database.sismember('bot:actionchats', str(chat_id))

