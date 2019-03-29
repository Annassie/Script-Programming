def countryinfo(countrycodes,codemap,countries):
	for country in countrycodes:
		print("{0}:\n\t head honcho: {1}, who is {2} years old \n\t population: {3} million".format(codemap[country],
			countries[codemap[country]]["Prime minister"][0],countries[codemap[country]]["Prime minister"][1], 
			countries[codemap[country]]["Population"]))

