'''
Used to create files for practive
'''

import random as rd

for i in range(50):
	one = str(rd.randrange(1,255))		
	two = str(rd.randrange(1,255))
	three = str(rd.randrange(1,255))
	four= str(rd.randrange(1,255))
	note = str(rd.randrange(18,32))
	with open('testprefixlist.txt','a') as file:
		file.write('seq '+str(i)+' '+one+'.'+two+'.'+three+'.'+four+'/'+note+'\n')
