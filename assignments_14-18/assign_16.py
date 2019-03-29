import sys

def division(*args):
	try:
		theResult = int(args[0]) / int(args[1])
		args = int
		if (len(args)) > 2:
			raise TypeError("Numbers of Parameters can't be more than 2")
		else:
			return theResult

	except ZeroDivisionError:
		print("Error: Cannot divide by zero")
		sys.exit()

	except TypeError:
		print("Numbers of Parameters can't be more than 2")
		sys.exit()

	except ValueError:
		print("One or both of your parameter are wrong type!")
		sys.exit()


print (division(12,3,4))
