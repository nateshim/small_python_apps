#Author: Nathanael Shim
#Description: Your classic game of rock, paper, and scissors!....except you're playing against Bill sigh smh.
import random
import sys

times_billy_lost = 0
def rock_paper_scissors():
	global times_billy_lost
	try:
		billychoices = ["rock", "paper", "scissors"]
		choices = ["rock", "paper", "scissors", "rocket"]
		yourChoice = input("Bill: Alright let's go! rock, paper...\nYou:")
		billyChoice = random.choice(billychoices)
		if times_billy_lost >= 1:
			if yourChoice == "rock":
				billyChoice = "paper"
			elif yourChoice == "paper":
				billyChoice = "scissors"
			elif yourChoice == "scissors":
				billyChoice = "rock"
			else:
				billyChoice = random.choice(billychoices)
		if yourChoice not in choices:
			if times_billy_lost < 1:
				print("Uhhh come back when you learn how to play rock paper scissors lol")
				return
			else:
				print("Billy: Fufufu! That trick won't save you!")
				rock_paper_scissors()
		else:
			print("..." + billyChoice + "!")
			if times_billy_lost >= 1 and yourChoice == "rocket":
				print("Billy: NOOO! HOW DID YOU KNOW???")
				print("Congratulations! You beat Billy at his own game!")
				return
			elif yourChoice == "rocket":
				print("Uhhh come back when you learn how to play rock paper scissors lol")
				return 
			if yourChoice == "rock" and billyChoice == "rock":
				print("Billy: Hohoho! A worthy opponent!")
				rock_paper_scissors()
			elif yourChoice == "rock" and billyChoice == "paper":
				print("Billy: Huehuehue! Looks like I win again!")
				try:
					rematch = input("Rematch: yes/no\n")
					if rematch == "yes":
						if times_billy_lost < 1:
							print("Billy: Ack! uhh..uh..n-n-no no more rematches get out!")
							print("Game over!")
							return
						else:
							print("Billy: Huehuehue! Sure thing Susan, I'm feeling extra confident today >:)")
							rock_paper_scissors()
					elif rematch == "no":
						if times_billy_lost < 1:
							print("Billy: Huehuehue! Looks like someone's a sore loser! >:)")
							return
						else:
							print("Billy: Nope! Sorry we're playing again! This is what happens when you humiliate me >:)")
							rock_paper_scissors()
					else:
						if times_billy_lost < 1:
							print("Billy: Huehuehue! Looks like someone's a sore loser! >:)")
							print("Game over! Note: make sure that you put quotation marks around your answer!") 
							return
						else:
							print("Billy: Nope! Sorry we're playing again! This is what happens when you humiliate me >:)")
							rock_paper_scissors()
				except Exception as exception:
					if times_billy_lost < 1:
							print("Billy: Huehuehue! Looks like someone's a sore loser! >:)")
							print("Game over! Note: make sure that you put quotation marks around your answer!") 
							return
					else:
						print("Billy: Nope! Sorry we're playing again! This is what happens when you humiliate me >:)")
						rock_paper_scissors() 
				return
			elif yourChoice == "rock" and billyChoice == "scissors":
				print("Billy: I-I-Impossible! How could I lose!")
				print("Congratulations! You won!")
				try:
					rematch = input("Rematch: yes/no\n")
					if rematch == "yes":
						print("Billy: Just you wait! I got a little surprise for you soon huehuehue")
						times_billy_lost += 1
						rock_paper_scissors()
					elif rematch == "no":
						if times_billy_lost < 1:
							print("Billy: Huehuehue! Scared Jonny? >:)")
							return
						else:
							print("Billy: Nope! Sorry we're playing again! This is what happens when you humiliate me >:)")
							rock_paper_scissors()
					else:
						if times_billy_lost < 1:
							print("Billy: Huehuehue! Scared Jonny? >:)")
							print("Game over! Note: make sure that you put quotation marks around your answer!") 
							return
						else:
							print("Billy: Nope! Sorry we're playing again! This is what happens when you humiliate me >:)")
							rock_paper_scissors()
				except Exception as exception:
					if times_billy_lost < 1:
							print("Billy: Huehuehue! Scared Jonny? >:)")
							print("Game over! Note: make sure that you put quotation marks around your answer!") 
							return
					else:
						print("Billy: Nope! Sorry we're playing again! This is what happens when you humiliate me >:)")
						rock_paper_scissors()
				return
			elif yourChoice == "paper" and billyChoice == "paper":
				print("Billy: Hohoho! A worthy opponent!")
				rock_paper_scissors()
			elif yourChoice == "paper" and billyChoice == "scissors":
				print("Billy: Huehuehue! Looks like I win again!")
				try:
					rematch = input("Rematch: yes/no\n")
					if rematch == "yes":
						if times_billy_lost < 1:
							print("Billy: Ack! uhh..uh..n-n-no no more rematches get out!")
							print("Game over!")
							return
						else:
							print("Billy: Huehuehue! Sure thing Susan, I'm feeling extra confident today >:)")
							rock_paper_scissors()
					elif rematch == "no":
						if times_billy_lost < 1:
							print("Billy: Huehuehue! Looks like someone's a sore loser! >:)")
							return
						else:
							print("Billy: Nope! Sorry we're playing again! This is what happens when you humiliate me >:)")
							rock_paper_scissors()
					else:
						if times_billy_lost < 1:
							print("Billy: Huehuehue! Looks like someone's a sore loser! >:)")
							print("Game over! Note: make sure that you put quotation marks around your answer!") 
							return
						else:
							print("Billy: Nope! Sorry we're playing again! This is what happens when you humiliate me >:)")
							rock_paper_scissors()
				except Exception as exception:
					if times_billy_lost < 1:
							print("Billy: Huehuehue! Looks like someone's a sore loser! >:)")
							print("Game over! Note: make sure that you put quotation marks around your answer!") 
							return
					else:
						print("Billy: Nope! Sorry we're playing again! This is what happens when you humiliate me >:)")
						rock_paper_scissors() 
				return
			elif yourChoice == "paper" and billyChoice == "rock":
				print("Billy: I-I-Impossible! How could I lose!")
				print("Congratulations! You won!")
				try:
					rematch = input("Rematch: yes/no\n")
					if rematch == "yes":
						print("Billy: Just you wait! I got a little surprise for you soon huehuehue")
						times_billy_lost += 1
						rock_paper_scissors()
					elif rematch == "no":
						if times_billy_lost < 1:
							print("Billy: Huehuehue! Scared Jonny? >:)")
							return
						else:
							print("Billy: Nope! Sorry we're playing again! This is what happens when you humiliate me >:)")
							rock_paper_scissors()
					else:
						if times_billy_lost < 1:
							print("Billy: Huehuehue! Scared Jonny? >:)")
							print("Game over! Note: make sure that you put quotation marks around your answer!") 
							return
						else:
							print("Billy: Nope! Sorry we're playing again! This is what happens when you humiliate me >:)")
							rock_paper_scissors()
				except Exception as exception:
					if times_billy_lost < 1:
							print("Billy: Huehuehue! Scared Jonny? >:)")
							print("Game over! Note: make sure that you put quotation marks around your answer!") 
							return
					else:
						print("Billy: Nope! Sorry we're playing again! This is what happens when you humiliate me >:)")
						rock_paper_scissors()
				return
			elif yourChoice == "scissors" and billyChoice == "scissors":
				print("Billy: Hohoho! A worthy opponent!")
				rock_paper_scissors()
			elif yourChoice == "scissors" and billyChoice == "rock":
				print("Billy: Huehuehue! Looks like I win again!")
				try:
					rematch = input("Rematch: yes/no\n")
					if rematch == "yes":
						if times_billy_lost < 1:
							print("Billy: Ack! uhh..uh..n-n-no no more rematches get out!")
							return
						else:
							print("Billy: Huehuehue! Sure thing Susan, I'm feeling extra confident today >:)")
							rock_paper_scissors()
					elif rematch == "no":
						if times_billy_lost < 1:
							print("Billy: Huehuehue! Looks like someone's a sore loser! >:)")
							return
						else:
							print("Billy: Nope! Sorry we're playing again! This is what happens when you humiliate me >:)")
							rock_paper_scissors()
					else:
						if times_billy_lost < 1:
							print("Billy: Huehuehue! Looks like someone's a sore loser! >:)")
							return
						else:
							print("Billy: Nope! Sorry we're playing again! This is what happens when you humiliate me >:)")
							rock_paper_scissors()
				except Exception as exception:
					if times_billy_lost < 1:
							print("Billy: Huehuehue! Looks like someone's a sore loser! >:)")
							return
					else:
						print("Billy: Nope! Sorry we're playing again! This is what happens when you humiliate me >:)")
						rock_paper_scissors() 
				return
			else:
				print("Billy: I-I-Impossible! How could I lose!")
				print("Congratulations! You won!")
				try:
					rematch = input("Rematch: yes/no\n")
					if rematch == "yes":
						print("Billy: Just you wait! I got a little surprise for you soon huehuehue")
						times_billy_lost += 1
						rock_paper_scissors()
					elif rematch == "no":
						if times_billy_lost < 1:
							print("Billy: Huehuehue! Scared Jonny? >:)")
							return
						else:
							print("Billy: Nope! Sorry we're playing again! This is what happens when you humiliate me >:)")
							rock_paper_scissors()
					else:
						if times_billy_lost < 1:
							print("Billy: Huehuehue! Scared Jonny? >:)")
							return
						else:
							print("Billy: Nope! Sorry we're playing again! This is what happens when you humiliate me >:)")
							rock_paper_scissors()
				except Exception as exception:
					if times_billy_lost < 1:
							print("Billy: Huehuehue! Scared Jonny? >:)")
							return
					else:
						print("Billy: Nope! Sorry we're playing again! This is what happens when you humiliate me >:)")
						rock_paper_scissors()
				return
	except Exception as exception:
		if times_billy_lost < 1:
			print("Uhhh come back when you learn how to play rock paper scissors lol")
			return
		else:
			print("Billy: Nope! Sorry we're playing again! This is what happens when you humiliate me >:)")
			rock_paper_scissors()


if __name__ == "__main__":
	rock_paper_scissors()