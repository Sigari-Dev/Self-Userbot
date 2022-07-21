from random import choice

def symbolize(message):
    symbol = choice(["❋", "●"])
    return f'{symbol} ' + message

def font(message):
    pass