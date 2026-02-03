"""
Cliente para interagir com a API SWAPI (Star Wars API)
"""
import requests
from typing import Dict, List, Optional
from functools import lru_cache


class SWAPIClient:
    """Cliente para consumir a API do Star Wars"""
    
    BASE_URL = "https://swapi.dev/api"
    
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'StarWars-API-Client/1.0'
        })
    
    def _make_request(self, endpoint: str, params: Optional[Dict] = None) -> Dict:
        """Faz requisição à API com tratamento de erros"""
        try:
            url = f"{self.BASE_URL}/{endpoint}/"
            response = self.session.get(url, params=params, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}
    
    @lru_cache(maxsize=128)
    def get_all_films(self) -> Dict:
        """Retorna todos os filmes"""
        return self._make_request("films")
    
    @lru_cache(maxsize=128)
    def get_film_by_id(self, film_id: int) -> Dict:
        """Retorna um filme específico por ID"""
        return self._make_request(f"films/{film_id}")
    
    def search_films(self, search: str) -> Dict:
        """Busca filmes por título"""
        return self._make_request("films", params={"search": search})
    
    @lru_cache(maxsize=128)
    def get_all_people(self) -> Dict:
        """Retorna todos os personagens"""
        return self._make_request("people")
    
    @lru_cache(maxsize=128)
    def get_person_by_id(self, person_id: int) -> Dict:
        """Retorna um personagem específico por ID"""
        return self._make_request(f"people/{person_id}")
    
    def search_people(self, search: str) -> Dict:
        """Busca personagens por nome"""
        return self._make_request("people", params={"search": search})
    
    @lru_cache(maxsize=128)
    def get_all_planets(self) -> Dict:
        """Retorna todos os planetas"""
        return self._make_request("planets")
    
    @lru_cache(maxsize=128)
    def get_planet_by_id(self, planet_id: int) -> Dict:
        """Retorna um planeta específico por ID"""
        return self._make_request(f"planets/{planet_id}")
    
    def search_planets(self, search: str) -> Dict:
        """Busca planetas por nome"""
        return self._make_request("planets", params={"search": search})
    
    @lru_cache(maxsize=128)
    def get_all_starships(self) -> Dict:
        """Retorna todas as naves"""
        return self._make_request("starships")
    
    @lru_cache(maxsize=128)
    def get_starship_by_id(self, starship_id: int) -> Dict:
        """Retorna uma nave específica por ID"""
        return self._make_request(f"starships/{starship_id}")
    
    def search_starships(self, search: str) -> Dict:
        """Busca naves por nome"""
        return self._make_request("starships", params={"search": search})
