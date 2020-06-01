from hashlib import md5
from os import environ
import requests
import time

from marvel.models import Character, Comic

apiPublicKey = environ.get('MARVEL_PUBLIC_KEY')
apiPrivateKey = environ.get('MARVEL_PRIVATE_KEY')
baseUrl = 'http://gateway.marvel.com'

def getCharacters():
    # string timestamp
    ts = str(time.time()).split('.')[0]
    # MD5 Hash ts, apiPublicKey and apiPrivateKey for API auth
    auth = md5((ts+apiPrivateKey+apiPublicKey).encode()).hexdigest()
    # How many records to return per call
    recordCountPerCall = 100

    i = 0
    while True:
        # Fully constructed URL
        apiUrl = f'{baseUrl}/v1/public/characters?ts={ts}&apikey={apiPublicKey}&hash={auth}&limit={recordCountPerCall}&offset={i * recordCountPerCall}'

        try:
            response = requests.get(apiUrl)
        except Exception as e:
            print('Marvel API request failed!', e)
            break

        print('Run: ' + str(i))
        if response.ok:
            saveCharacters(response.json())
        # Check if there are more API calls required
        if i * recordCountPerCall > response.json()['data']['total']:
            break
        i = i + 1

def saveCharacters(responseJson):
    characters = responseJson['data']['results']
    for character in characters:
        characterModel = Character(id=character['id'], name=character['name'], thumbnail=(character['thumbnail']['path'] + '.' + character['thumbnail']['extension']))
        characterModel.save()
        for comic in character['comics']['items']:
            comicModel = Comic(name=comic['name'], character=characterModel)
            comicModel.save()