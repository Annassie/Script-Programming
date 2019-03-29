# list
countrycodes = ["fi", "se", "no"]

# dictionaries
codemap = {"fi": "Finland", "se": "Sweden", "no":"Norway"}
countries = { "Finland": {"Prime minister": ("Juho Sipila", 54),
	      "Population": 5.439},
	      "Sweden": {"Prime minister": ("Stefan Lofven", 58),
	      "Population": 9.593},
	      "Norway": {"Prime minister": ("Erna Solberg", 54),
              "Population": 5.084}
             }

def countryinfo(countrycodes,codemap,countries):
	for country in countrycodes:
		print("{0}:\n\t head honcho: {1}, who is {2} years old \n\t population: {3} million".format(codemap[country],
			countries[codemap[country]]["Prime minister"][0],countries[codemap[country]]["Prime minister"][1], 
			countries[codemap[country]]["Population"]))

countryinfo(countrycodes,codemap,countries)

