import requests
from django.shortcuts import render

def get_pokemon_data(pokemon):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}/"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {
            'id': data['id'],
            'name': data['name'].capitalize(),
            'image': data['sprites']['front_default'],
            'types': [t['type']['name'].capitalize() for t in data['types']],
            'stats': {stat['stat']['name']: stat['base_stat'] for stat in data['stats']},
        }
    return None

def get_all_pokemon():
    url = "https://pokeapi.co/api/v2/pokemon?limit=1000"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return [{'name': pokemon['name'].capitalize()} for pokemon in data['results']]
    return []

def pokemon_view(request):
    pokemon = request.GET.get('pokemon', None)
    data = get_pokemon_data(pokemon) if pokemon else None
    prev_pokemon = data['id'] - 1 if data and data['id'] > 1 else None
    next_pokemon = data['id'] + 1 if data else None
    all_pokemon = get_all_pokemon()
    return render(request, 'pokemon.html', {
        'data': data, 
        'prev_pokemon': prev_pokemon, 
        'next_pokemon': next_pokemon,
        'all_pokemon': all_pokemon
    })
