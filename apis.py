import requests

class Pokemon:
    def __init__(self, name, number, weight, height, stats, types):
        self.name = name 
        self.number = number
        self.weight = weight
        self.height = height
        # hp, at, def, spa, spd, spe 
        self.stats = stats
        self.types = types

    def __str__(self):
        output_string = ""
        output_string += str(self.number) + "\n"
        output_string += self.name.capitalize() + "\n"
        output_string += f"Height: {self.height/10}m, Weight: {self.weight/10}kg\n"
        output_string += f"HP: {self.stats[0]}, Attack: {self.stats[1]}, Def: {self.stats[2]}, SPA: {self.stats[3]}, Spd: {self.stats[4]}, Spe: {self.stats[5]}\n"
        output_string += f"Types " + ", ".join(self.types) + "\n"

        return output_string
    
r = requests.get("https://pokeapi.co/api/v2/pokemon?limit=151")

data = (r.json())
results = data["results"]

for result in results[:10]:
    r = requests.get(result["url"])
    data = r.json()

    stats = []
    for stat in data ["stats"]:
        stats.append(stat["base_stat"])
    
    types = []
    for poke_type in data ["types"]:
        types.append(poke_type["type"]["name"])

    pokemon = Pokemon(data["name"], data["id"], data["height"], data["weight"], stats,types)
    #print(pokemon.number, pokemon.name , pokemon.height, pokemon.weight, pokemon.stats, pokemon.types)
    print(pokemon)