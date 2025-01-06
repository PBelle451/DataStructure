import json
c3p0 = '''{
	"name": "C-3PO",
	"height": "167",
	"mass": "75",
	"hair_color": "n/a",
	"skin_color": "gold",
	"eye_color": "yellow",
	"birth_year": "112BBY",
	"gender": "n/a",
	"homeworld": "https://swapi.py4e.com/api/planets/1/",
	"films": [
		"https://swapi.py4e.com/api/films/1/",
		"https://swapi.py4e.com/api/films/2/",
		"https://swapi.py4e.com/api/films/3/",
		"https://swapi.py4e.com/api/films/4/",
		"https://swapi.py4e.com/api/films/5/",
		"https://swapi.py4e.com/api/films/6/"
	],
	"species": [
		"https://swapi.py4e.com/api/species/2/"
	],
	"vehicles": [],
	"starships": [],
	"created": "2014-12-10T15:10:51.357000Z",
	"edited": "2014-12-20T21:17:50.309000Z",
	"url": "https://swapi.py4e.com/api/people/2/"
}'''
c3p0 = json.loads(c3p0)
c3p0['name'] = "Johnny Bell"
c3p0['height'] = "170"
c3p0['mass'] = "110"
c3p0['hair_color'] = "brown"
c3p0['skin'] = "white"
c3p0_str = json.dumps(c3p0)
print(c3p0_str)