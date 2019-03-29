import sys

def printFile():

	f = open("animals.txt", "r") # open a file for reading

	animal_list = f.readlines() # read all lines into a list called "animal_list"
	animal_list.sort()

	for line in animal_list:
		print(line)
	f.close() # close the file

def addAnimal():
	f = open("animals.txt", "a")
	add = input("Add an animal: ")
	f.write(add+"\r\n")

	print("{add} is added".format(add=add))
	f.close()

def deleteAnimal():
	print("All animals: \n")
	printFile()
	option = input("Write the animal you want to delete: ")
	f = open("animals.txt", "r")
	animal_list = f.readlines()

	for line in range(0, len(animal_list)):
		animal_list[line] = animal_list[line].strip()
	f.close()

	animal_list.remove(option)

	print("{option} is delete".format(option=option))

	with open("animals.txt", "w") as f:
		for item in animal_list:
			f.write("{}\n".format(item))

def main():

	while True:
		print("1) Print animals")
		print("2) Add an animal")
		print("3) Delete an animal")

		choice = int(input("Enter your choice, 1, 2 or 3: "))

		if (choice == 1):
			printFile()
		elif (choice == 2):
			addAnimal()
		elif (choice == 3):
			deleteAnimal()
		else:
			sys.exit()

main()

