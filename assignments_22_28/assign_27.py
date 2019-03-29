import random
import sys

print("++ Guessing Game ++")
print("Guess a number between 0 and 20 !")
rnd = random.randint(0,20)
count = 1

while True:
	while True:

		x = input("Guess %s / 5: " % count)

		try:
			guess = int(x)
			if guess == rnd:
				print("Correct !")
				sys.exit()
			elif guess not in range(0,20):
				print("The guess should be between 0 and 20, try again")
			elif count == 5:
				print("Game over, you lost! The correct number was", rnd)
				sys.exit()
			else:
				print("sorry, try again")
				count = count + 1

		except ValueError:
			print("Not a number, try again")
