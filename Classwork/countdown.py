#countdown script to launch alarm

import time, subprocess


def countDown():
	timeLeft = 60
	while timeLeft > 0:
		print(timeLeft)
		time.sleep(1)
		timeLeft = timeLeft -  1
countDown()


