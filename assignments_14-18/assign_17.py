try:
	raise NameError("Se on NameError")
except NameError as detail:
	print("Se ei ole NimiVirhe!", detail)


try:
	my_list = [1,2,3,4,5]
	print (my_list[2])
	print (my_list[5])
except IndexError:
	print("Indeksipaikka 5 ei ole olemassa")

try:
	car = {
		"brand": "Ford",
		"model": "Mustang",
		"year": 1964
	}

	for key in car:
		print (car["color"])

except KeyError:
	print ("Väri ei ole määrittelty")
