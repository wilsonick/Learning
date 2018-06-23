finished = 0
string = ''
time = 5

print('Welcome musicians! How many times do you want to choose?')

time = int(input())


while len(string) < time:

	print('Choose a number between 0 and 9 inclusive! ')

	response = input()

	if len(response) <= 1:
		
		string = string + response
	
		print('You answered: ', string)
	
	else: print('Too big try again I don\'t like you. ')
	
	
"""
	if response == '1':
		string = string + '1'
		finished = 1
	elif response == '2':
		string = string + '2'
		finished = 1
	elif response == '3':
		string = string + '3'
		finished = 1
	else: 
		print('Try another number!')
		finished = 1
"""

print('Thank you for playing! Goodbye!')
