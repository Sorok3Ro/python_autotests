import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'd4d4bee34d2c9a12ad4c92b2ed1c70ca'
HEADER = {'Content-Type' : 'application/json', "trainer_token": TOKEN,}

body_create_pokemons = {

    "name": "generate",
    "photo_id": -1
}


response_craete_pokemons = requests.post(url = f'{URL}/pokemons', headers = HEADER,  json = body_create_pokemons)
convert_respose = response_craete_pokemons.json()
pokemon_id = response_craete_pokemons.json()["id"]
print(convert_respose)


body_add_in_pockeball = {
    
    "pokemon_id": pokemon_id

}
response_add_in_pockeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER,  json = body_add_in_pockeball)
convert_respose1 = response_add_in_pockeball.json()
print(convert_respose1)

response_pokemons = requests.get(url = f'{URL}/pokemons',params = {'in_pokeball' : '1'}, headers = HEADER)
enemy_id = response_pokemons.json()["data"][5]["id"]
print(enemy_id)

body_batle = {

    "attacking_pokemon": pokemon_id,
    "defending_pokemon": enemy_id
}

respose_batle = requests.post(url = f'{URL}/battle', headers = HEADER, json = body_batle)
convert_respose3 = respose_batle.json()
print(convert_respose3)