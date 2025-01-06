import requests

while True:
    pokemon = input("Which pokemon do you want to find? ")
    pokemon = pokemon.lower()
    if pokemon == "quit":
        break

    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"
    req = requests.get(url)
    pk = req.json()
    print(f"Name is\t\t{pk['name']}")
    print("Abilities:")
    for ability in pk['abilities']:
        print(ability['ability']['name'])
#dictionary = dict(pk)
#print(dictionary)