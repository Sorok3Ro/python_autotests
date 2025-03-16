import requests
import pytest
URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'd4d4bee34d2c9a12ad4c92b2ed1c70ca'
HEADER = {'Content-Type' : 'application/json', "trainer_token": TOKEN,}
TRAINER_ID = '24830'

def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID}, headers = HEADER)
    assert response.status_code == 200
def test_name_trainers():
    response_name = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID}, headers = HEADER)
    assert response_name.json()["data"][0]["trainer_name"]== 'Oliver Queen'