lista = []
i = 0
while 1:
	i += 1
	item = raw_input("Syötä arviot %d listaan: " %i)
	if item == 'print':
		break
	if item == 'remove':
		item = raw_item("Syötä arvo mitä haluat poistaa: ")
		lista.remove(item)
	else:
		lista.append(item)

print("Tässä on sinun listasi: ")
