#Stopwatch.py, A simple stopwatch program
import time

#Display program's instructions
print('Press ENTER to being. Afterwards, press ENTER to "click" the stopwatch pres CRTL-C to quit')

input() #press enter
print('Started')
startTime = time.time()
lastTime = startTime
lapNum = 1

try:
	while True:
		input()
		lapTime = round(time.time() - lastTime, 2)
		totalTime = round(time.time() - startTime, 2)
		print('Lap #%s: %s (%s)' % (lapNum, totalTime, lapTime), end='')
		lapNum += 1
		lastTime = time.time() #reset the last lap time
except KeyboardInterrupt:
	#Handle Ctrl-c exception
	print('\nDone.')
