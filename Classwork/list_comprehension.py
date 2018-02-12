'''
This is just an exmaple of LIST COMPREHENSION
using the dictionary.txt file
'''

doc = open('dictionary.txt', 'r').readlines()

#this is performing the list comprehension
create_list = [word for word in doc] #this uses WORD as each element, creates new list

print(create_list) #this will simply print out the doc

create_list = [word for word in  doc if 'UU' in word] #filters doc in single line


print('break, break')
#print new list
print(create_list)
