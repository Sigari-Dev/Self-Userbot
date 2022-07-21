import requests
import re
import datetime
from base64 import b64encode


def set_score_gamee(link, score):
    link = re.search("(\/game-bot\/\w+\-[0-9a-fA-F]+)", link).group(1)
    score = str(score)
    
    headers = {
        'authority': 'api.service.gameeapp.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'client-language': 'en',
        'content-type': 'text/plain;charset=UTF-8',
        'origin': 'https://prizes.gamee.com',
        'referer': 'https://prizes.gamee.com/',
        'sec-ch-ua': '" Not;A Brand";v="99", "Microsoft Edge";v="103", "Chromium";v="103"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.62',
        'x-install-uuid': '9729b743-3543-4dd9-b2f7-b8bf27d34fc1',
        }
    
    data = \
        '{"jsonrpc":"2.0","id":"game.getWebGameplayDetails","method":"game.getWebGameplayDetails","params":{"gameUrl":"' \
        + link + '"}}'
    result = requests.post('https://api.service.gameeapp.com/',
                           headers=headers, data=data).json()['result']

    game_id = result['game']['id']
    game_name = result['game']['name']
    release_number = result['game']['release']['number']

    data = \
        '{"jsonrpc":"2.0","id":"user.authentication.botLogin","method":"user.authentication.botLogin","params":{"botName":"telegram","botGameUrl":"' \
        + link + '","botUserIdentifier":null}}'
    user = requests.post('https://api.service.gameeapp.com/',
                         headers=headers, data=data).json()
    #print(user)
    token = user['result']['tokens']['authenticate']
    authenticated_headers = headers
    authenticated_headers['authorization'] = 'Bearer {}'.format(token)

    data = \
        '[{"jsonrpc":"2.0","id":"leaderboards.getWebByGame","method":"leaderboards.getWebByGame","params":{"pagination":{"limit":1,"offset":0},"type":"global","gameUrl":"/game-bot/motofx2-d0f8e36439fcdde791952ff380ea7a94d76969c2"}},{"jsonrpc":"2.0","id":"leaderboards.getWebSurroundingByGame","method":"leaderboards.getWebSurroundingByGame","params":{"gameUrl":"/game-bot/motofx2-d0f8e36439fcdde791952ff380ea7a94d76969c2"}}]'
    gameState = requests.post('https://api.service.gameeapp.com/',
                              headers=authenticated_headers, data=data).json()
    if len(gameState) >= 1:
        if 'saveStateData' in gameState[1]['result']:
            saveStateData = gameState[1]['result']['saveStateData']
        else:
            saveStateData = ''

    date = datetime.datetime.now().strftime('%Y-%M-%dT%X+04:30')
    play_time = int(int(score) * 2.5)
    if play_time > 43200: play_time = 43200
    play_time = str(play_time)
    checksum = score + ':' + play_time + ':' + link \
        + ':{}:crmjbjm3lczhlgnek9uaxz2l9svlfjw14npauhen'
    checksum = b64encode(checksum.encode()).decode()
    checksum = requests.get('http://mandofski1.pythonanywhere.com/makeGameeChecksum/{}'.format(checksum)).text
    data = \
        '{"jsonrpc":"2.0","id":"game.saveWebGameplay","method":"game.saveWebGameplay","params":{"gameplayData":{"gameId":' \
        + str(game_id) + ',"score":' + score + ',"playTime":' \
        + play_time + ',"gameUrl":"' + link \
        + '","metadata":{"gameplayId":162},"releaseNumber":' \
        + str(release_number) + ',"gameStateData":"{}","createdTime":"' \
        + date + '","checksum":"' + checksum \
        + '","replayVariant":null,"replayData":null,"replayDataChecksum":null,"isSaveState":false,"gameplayOrigin":"game"}}}'

    print(requests.post('https://api.service.gameeapp.com/',
                             headers=authenticated_headers, data=data).json())