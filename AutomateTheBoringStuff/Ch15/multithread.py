import time, datetime

currentTime = datetime.datetime.now()
twentySeconds = datetime.timedelta(seconds = 20)
startTime = currentTime + twentySeconds

while(datetime.datetime.now() < startTime):
	time.sleep(1)

print('Program now starting')