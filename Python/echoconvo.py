finished = 0

while finished == 0:

	print('Hello, talk to me! How many chess games make a master? I will not stop until you are right! ')

	response = input()


	if response == '2':
		print('Correct!')
		finished = 1
	elif response == '3':
		print('Even more correct!')
		finished = 1
	elif response == '4':
		print('Most correct!')
		finished = 1
	else: 
		print('Wrong!')
		finished = 0



	print('You responded:', response, '\n')

