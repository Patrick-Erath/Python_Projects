import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
import random

vertices = (
	(1, -1, -1),
	(1, 1, -1),
	(-1, 1, -1),
	(-1, -1, -1),
	(1, -1, 1),
	(1, 1, 1),
	(-1, -1, 1),
	(-1, 1, 1)
	)

edges = (
	(0,1),
	(0,3),
	(0,4),
	(2,1),
	(2,3),
	(2,7),
	(6,3),
	(6,4),
	(6,7),
	(5,1),
	(5,4),
	(5,7)
	)

surfaces = (
	(0,1,2,3),
	(3,2,7,6),
	(6,7,5,4),
	(4,5,1,0),
	(1,5,7,2),
	(4,0,3,6)
	)

color = (
	(1,0,0),
	(0,1,0),
	(0,0,1),
	(0,0,0),
	(1,1,1),
	(0,1,1),
	(1,0,0),
	(0,1,0),
	(0,0,1),
	(0,0,0),
	(1,1,1),
	(0,1,1)
	)

ground_vertices = (
	(-10, -2.1, 20),
	(10, -2.1, 20),
	(-10, -2.1, -300),
	(10, -2.1, -300),
	)

white = (0, 0, 0)
black = (255,255,255)

pygame.init()
display = (800,600)
gameDisplay = pygame.display.set_mode(display)
#gameDisplay = pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
pygame.display.set_caption('Cubez')

def text_objects(text, font):
	textSurface = font.render(text, True, black)
	return textSurface, textSurface.get_rect() 

def message_display(text, fontSize, xPosition, yPosition):
	largeText = pygame.font.Font('freesansbold.ttf', fontSize)
	TextSurf, TextRect = text_objects(text, largeText)
	TextRect.center = (xPosition, yPosition)
	gameDisplay.blit(TextSurf, TextRect)
	pygame.display.update()

def game_intro():
	intro=True
	while intro:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					main()
		gameDisplay.fill(white)
		message_display("Cubez Runnerz", 80, 400, 300)
		message_display("By : Patrick Erath", 30, 400, 350)
		message_display("PRESS SPACE TO START", 30, 400, 390)
		pygame.display.update()
		#Buttons to start & Quit game


def set_vertices(max_distance, min_distance = -20, camera_x = 0, camera_y = 0):
	camera_x = -1*int(camera_x)
	camera_y = -1*int(camera_y)

	x_value_change = random.randrange(camera_x-75, camera_x+75) #+-75
	y_value_change = random.randrange(camera_y-75, camera_y+75)
	z_value_change = random.randrange(-1*max_distance,-20)
	# x_value_change=0
	# y_value_change=0
	# z_value_change = max_distance

	new_vertices = []

	for vert in vertices:
		new_vert = []
		new_x = vert[0] + x_value_change
		new_y = vert[1] + y_value_change
		new_z = vert[2] + z_value_change

		new_vert.append(new_x)
		new_vert.append(new_y)
		new_vert.append(new_z)

		new_vertices.append(new_vert)

	return new_vertices

def Cube(vertices):
	glBegin(GL_QUADS)
	for surface in surfaces:
		x=0
		for vertex in surface:
			x+=1
			glColor3fv(color[x])
			glVertex3fv(vertices[vertex])
	glEnd()

def main():
	pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
	x_move = 0
	y_move = 0
	max_distance = 100
	cur_x = 0
	cur_y = 0
	game_speed = 1.5
	direction_speed = 0.8 #0.8

	cube_dict = {}

	for i in range(120):
		cube_dict[i] = set_vertices(max_distance)

	#params: (FieldofView in degrees, AspectRation width/height, Clipping ranges
	gluPerspective(45, (display[0]/display[1]), 0.1, max_distance)

	#params: x,y,z
	glTranslatef(0, 0, -40)

	#params: degrees, x, y, z
	glRotatef(0,0,0,0)

	object_passed = False

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					x_move=direction_speed
				if event.key == pygame.K_RIGHT:
					x_move=-1*direction_speed
				if event.key == pygame.K_UP:
					y_move=-1*direction_speed
				if event.key == pygame.K_DOWN:
					y_move=direction_speed
	
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					x_move=-0
				if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
					y_move=0

		x = glGetDoublev(GL_MODELVIEW_MATRIX)
		#print(x[3][0])
		camera_x = x[3][0]
		camera_y = x[3][1]
		camera_z = x[3][2]

		cur_x += x_move
		cur_y += y_move

		glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

		glTranslatef(x_move,y_move,game_speed)

		for each_cube in cube_dict:
			Cube(cube_dict[each_cube])

		delete_list = []
		new_max = 0

		for each_cube in cube_dict:
			#print("Cube y Coordinates",cube_dict[each_cube][0][1])
			#print("Camera Coordiantes",camera_y)
			#print(x)
			#pygame.time.wait(50)
			#print("test")
			if camera_z <= cube_dict[each_cube][0][2]:
				new_max = int(-1*(camera_z-max_distance*2))
				cube_dict[each_cube] = set_vertices(new_max, int(camera_z-max_distance), cur_x, cur_y)

			if camera_z < cube_dict[each_cube][0][2]+4:
				#print("Passed z")
				if camera_x < cube_dict[each_cube][0][0] and camera_x > cube_dict[each_cube][0][0] - 4:
					#print("Passed x")
					#if camera_y > cube_dict[each_cube][0][1]  and camera_y < cube_dict[each_cube][0][1]:
					if camera_y > cube_dict[each_cube][0][1] and camera_y < cube_dict[each_cube][0][1] + 3 or camera_y < cube_dict[each_cube][0][1] and camera_y >  cube_dict[each_cube][0][1] - 1.4 :
						print("Hit Object")

		pygame.display.flip()	
		#pygame.time.wait(40)

game_intro()
main()


