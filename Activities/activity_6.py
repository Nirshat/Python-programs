print(' Python Program Written by: Aron Paul Gonzales')
print('\n MULTIPLICATION TABLE (from 1 to 10)')

# this is the whole function of multiplication table po sir
def table_function ():
	if num_input >= 1 and num_input <= 10: 
		for i in range(10):   # this is a number from 0 to 9
			i += 1  	# add 1 in each number to make it from 1 to 10
			
			# this will display the multiplication table of the inputted number 
			print('  ',num_input,'×',i,'=',num_input * i)
	

	# this will execute sir if the user input a number below 1 / 10 above
	else:
		print(''' _(System Denied...)
 Invalid input for below 1 or above 10
 Please try again...(Press Enter)''')
		 

again = ''
while again == '': # the loop will continue as long as the user does not inserting any key (Pressing Enter).
	num_input = int(input('\n  Enter number: '))
	table_function()  # this will execute the whole function of multiplication table
	print('__________________________________________________')
	# this will execute if the user insert any key (the program will end).
	again = input(' Type any key to end program... ')
	
	