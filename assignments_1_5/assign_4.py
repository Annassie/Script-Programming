# Kaksi vaihtoehtoja, ei kumpikaan toimi


## Vaihtoehto 1

persons = ["alice", "bob", "craig", "dave", "elisabeth", "frank", "george"]
index = 0
for index, name in enumerate(persons):
	if index % 2 == 0:
		persons.append(name)
#return persons
print("Nimet, joiden indeksipaikka on jaollinen kahdella " + '\n' + "indeksipaikka: " + str(index) + persons)

'''
Vaihtoehto 2
def is_even_name(l):
	persons = ["alice", "bob", "craig", "dave", "elisabeth", "frank", "george"]
	index = 0

	for name in l:
		if index % 2 == 0:
			persons.append(name)
	return persons
print (is_even_name(["alice", "bob", "craig", "dave", "elisabeth", "frank", "george"]))
'''
