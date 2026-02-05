# Funções utilitárias para processamento de dados
from typing import List, Dict, Any
from functools import wraps
import time


def extract_id_from_url(url: str) -> int:
    # Extrai o ID de uma URL da SWAPI
    try:
        return int(url.rstrip('/').split('/')[-1])
    except (ValueError, IndexError):
        return 0


def format_film_data(film: Dict) -> Dict:
    # Formata dados de um filme
    return {
        "id": extract_id_from_url(film.get("url", "")),
        "title": film.get("title"),
        "episode_id": film.get("episode_id"),
        "opening_crawl": film.get("opening_crawl"),
        "director": film.get("director"),
        "producer": film.get("producer"),
        "release_date": film.get("release_date"),
        "characters_count": len(film.get("characters", [])),
        "planets_count": len(film.get("planets", [])),
        "starships_count": len(film.get("starships", []))
    }


def format_person_data(person: Dict) -> Dict:
    # Formata dados de um personagem
    return {
        "id": extract_id_from_url(person.get("url", "")),
        "name": person.get("name"),
        "height": person.get("height"),
        "mass": person.get("mass"),
        "hair_color": person.get("hair_color"),
        "skin_color": person.get("skin_color"),
        "eye_color": person.get("eye_color"),
        "birth_year": person.get("birth_year"),
        "gender": person.get("gender"),
        "homeworld": person.get("homeworld"),
        "films_count": len(person.get("films", []))
    }


def format_planet_data(planet: Dict) -> Dict:
    # Formata dados de um planeta
    return {
        "id": extract_id_from_url(planet.get("url", "")),
        "name": planet.get("name"),
        "rotation_period": planet.get("rotation_period"),
        "orbital_period": planet.get("orbital_period"),
        "diameter": planet.get("diameter"),
        "climate": planet.get("climate"),
        "gravity": planet.get("gravity"),
        "terrain": planet.get("terrain"),
        "surface_water": planet.get("surface_water"),
        "population": planet.get("population"),
        "residents_count": len(planet.get("residents", []))
    }


def format_starship_data(starship: Dict) -> Dict:
    # Formata dados de uma nave
    return {
        "id": extract_id_from_url(starship.get("url", "")),
        "name": starship.get("name"),
        "model": starship.get("model"),
        "manufacturer": starship.get("manufacturer"),
        "cost_in_credits": starship.get("cost_in_credits"),
        "length": starship.get("length"),
        "max_atmosphering_speed": starship.get("max_atmosphering_speed"),
        "crew": starship.get("crew"),
        "passengers": starship.get("passengers"),
        "cargo_capacity": starship.get("cargo_capacity"),
        "consumables": starship.get("consumables"),
        "hyperdrive_rating": starship.get("hyperdrive_rating"),
        "MGLT": starship.get("MGLT"),
        "starship_class": starship.get("starship_class")
    }


def sort_results(results: List[Dict], sort_by: str, order: str = "asc") -> List[Dict]:
    # Ordena resultados por um campo específico
    reverse = order.lower() == "desc"
    try:
        return sorted(results, key=lambda x: x.get(sort_by, ""), reverse=reverse)
    except TypeError:
        return results


def measure_time(func):
    # Mede quanto tempo uma função leva para executar
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} executado em {end - start:.2f}s")
        return result
    return wrapper
