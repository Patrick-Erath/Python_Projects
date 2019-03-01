import pygame
import random
from blob import Blob
import numpy as np

STARTING_BLUE_BLOBS = 10
STARTING_RED_BLOBS = 3
STARTING_GREEN_BLOBS = 10

WIDTH = 800
HEIGHT = 600
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

game_display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Blob World")
clock = pygame.time.Clock()

class BlueBlob(Blob):
	def __init__(self, x_boundary, y_boundary):
		Blob.__init__(self, (0, 0, 255), x_boundary, y_boundary)

	#OPERATOR OVERLOADING
	def __add__(self, other_blob): #We can redefine what actually happens when + operator is used on our object
		if other_blob.color == (255,0,0): #If blob is red
			self.size -= other_blob.size #BLUE blob size = BLUE blob size - RED size
			other_blob.size -= self.size #red size = NEW blue blob size - red size

		elif other_blob.color == (0, 255, 0): #If blob is green
			self.size += other_blob.size  #blue blob size = blue blob size + GREEN size
			other_blob.size = 0           #remove green blob
 
		elif other_blob.color == (0,0,255): #BLUE on BLUE, do nothing
			pass

		else:
			raise Exception('Tried to combine one or multiple blobs of unsupported colors!')

	def move_fast(self):
		self.x += random.randrange(-2,4)
		self.y += random.randrange(-2,4)

class RedBlob(Blob): 
	def __init__(self, x_boundary, y_boundary):
		Blob.__init__(self, (255, 0, 0), x_boundary, y_boundary)

class GreenBlob(Blob):  
	def __init__(self, x_boundary, y_boundary):
		Blob.__init__(self, (0, 255, 0), x_boundary, y_boundary)
		
def is_touching(b1,b2):
	return np.linalg.norm(np.array([b1.x,b1.y])-np.array([b2.x,b2.y]))<(b1.size + b2.size)

def handle_collisions(blob_list): #blob_list is a list of dictionaries
	blues, reds, greens = blob_list #unpacking the list
	for blue_id, blue_blob in blues.copy().items():  #for key, value in blues dictionary, (we copy the item in the dictionary because we are going to modfify them)
		for other_blobs in blues, reds, greens:   # for all the other blobs in dict blue, red and green
			for other_blob_id, other_blob in other_blobs.copy().items(): #for all key, vlaues in other blob ((we copy the item in the dictionary because we are going to modfify them)) 
				if blue_blob == other_blob: # if this blob touching itself don't do anything 
					pass
				else:
					if is_touching(blue_blob, other_blob):
						blue_blob + other_blob
						if other_blob.size <= 0:
							del other_blobs[other_blob_id] #if other blob has 0 or less size, delete it
						if blue_blob.size <= 0: 
							del blues[blue_id] #if blue blob has 0 or less size, delete blob
	return blues, reds, greens


def draw_environment(blob_list):
	game_display.fill(WHITE)
	blues, reds, greens = handle_collisions(blob_list)
	for blob_dict in blob_list:
		for blob_id in blob_dict:
			blob = blob_dict[blob_id]
			pygame.draw.circle(game_display, blob.color, [blob.x, blob.y], blob.size)
			if (blob.color == (0,0,255)):
				blob.move_fast()
			else:
				blob.move()
			blob.check_bounds()

	pygame.display.update()
	return blues, reds, greens

def main():
	blue_blobs = dict(enumerate([BlueBlob(WIDTH,HEIGHT) for i in range(STARTING_BLUE_BLOBS)]))
	red_blobs = dict(enumerate([RedBlob(WIDTH,HEIGHT) for i in range(STARTING_RED_BLOBS)]))
	green_blobs = dict(enumerate([GreenBlob(WIDTH,HEIGHT) for i in range(STARTING_GREEN_BLOBS)]))

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

		blue_blobs, red_blobs, green_blobs = draw_environment([blue_blobs,red_blobs,green_blobs])
		clock.tick(60)

if __name__ == '__main__':
	main()