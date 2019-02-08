import pygame
import time
import random

pygame.init() #Initialize pigame
display_width = 800
display_height = 600
car_width = 80

black = (0, 0, 0)
white = (255, 255, 255)
red = (250, 50, 50)
blue = (51, 250, 204)
green = (61, 140, 30)

dark_red = (200, 0, 0)
dark_green = (11, 90, 0)

gameDisplay = pygame.display.set_mode((display_width,display_height)) #Sets window size
pygame.display.set_caption('Fast and Furious') #Sets window name
clock = pygame.time.Clock() #Frames per second measured using clock
carImg = pygame.image.load('car.png')

def obs_avoided(count):
	font = pygame.font.SysFont(None, 25)
	text = font.render("Score:  " +str(count), True, black)
	gameDisplay.blit(text, (0, 0))

def randomColor():
	r = random.randrange(0, 255)
	g = random.randrange(0, 255)
	b = random.randrange(0, 255)
	return (r, g, b)

def obstacles(obsX, obsY, obsW, obsH, color):
	pygame.draw.rect(gameDisplay, color, [obsX, obsY, obsW, obsH]) 

def car(x,y):
	gameDisplay.blit(carImg, (x,y))
	#Car image is a paramater, so need to reference x and y as a tuple

def text_objects(text, font):
	textSurface = font.render(text, True, black)
	return textSurface, textSurface.get_rect() 

def message_display(text, fontSize, xPosition, yPosition):
	largeText = pygame.font.Font('freesansbold.ttf', fontSize)
	TextSurf, TextRect = text_objects(text, largeText)
	TextRect.center = (xPosition, yPosition)
	gameDisplay.blit(TextSurf, TextRect)
	pygame.display.update()

def button(msg,x,y,w,h,bright,dark):
	mouse = pygame.mouse.get_pos()

	if x+w > mouse[0] > x and y+h > mouse[1] > y:
		pygame.draw.rect(gameDisplay, dark, (x, y, w, h))
	else:	
		pygame.draw.rect(gameDisplay, bright, (x, y, w, h))

	message_display(msg,20,x+(w/2),y+(h/2))
	pygame.display.update()


def game_intro():
	intro=True
	while intro:
		for event in pygame.event.get():
			print(event)
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.fill(white)
		message_display("FAST & FURIOUS!", 80, display_width/2, display_height/2)
		pygame.display.update()
		#Buttons to start & Quit game

		button("PLAY", 120, 400, 200, 100, green, dark_green)
		button("QUIT", 450, 400, 200, 100, red, dark_red)

		clock.tick(15)

def crash():
	#carImg = pygame.image.load('crash.png')
	message_display("You Crashed!", 115, display_width/2, display_height/2)
	message_display("Press Space to Continue", 20, display_width/2, display_height/2+60)
	gameOver = True
	while gameOver:
	 for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_loop()
            if event.type == pygame.QUIT:
                pygame.quit()
	game_loop()


def game_loop():
	xCar=display_width*0.45
	yCar=display_height*0.7
	x_change=0
	dodged = 0

	obs_startX = random.randrange(0, display_width)
	obs_startY = -600
	obs_speed = 10
	obs_width = 100
	obs_height = 100

	#Exit game logic        
	gameExit = False
	while not gameExit:
		for event in pygame.event.get():
			if event.type == pygame.QUIT: #Quit game when x is pressed & exit while loop
				pygame.quit()
				quit()
			if event.type == pygame.KEYDOWN: #checks if a key has been pressed
				if event.key == pygame.K_LEFT: #If left arrow has been pressed
					x_change += -10	#Set x change to -10 
				if event.key == pygame.K_RIGHT: #If right arrow has been pressed
					x_change += 10   #Set y change to +10

			if event.type == pygame.KEYUP: #checks if a key has been released
				if event.key == pygame.K_LEFT:
					x_change = 0
				if event.key == pygame.K_RIGHT:
					x_change = 0	

		xCar += x_change

		#Draw background & car & obs
		gameDisplay.fill(white)
		car(xCar, yCar)
		#obstacles(obsX, obsY, obsW, obsH, color)
		obstacles(obs_startX, obs_startY, obs_width, obs_height, randomColor())
		obs_startY += obs_speed
		obs_avoided(dodged)

		if xCar > display_width - car_width or xCar < 0:
			crash()

		# Object is off the screen
		if obs_startY > display_height:
			obs_startY = 0-obs_height
			obs_startX = random.randrange(0, display_width)
			dodged += 1
			obs_speed += 0.5
			obs_width += (dodged * 1.05)

		if yCar < obs_startY + obs_height:
			if xCar > obs_startX and xCar < obs_startX + obs_width or xCar + car_width > obs_startX and xCar + car_width < obs_startX + obs_width:
				crash()

		pygame.display.update() #Updates a certain portion of the screen
		clock.tick(60) #Frames per second

game_intro()
game_loop()
pygame.quit() #Quits pygame
quit()