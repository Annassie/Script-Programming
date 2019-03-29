import sys

def printFile(file):
	f = open(file, "r")	# mikä tahansa file
	text = f.readlines()	# file:n teksti, lue kaikki rivit
	for i in range(0, len(text)):
		text[i] = text[i].strip()
		print(text[i])
	print("\n")
	f.close()

def main():
	try:
		if len(sys.argv) >= 1:
			try:
				filename = sys.argv[1]
				printFile(filename)
			except IOError:
				print("No ifle %s found!" % filename)
	except:
		print("Not enough arguments")
		print("Usage: 32.py <filename>")

main()
