import time


userDta = input('\n User: ')
passDta = input(' Password: ')

while userDta != 'admin' or passDta != '123' :
	print(' Access Denied! Please try again...')
	userDta = input('\n User: ')
	passDta = input(' Password: ')

else:
	print(' Login Success')
	time.sleep(.3)
	print(' Accessing...3')
	time.sleep(.3)
	print(' Accessing...2')
	time.sleep(.3)
	print(' Accessing...1')
	import grading_system 
	
	


# Program Written by: Aron Paul Gonzales
