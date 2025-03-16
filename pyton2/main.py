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

body_put = {
    
    "pokemon_id": pokemon_id,
    "name": "Асура",
    "photo_id": 2

}

response_put = requests.put(url = f'{URL}/pokemons', headers = HEADER,  json = body_put)
convert_respose1 = response_put.json()
print(convert_respose1)


body_add_in_pockeball = {
    
    "pokemon_id": pokemon_id

}
response_add_in_pockeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER,  json = body_add_in_pockeball)
convert_respose2 = response_add_in_pockeball.json()
print(convert_respose2)

body_delete_pockeball = {

    "pokemon_id": pokemon_id
}
response_delete_pockeball = requests.put(url = f'{URL}/trainers/delete_pokeball', headers = HEADER,  json = body_delete_pockeball)
convert_respose3 = response_delete_pockeball.json()
print(convert_respose3)

body_knockout = {
    
    "pokemon_id": pokemon_id

}
response_knockout = requests.post(url = f'{URL}/pokemons/knockout', headers = HEADER,  json = body_knockout)
convert_response4 = response_knockout.json()
print(convert_response4)