"""
Testes automatizados para a API Star Wars
"""
import pytest
import sys
import os

# Adiciona o diretório src ao path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from main import app
from swapi_client import SWAPIClient
from utils import extract_id_from_url, format_film_data, sort_results


@pytest.fixture
def client():
    """Fixture para cliente de teste do Flask"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_home_endpoint(client):
    """Testa o endpoint raiz"""
    response = client.get('/')
    assert response.status_code == 200
    data = response.get_json()
    assert 'message' in data
    assert 'endpoints' in data
    assert data['version'] == '1.0.0'


def test_get_all_films(client):
    """Testa listagem de todos os filmes"""
    response = client.get('/api/films')
    assert response.status_code == 200
    data = response.get_json()
    assert 'count' in data
    assert 'results' in data
    assert data['count'] > 0


def test_get_film_by_id(client):
    """Testa busca de filme por ID"""
    response = client.get('/api/films/1')
    assert response.status_code == 200
    data = response.get_json()
    assert 'title' in data
    assert 'director' in data
    assert 'episode_id' in data


def test_get_all_people(client):
    """Testa listagem de todos os personagens"""
    response = client.get('/api/people')
    assert response.status_code == 200
    data = response.get_json()
    assert 'count' in data
    assert 'results' in data


def test_get_person_by_id(client):
    """Testa busca de personagem por ID"""
    response = client.get('/api/people/1')
    assert response.status_code == 200
    data = response.get_json()
    assert 'name' in data
    assert 'height' in data


def test_get_all_planets(client):
    """Testa listagem de todos os planetas"""
    response = client.get('/api/planets')
    assert response.status_code == 200
    data = response.get_json()
    assert 'count' in data
    assert 'results' in data


def test_get_planet_by_id(client):
    """Testa busca de planeta por ID"""
    response = client.get('/api/planets/1')
    assert response.status_code == 200
    data = response.get_json()
    assert 'name' in data
    assert 'climate' in data


def test_get_all_starships(client):
    """Testa listagem de todas as naves"""
    response = client.get('/api/starships')
    assert response.status_code == 200
    data = response.get_json()
    assert 'count' in data
    assert 'results' in data


def test_films_with_sort(client):
    """Testa ordenação de filmes"""
    response = client.get('/api/films?sort_by=title&order=asc')
    assert response.status_code == 200
    data = response.get_json()
    assert data['count'] > 0


def test_people_with_search(client):
    """Testa busca de personagens"""
    response = client.get('/api/people?search=Luke')
    assert response.status_code == 200
    data = response.get_json()
    assert data['count'] > 0


def test_extract_id_from_url():
    """Testa extração de ID de URL"""
    url = "https://swapi.dev/api/films/1/"
    assert extract_id_from_url(url) == 1


def test_sort_results():
    """Testa função de ordenação"""
    data = [
        {"name": "C", "value": 3},
        {"name": "A", "value": 1},
        {"name": "B", "value": 2}
    ]
    sorted_data = sort_results(data, "name", "asc")
    assert sorted_data[0]["name"] == "A"
    assert sorted_data[2]["name"] == "C"


def test_swapi_client():
    """Testa cliente SWAPI"""
    client = SWAPIClient()
    assert client.BASE_URL == "https://swapi.dev/api"
    
    # Testa busca de filmes
    films = client.get_all_films()
    assert 'results' in films or 'error' in films
