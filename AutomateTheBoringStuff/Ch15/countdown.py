# countdown.py - A simple countdown script
import time, subprocess

timeLeft = 5
while timeLeft > 0:
	print(timeLeft)
	time.sleep(1)
	timeLeft-=1

subprocess.Popen(['open', 'alarm.wav'])