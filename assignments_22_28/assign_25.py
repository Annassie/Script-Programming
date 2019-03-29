#-*- coding: UTF-8 -*-


def calculator(cmd, num1, num2):
	try:
		if cmd =="add":
			return num1+num2
		elif cmd =="sub":
			return num1-num2
		elif cmd == "multiply":
			return num1*num2
		elif cmd == "divide":
			try:
				return num1/num2
			except ZeroDivisionError:
				return None
	except TypeError:
		return "Non numeral value"

print(calculator("add", 1, 2)) #should prints 3
print(calculator("sub", 1, 2)) #should prints -1
print(calculator("multiply", 1, 2)) #should prints 2
print(calculator("divide", 1, 2)) #should prints 0.5
print(calculator("divide", 1, 0)) #should prints "None"
print(calculator("divide", 4, "kaksi")) #should prints Error
