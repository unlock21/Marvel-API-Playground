from hashlib import md5
from os import environ
import requests
import time
import json

from marvel.models import Character, Comic

apiPublicKey = environ.get('MARVEL_PUBLIC_KEY')
apiPrivateKey = environ.get('MARVEL_PRIVATE_KEY')
baseUrl = "http://gateway.marvel.com"

def getCharacters():
  # Parts to construct call
  ts = str(time.time()).split('.')[0]

  # MD5 Hash ts, apiPublicKey and apiPrivateKey for API auth
  auth = md5((ts+apiPrivateKey+apiPublicKey).encode()).hexdigest()

  # Fully constructed URL
  apiUrl = f"{baseUrl}/v1/public/characters?ts={ts}&apikey={apiPublicKey}&hash={auth}"

  response = requests.get(apiUrl)

  if not response.ok:
    print("Marvel API - CHARACTERS - NO GO")
  else:
    print("Marvel API - CHARACTERS - GO")

  saveCharacters(response.json())

def saveCharacters(responseJson):
  characters = responseJson["data"]["results"]
  for character in characters:
    characterModel = Character(id=character["id"], name=character["name"], thumbnail=(character["thumbnail"]["path"] + '.' + character["thumbnail"]["extension"]))
    characterModel.save()
    for comic in character["comics"]["items"]:
      comicModel = Comic(name=comic["name"], character=characterModel)
      comicModel.save()