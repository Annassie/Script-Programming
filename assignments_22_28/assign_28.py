import sys

def add(num1, num2):
	result = num1 + float(num2)
	return result

def sub(num1, num2):
	result = num1 - float(num2)
	return result

def multiply(num1, num2):
	result = num1 * float(num2)
	return result

def divide(num1, num2):
	try:
		result = num1 / float(num2)
		return result
	except ZeroDivisionError:
		return "Cannot divide ba zero!"


def main():
	while True:
		print("0) add")
		print("1) subtract")
		print("2) multiply")
		print("3) divide")
		print("-1) quit")

		choise = input("Choose: ")
		if choise == "0" or choise == "1" or choise == "2" or choise == "3":
			number1 = input("Enter number 1: ")
			number2 = input("Enter number 2: ")
			if choise == "0":
				try:
					print("Result is ", add(int(number1), int(number2)))
				except TypError:
					print("Data type mismatch")
				except:
					print("Something went wrong")
			elif choise == "1":
				try:
					print("Result is ", sub(int(number1), int(number2)))
				except TypeError:
					print("Data type mismatch")
				except:
					print("Something went wrong")
			elif choise == "2":
				try:
					print("Result is ", multiply(int(number1), int(number2)))
				except TypeError:
					print("Data type mismatch")
				except:
					print("Something went wrong")
			elif choise == "3":
				try:
					print("Result is ", divide(int(number1), int(number2)))
				except TypeError:
					print("Data type mismatch")
				except:
					print("Something went wrong")
		elif choise == "-1":
			sys.exit()
		else:
			print("Invalid option")
main()



