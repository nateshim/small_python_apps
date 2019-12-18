#Author: Nathanael Shim
#Description: Everyone's favorite guessing game: hangman
#- Used pygame and random-word 
# o
#/ \
# |
#/ \
from random_word import RandomWords
import random, sys, pygame, time

pygame.init()

size = width, height = 800, 600

screen = pygame.display.set_mode(size)
black = (0,0,0)
red = (200,0,0)
green = (0,200,0)

bright_red = (255,0,0)
bright_green = (0,255,0)
white = 255, 255, 255
clock = pygame.time.Clock()


gameDisplay = pygame.display.set_mode((width, height))
pygame.display.set_caption("HANGMAN")


def message_display(text):
	largeText = pygame.font.Font('freesansbold.ttf',115)
	TextSurf, TextRect = text_objects(text, largeText)
	TextRect.center = ((width/2), (height/2))
	gameDisplay.blit(TextSurf, TextRect)

	pygame.display.update()
	time.sleep(2)

	game_loop()

def text_objects(text, font):
	textSurface = font.render(text, True, black)
	return textSurface, textSurface.get_rect()

def button(msg,x,y,w,h,ic,ac,action=None):
	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()

	if x+w > mouse[0] > x and y+h > mouse[1] > y:
		pygame.draw.rect(gameDisplay, ac,(x,y,w,h))

		if click[0] == 1 and action != None:
			action()
	else:
		pygame.draw.rect(gameDisplay, ic, (x,y,w,h))

	smallText = pygame.font.Font("freesansbold.ttf",20)
	TextSurf, TextRect = text_objects(msg, smallText)
	TextRect.center = ((x+(w/2)), (y+(h/2)))
	gameDisplay.blit(TextSurf, TextRect)

def game_intro():
	intro = True

	while intro:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

		gameDisplay.fill(white)
		largeText = pygame.font.Font('freesansbold.ttf', 115)
		TextSurf, TextRect = text_objects("HANGMAN", largeText)
		TextRect.center = ((width/2),(height/2))
		gameDisplay.blit(TextSurf, TextRect)

		button("Start",150,450,100,50,green,bright_green,game_loop)
		button("Quit",550,450,100,50,red,bright_red,quitgame)


		pygame.display.update()
		clock.tick(15)

def game_loop():
	gameExit = False
	r = RandomWords()
	randomWord = r.get_random_word(hasDictionaryDef="true", includePartOfSpeech="noun",minLength=6, maxLength=6)
	randomWord = randomWord.lower()
	remaining_letters = "******"
	#hangmanhead = 'o'
	#hangmanleftarm = '/'
	#hangmanrightarm = "\\"
	#hangmanbody = '|'
	#hangmanleftleg = '/'
	#hangmanrightleg = '\\'
	hangmanhead = ''
	hangmanleftarm = ''
	hangmanrightarm = ''
	hangmanbody = ''
	hangmanleftleg = ''
	hangmanrightleg = ''
	chances = 0
	while not gameExit:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		if '*' not in remaining_letters:
			game_won()
		if chances > len(remaining_letters):
			game_over()
		if event.type == pygame.KEYDOWN:
			key = pygame.key.name(event.key)
			if key in randomWord:
				counter = 0
				while counter < len(randomWord):
					if key == randomWord[counter]:
						remaining_letters = remaining_letters[0:counter] + key + remaining_letters[counter+1::]
					counter+=1
			else:
				chances += 1
				if chances == 1:
					hangmanhead = 'o'
				elif chances == 5:
					hangmanleftarm = '/'
				elif chances == 6:
					hangmanrightarm = "\\"
				elif chances == 2:
					hangmanbody = '|'
				elif chances == 3:
					hangmanleftleg = '/'
				elif chances == 4:
					hangmanrightleg = '\\'
		gameDisplay.fill(white)
		largeText = pygame.font.Font('freesansbold.ttf', 115)
		TextSurf, TextRect = text_objects(remaining_letters, largeText)
		TextRect.center = ((width/2),(height-100))
		gameDisplay.blit(TextSurf, TextRect)

		largeTextHangman = pygame.font.Font('freesansbold.ttf', 115)
		TextSurfHangman, TextRectHangman = text_objects(hangmanhead, largeTextHangman)
		TextRectHangman.center = ((width/2),(height/4))
		gameDisplay.blit(TextSurfHangman, TextRectHangman)

		largeTextHangman = pygame.font.Font('freesansbold.ttf', 115)
		TextSurfHangman, TextRectHangman = text_objects(hangmanleftarm, largeTextHangman)
		TextRectHangman.center = ((width/2-25),(height/4+85))
		gameDisplay.blit(TextSurfHangman, TextRectHangman)

		largeTextHangman = pygame.font.Font('freesansbold.ttf', 115)
		TextSurfHangman, TextRectHangman = text_objects(hangmanrightarm, largeTextHangman)
		TextRectHangman.center = ((width/2+25),(height/4+85))
		gameDisplay.blit(TextSurfHangman, TextRectHangman)

		largeTextHangman = pygame.font.Font('freesansbold.ttf', 115)
		TextSurfHangman, TextRectHangman = text_objects(hangmanbody, largeTextHangman)
		TextRectHangman.center = ((width/2),(height/4+75))
		gameDisplay.blit(TextSurfHangman, TextRectHangman)

		largeTextHangman = pygame.font.Font('freesansbold.ttf', 115)
		TextSurfHangman, TextRectHangman = text_objects(hangmanleftleg, largeTextHangman)
		TextRectHangman.center = ((width/2-20),(height/2 + 30))
		gameDisplay.blit(TextSurfHangman, TextRectHangman)

		largeTextHangman = pygame.font.Font('freesansbold.ttf', 115)
		TextSurfHangman, TextRectHangman = text_objects(hangmanrightleg, largeTextHangman)
		TextRectHangman.center = ((width/2+20),(height/2 + 30))
		gameDisplay.blit(TextSurfHangman, TextRectHangman)

		pygame.display.update()
		clock.tick(10)
def game_over():
	print("GAME OVER")
	quitgame()
def game_won():
	print("CONGRATULATIONS!")
	quitgame()
def quitgame():
	pygame.quit()
	quit()

game_intro()
game_loop()
pygame.quit()
quit()