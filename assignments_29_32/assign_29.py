file = open("animals.txt", "r") # open a file for reading

animal_list = file.readlines() # read all lines into a list called "animal_list"
animal_list.sort()
file.close() # close file

for line in animal_list:
	print(line)
