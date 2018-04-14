import threading, time


print("start")

def takeNap():
	time.sleep(10)
	print("wake")

threadObj = threading.Thread(target = takeNap)
threadObj.start()


print("End")

	
