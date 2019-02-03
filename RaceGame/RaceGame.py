import pygame

pygame.init() #Initialize pigame
display_width = 800
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)
red = (252, 53, 53)

gameDisplay = pygame.display.set_mode((display_width,display_height)) #Sets window size
pygame.display.set_caption('Fast and Furious') #Sets window name
clock = pygame.time.Clock() #Frames per second measured using clock
carImg = pygame.image.load('car.png')

xCar=display_width*0.45
yCar=display_height*0.7
x_change=0

def car(x,y):
	gameDisplay.blit(carImg, (x,y))
	#Car image is a paramater, so need to reference x and y as a tuple

#Crash logic
crashed = False

while not crashed:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: #Quit game when x is pressed & exit while loop
			crashed = True

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

	#Draw background & car
	gameDisplay.fill(white)
	car(xCar, yCar)

	pygame.display.update() #Updates a certain portion of the screen
	clock.tick(60) #Frames per second








pygame.quit() #Quits pygame
quit()