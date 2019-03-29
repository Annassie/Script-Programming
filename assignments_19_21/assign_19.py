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
def info(country):
	for a, b in zip(countrycodes, codemap):
		d[a].append(codemap)

print(dict(countries))
