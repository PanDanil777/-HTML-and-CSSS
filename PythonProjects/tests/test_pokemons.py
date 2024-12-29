'''import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '3f03f0457cfd6dba2a646b5db28ba1d1'
HEADER = {'Content-Type': 'application/json', 'trainer_token':TOKEN}
TRAINER_ID = '12423'

def test_status_code():
    response = requests.get(url=f'{URL}/pokemons', params={'trainer_id' : TRAINER_ID} )
    assert response.status_code == 200

def test_part_of_responce():
    response_get= requests.post(url=f'{URL}/pokemons', params={'trainer_id' : TRAINER_ID} )
    assert response_get.json()['name'] == '''

import requests
import pytest

# Задаем URL и заголовки
URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '3f03f0457cfd6dba2a646b5db28ba1d1'
HEADER = {'Content-Type': 'application/json', 'trainer_token': TOKEN}

# Замените на ваш реальный ID и имя тренера
TRAINER_ID = '12423а'  # Вставьте ваш ID тренера
TRAINER_NAME = 'MegaMAN'  # Вставьте ваше имя тренера

def test_get_trainer_status_code():
    response = requests.get(url=f'{URL}/trainers', params={'trainer_id': TRAINER_ID}, headers=HEADER)
    assert response.status_code == 200

def test_get_trainer_info():
    response = requests.get(url=f'{URL}/trainers', params={'trainer_id': TRAINER_ID}, headers=HEADER)
    assert response.status_code == 200  # Проверка, что код ответа 200
    
    trainer_data = response.json()  # Получаем данные в формате JSON
    
    # Проверка наличия 'trainer_id' и 'name' в ответе
    assert 'trainer_id' in trainer_data  # Проверяем, что 'trainer_id' присутствует
    assert trainer_data['trainer_id'] == TRAINER_ID  # Проверяем, что ID соответствует вашему ID тренера
    
    assert 'name' in trainer_data  # Проверяем, что 'name' присутствует
    assert trainer_data['name'] == TRAINER_NAME  # Проверяем, что имя соответствует вашему имени тренера

if __name__ == "__main__":
    pytest.main()
