import subprocess
import time

list=['Calculator', 'Safari', 'GarageBand', 'iMovie', 'Stocks', 'Stickies', 'Photos',
	'Preview', 'Calender', 'Chess', 'Contacts', 'Itunes', 'Messages', 'Mail', 'Maps',
	'Notes', 'Reminder', 'Dictionary']

def launchProgram():
	for program in list:
		try:
			path = '/Applications/'+program+'.app'
			subprocess.Popen(['open', path])
		except:
			continue

while True:
	launchProgram()
	time.sleep(5)