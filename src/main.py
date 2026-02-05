# API Star Wars - Endpoint principal para Google Cloud Functions
from flask import Flask, request, jsonify
from flask_cors import CORS
from swapi_client import SWAPIClient
from utils import (
    format_film_data,
    format_person_data,
    format_planet_data,
    format_starship_data,
    sort_results
)

app = Flask(__name__)
CORS(app)

# Inicializa o cliente SWAPI
swapi = SWAPIClient()


@app.route('/')
def home():
    # Endpoint raiz com informacoes da API
    return jsonify({
        "message": "Star Wars API - PowerOfData",
        "version": "1.0.0",
        "endpoints": {
            "films": "/api/films",
            "people": "/api/people",
            "planets": "/api/planets",
            "starships": "/api/starships"
        },
        "documentation": "https://github.com/andre-zana/starwars-api"
    })


@app.route('/api/films', methods=['GET'])
def get_films():
    """
    Retorna filmes com filtros opcionais
    Query params: search, sort_by, order
    """
    search = request.args.get('search')
    sort_by = request.args.get('sort_by', 'episode_id')
    order = request.args.get('order', 'asc')
    
    if search:
        data = swapi.search_films(search)
    else:
        data = swapi.get_all_films()
    
    if 'error' in data:
        return jsonify({"error": data['error']}), 500
    
    results = data.get('results', [])
    formatted_results = [format_film_data(film) for film in results]
    
    if sort_by:
        formatted_results = sort_results(formatted_results, sort_by, order)
    
    return jsonify({
        "count": len(formatted_results),
        "results": formatted_results
    })


@app.route('/api/films/<int:film_id>', methods=['GET'])
def get_film_by_id(film_id):
    # Retorna um filme especifico por ID
    data = swapi.get_film_by_id(film_id)
    
    if 'error' in data:
        return jsonify({"error": data['error']}), 404
    
    return jsonify(format_film_data(data))


@app.route('/api/people', methods=['GET'])
def get_people():
    """
    Retorna personagens com filtros opcionais
    Query params: search, sort_by, order
    """
    search = request.args.get('search')
    sort_by = request.args.get('sort_by', 'name')
    order = request.args.get('order', 'asc')
    
    if search:
        data = swapi.search_people(search)
    else:
        data = swapi.get_all_people()
    
    if 'error' in data:
        return jsonify({"error": data['error']}), 500
    
    results = data.get('results', [])
    formatted_results = [format_person_data(person) for person in results]
    
    if sort_by:
        formatted_results = sort_results(formatted_results, sort_by, order)
    
    return jsonify({
        "count": len(formatted_results),
        "results": formatted_results
    })


@app.route('/api/people/<int:person_id>', methods=['GET'])
def get_person_by_id(person_id):
    # Retorna um personagem especifico por ID
    data = swapi.get_person_by_id(person_id)
    
    if 'error' in data:
        return jsonify({"error": data['error']}), 404
    
    return jsonify(format_person_data(data))


@app.route('/api/planets', methods=['GET'])
def get_planets():
    """
    Retorna planetas com filtros opcionais
    Query params: search, sort_by, order
    """
    search = request.args.get('search')
    sort_by = request.args.get('sort_by', 'name')
    order = request.args.get('order', 'asc')
    
    if search:
        data = swapi.search_planets(search)
    else:
        data = swapi.get_all_planets()
    
    if 'error' in data:
        return jsonify({"error": data['error']}), 500
    
    results = data.get('results', [])
    formatted_results = [format_planet_data(planet) for planet in results]
    
    if sort_by:
        formatted_results = sort_results(formatted_results, sort_by, order)
    
    return jsonify({
        "count": len(formatted_results),
        "results": formatted_results
    })


@app.route('/api/planets/<int:planet_id>', methods=['GET'])
def get_planet_by_id(planet_id):
    # Retorna um planeta especifico por ID
    data = swapi.get_planet_by_id(planet_id)
    
    if 'error' in data:
        return jsonify({"error": data['error']}), 404
    
    return jsonify(format_planet_data(data))


@app.route('/api/starships', methods=['GET'])
def get_starships():
    """
    Retorna naves com filtros opcionais
    Query params: search, sort_by, order
    """
    search = request.args.get('search')
    sort_by = request.args.get('sort_by', 'name')
    order = request.args.get('order', 'asc')
    
    if search:
        data = swapi.search_starships(search)
    else:
        data = swapi.get_all_starships()
    
    if 'error' in data:
        return jsonify({"error": data['error']}), 500
    
    results = data.get('results', [])
    formatted_results = [format_starship_data(starship) for starship in results]
    
    if sort_by:
        formatted_results = sort_results(formatted_results, sort_by, order)
    
    return jsonify({
        "count": len(formatted_results),
        "results": formatted_results
    })


@app.route('/api/starships/<int:starship_id>', methods=['GET'])
def get_starship_by_id(starship_id):
    # Retorna uma nave especifica por ID
    data = swapi.get_starship_by_id(starship_id)
    
    if 'error' in data:
        return jsonify({"error": data['error']}), 404
    
    return jsonify(format_starship_data(data))


# Para Google Cloud Functions
def starwars_api(request):
    """
    Entry point para Google Cloud Functions
    Essa função é chamada automaticamente pelo GCP quando alguém faz requisição
    """
    with app.request_context(request.environ):
        return app.full_dispatch_request()


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)