# pokemon = {
#     "name": "pikachu", 
#     "types": ["electric", 'poison'], 
#     "id": 25
#     }

# print( pokemon["name"] )

# print( pokemon['types'][1])



pokemon_list = [
    {
        "id": 1, 
        "name": "Bulbasaur", 
        "types": ["poison", "grass"]
    },
    {
        "id": 5, 
        "name": "Charmeleon", 
        "types": ["fire"]
    },
    {"id": 9, "name": "Blastoise", "types": ["water"]},
    {"id": 12, "name": "Butterfree", "types": ["bug", "flying"]},
    {"id": 16, "name": "Pidgey", "types": ["normal", "flying"]},
    {"id": 23, "name": "Ekans", "types": ["poison"]},
    {"id": 24, "name": "Arbok", "types": ["poison"]},
    {"id": 25, "name": "Pikachu", "types": ["electric"]},
]

# for pokemon in pokemon_list:
#     print(pokemon['name'])

for pokemon in pokemon_list:

    for key, val in pokemon.items():
        print(f'Key : {key}')
        print(f'Value : {val}')

for i in range(len(pokemon_list)):

    for key in pokemon_list[i]:
        print(f'Key : {key} , Value : {pokemon_list[i][key]} ')

