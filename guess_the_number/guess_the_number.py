#Author: Nathanael Shim
#Description: cute guessing game with our little more than impatient host Bill


import random
import sys

angry_counter = 0

def guess_the_number():
	global angry_counter
	toCompare = random.randint(1, 20)
	try:
		val = input("Bill: Guess the number! \nYou:")
		if angry_counter > 5:
			print("Bill: Okay that's it! No more guessing for you! >:(")
			return
		elif angry_counter > 2:
			print("Bill: Hey! I said put in a number from 1-20! >:(")
			angry_counter += 1
			guess_the_number()
		elif val < 1 or val > 20:
			print("Bill: Please put in a number from 1-20!")
			angry_counter += 1
			guess_the_number()
		elif val == toCompare:
			print("Bill: Congratulations! You guessed correctly!")
			angry_counter = 0
		else:
			print("Bill: Aww! Try again!")
			guess_the_number()
	except Exception as error:
		if angry_counter > 5:
			print("Bill: Okay that's it! No more guessing for you! >:(")
			return
		elif angry_counter > 2:
			print("Bill: Hey! I said put in a number from 1-20! >:(")
			angry_counter += 1
			guess_the_number()
		else:
			print("Bill: Please put in a number from 1-20!")
			angry_counter += 1
			guess_the_number()
if __name__ == "__main__":
	guess_the_number()

