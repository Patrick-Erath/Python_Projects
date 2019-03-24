import threading, time
print('Start of program')

def takeANap():
	time.sleep(5)
	print('Finished sleeping')

threadObj = threading.Thread(target = takeANap)
threadObj.start()

for i in range(2):
	print('doing other stuff')