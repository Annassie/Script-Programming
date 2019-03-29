import sys

def division(x, y):
	try:
		theResult = int(x) / int(y)
		return theResult

	except ZeroDivisionError:
		print("Error: Cannot divide by zero")
		sys.exit()

	except ValueError:
		print("One or both of your parameter are wrong type!")
		sys.exit()

print (division(12, "ops"))
