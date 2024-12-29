import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '3f03f0457cfd6dba2a646b5db28ba1d1'
HEADER = {
    'Content-Type': 'application/json',
    'trainer_token': TOKEN  # Добавляем токен сюда
}

##body_pokemon = {
    ##"name": "DanilkA",
   ## "photo_id": 60
##}

##response = requests.post(url=f'{URL}/pokemons', headers=HEADER, json=body_pokemon)
##print(response.status_code)  # Чтобы увидеть код ответа
##print(response.text)         # Чтобы увидеть текст ответа

# ID покемона, имя которого нужно изменить
pokemon_id = "175020"  # Изменилось на строку

# Новые данные покемона
new_name_body = {
    "pokemon_id": pokemon_id,
    "name": "Danek",  # Укажите новое имя для покемона
    "photo_id": 2  # Вы можете указать новое photo_id, если хотите
}

# Отправка PUT-запроса для изменения имени покемона
response_update = requests.put(url=f'{URL}/pokemons', headers=HEADER, json=new_name_body)

# Проверка ответа на изменение имени покемона
if response_update.status_code == 200:
    updated_pokemon_data = response_update.json()
    print("Имя покемона изменено:", updated_pokemon_data)
else:
    print("Ошибка при изменении имени покемона:", response_update.status_code, response_update.text)

# Код для поймать покемона в покебол
pokemon_to_catch_id = "175020"  # ID покемона, которого нужно поймать в покебол

catch_pokeball_body = {
    "pokemon_id": pokemon_to_catch_id  # Здесь указываем ID покемона
}

# Отправка POST-запроса для ловли покемона
response_catch = requests.post(url=f'{URL}/trainers/add_pokeball', headers=HEADER, json=catch_pokeball_body)

# Проверка ответа на ловлю покемона
if response_catch.status_code == 200:
    catch_result = response_catch.json()
    print("Покемон пойман в покебол:", catch_result)
else:
    print("Ошибка при ловле покемона:", response_catch.status_code, response_catch.text)    
