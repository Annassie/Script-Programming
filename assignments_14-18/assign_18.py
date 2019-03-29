thedict = {
    "List1": ["Bob","Comes","After","You"],
    "List2": [100,"Hello"]
}

# function takes a dict, a list name and the element
def add_to_list_in_dict(thedict, listname, element):
	try:
		thedict[listname].append(element)
		print("Added %s to %s." % (listname, element))
	except KeyError:
		print("The dictonary doesn't have the following key: %s" % (listname))
	else:
		for key in thedict:
			print("Dictonary have next keys: %s" % key)
	finally:
		print("Thank you for using the program!")

add_to_list_in_dict(thedict, "List1", "Hellou")
add_to_list_in_dict(thedict, "Book", "Page1")
