print('hello world!')

import pygame
import numpy as np
from random import randrange

class Snake:
	def __init__(self):
		self.display_width = 400
		self.size = 10;
		self.x = randrange(5, self.display_width)
		self.y = randrange(5, self.display_width)
		# need vector of x,y 
		self.array = np.array([
			[self.x, self.y],
			[self.x-1, self.y],
			[self.x-2, self.y],
			[self.x-3, self.y]
		])

	def draw(self):
		pygame.init()
		blue = (51, 250, 204)
		white = (255, 255, 255)
		black = (0, 0, 0)
		QUIT = False
		x_fruit = randrange(1, self.display_width)
		y_fruit = randrange(1, self.display_width)

		gameDisplay = pygame.display.set_mode((self.display_width, self.display_width))
		pygame.display.set_caption('Snake')
		clock = pygame.time.Clock()

		FRUIT_PLACE = False
		#while !FRUIT_PLACE:
			#for x,y in array:
				#if x+self.size==

		while QUIT==False:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					QUIT = True
					pygame.quit()
					quit()
				#reset
				gameDisplay.fill(white)
				#draw snake
				for x,y in self.array:
					pygame.draw.rect(gameDisplay, black, [x, y, self.size, self.size])
				#draw fruit
				pygame.draw.rect(gameDisplay, blue, [x_fruit, y_fruit, self.size, self.size])
				pygame.display.update()

if __name__ == '__main__':
	snake = Snake()
	snake.draw()
