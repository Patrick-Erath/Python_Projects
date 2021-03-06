import pygame
import numpy as np
import time
from random import randrange

class Snake:
	def __init__(self):
		self.display_width = 400
		self.size = 10
		self.move = 'none'
		self.score = 0
		# need vector of x,y 
		self.array = np.array([
			[randrange(5, self.display_width), randrange(5, self.display_width)],
		])

	def draw(self):
		pygame.init()
		blue = (51, 250, 204)
		red = (255, 0, 0)
		white = (255, 255, 255)
		black = (0, 0, 0)
		QUIT = False
		x_fruit = randrange(1, self.display_width)
		y_fruit = randrange(1, self.display_width)
		counter = 0
		blockers = [
			[randrange(10, 30), randrange(10, 30)],
			[-randrange(10, 30), randrange(10, 30)],
			[randrange(10, 30), -randrange(10, 30)],
			[-randrange(10, 30), -randrange(10, 30)]
		]


		gameDisplay = pygame.display.set_mode((self.display_width, self.display_width))
		pygame.display.set_caption('Snake')
		clock = pygame.time.Clock()

		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()

				# reset
				gameDisplay.fill(white)


				# get move events
				if event.type == pygame.KEYDOWN:
					counter+=1
					if event.key == pygame.K_RIGHT:
						self.move = 'right'
					elif event.key == pygame.K_LEFT:
						self.move = "left"
					elif event.key == pygame.K_UP:
						self.move = "up"
					elif event.key == pygame.K_DOWN:
						self.move = "down"
					else:
						self.move = "none"

					self.moveSnake(self.move)

				# create blockers
				# TODO : refactor this code
				if counter == 0:
					blockers = [
						[randrange(10, 30), randrange(10, 30)],
						[-randrange(10, 30), randrange(10, 30)],
						[randrange(10, 30), -randrange(10, 30)],
						[-randrange(10, 30), -randrange(10, 30)]
					]
				elif counter == 5:
					counter = 0


				#  draw snake
				for x,y in self.array:
					pygame.draw.rect(gameDisplay, black, [x, y, self.size, self.size])
					# draw blockers
					for blocker in blockers:
						pygame.draw.rect(gameDisplay, red, [x - blocker[0], y-blocker[1], self.size, self.size])


				# draw fruit
				pygame.draw.rect(gameDisplay, blue, [x_fruit, y_fruit, self.size, self.size])


				# fruit not in snake coordinates -> fruit got eatten
				for x,y in self.array:
					if(abs(x - x_fruit) < self.size and abs(y - y_fruit) < self.size):
						# fruit  is inside snake coordinate, make new fruit
						self.score = self.score + 1
						while(True):
							print('ate')
							x_fruit = randrange(1, self.display_width)
							y_fruit = randrange(1, self.display_width)
							if(abs(x - x_fruit) < self.size or abs(y - y_fruit) < self.size):
								break
							break


			pygame.display.update()
			clock.tick(60)

	def moveSnake(self, event):
		# grab head
		new_x = self.array[0][0]
		new_y = self.array[0][1]

		#print('move')

		# make sure within boundaries
		if(new_x < self.display_width and new_y < self.display_width):
			for x,y in self.array:
				if(event == 'right'):
					new_x = x + self.size
				if(event == 'left'):
					new_x = x - self.size
				if (event == 'down'):
					new_y = y + self.size
				if (event == 'up'):
					new_y = y - self.size

		# update
		self.array[0][0] = new_x
		self.array[0][1] = new_y

		#for x, y in self.array:
			#pygame.draw.rect(display, color, [x, y, self.size, self.size])
			# check if ate fruit

if __name__ == '__main__':
	snake = Snake()
	snake.draw()
