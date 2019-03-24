# stopwatch.py - a simple stomwatch program
import time

# Display instructions
print('Press ENTER to begin. Afterwards press ENTER to "click" the stopwatch. Press CTRL-C to QUIT')
input()	# Pres senter to begin
print('Started.')
startTime = time.time()
lastTime = startTime
lapNum = 1

# Start tracking the lap times
try:
	while True:
		input()
		lapTime = round(time.time()-lastTime, 2)
		totalTime = round(time.time()-startTime, 2)
		print('Lap #%s: %s (%s)' %(lapNum, totalTime, lapTime))
		lapNum += 1
		lastTime = time.time()
except KeyboardInterrupt:
	# Handle the CTRL-C exception to keep its error message from displaying
	print('\nDone.')