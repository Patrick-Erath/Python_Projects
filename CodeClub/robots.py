from random import choice
from turtle import *

file = open('cards.txt','r') # Open file as read


screen = Screen()
screen.bgcolor('white')
style = ('Verdana', 14, 'bold')
penup()
hideturtle()
attr = ['Strength', 'Intelligence', 'Speed']


robots = {} # Robots dictionary

for line in file.read().splitlines():
	name, strength, intelligence, speed, image = line.split(',')
	robots[name]=[strength, intelligence, speed, image]
	clear()
	screen.register_shape(image)


while True:
	robot = input('Chose a robot:') 

	if robot in robots:
		setheading(-90)
		stats = robots[robot]
		clear()
		goto(0, 100)
		shape(stats[3])
		setheading(90)
		stamp()
		setheading(-90)
		forward(60)
		write('Name : ' + robot, font=(str(style[0]), 21, style[2]), align='center')
		forward(25)
		for i in range(3):
			write(str(attr[i])+' :'+robots[robot][i],font=style, align='center')
			forward(25)
	
	else:
		write('This robot doesn\'t exist, press enter to create it!',font=style, align='center')
		#ALLOW USER TO CREATE NEW ROBOT

file.close()