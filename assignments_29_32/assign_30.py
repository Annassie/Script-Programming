import sys

def printFile():

	f = open("animals.txt", "r") # open a file for reading

	animal_list = f.readlines() # read all lines into a list called "animal_list"
	animal_list.sort()
	f.close() # close file

	for line in animal_list:
		print(line)


def addAnimal():
	f = open("animals.txt", "a")
	add = input("Add an animal: ")
	f.write(add+"\r\n")

	print("{add} is added".format(add=add))
	f.close()

def main():

	while True:
		print("1) Print animals")
		print("2) Add an animal")

		choice = int(input("Enter your choice, 1 or 2: "))

		if (choice == 1):
			printFile()
		elif (choice == 2):
			addAnimal()
		else:
			sys.exit()

main()

