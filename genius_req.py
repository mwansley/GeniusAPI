# access GeniusAPI searching for song information
import requests
import logging
import pytest
import creds


TOKEN = creds.TOKEN
BASE_URL = 'https://api.genius.com/oauth/authorize'
title = input("What song lyrics are you looking for? ")
artist = input("Who does that song? ")
request_url = f"{BASE_URL}?token={TOKEN}&q={title},{artist}"

response = requests.get(request_url)

if(response.status_code != 200):
    raise Exception("Could not authorize!")
else:
    print("Connected!!")
data = response.json()

print(data)



