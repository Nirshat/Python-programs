#CALCULATOR in FUNCTIONS METHOD
  #Features
  #while loop
  #if else statement
  #def
 
print(' Calculator ver.3')

con = ""
while con == "":
	print()
	print(''' Keywords for operators:
   +[ add ] -[ min ] ×[ mul ] ÷[ div ]  
   %[ rem ] **[ power ] //[ round ]''')
	print()
	inp1 = float(input(' 1st num: '))
	inp2 = float(input(' 2nd num: '))

	ope = input(' enter operator: ')

	if ope == 'add': # this is the function coming from the input of the user
									 # user must choose an operator and insert the keyword ('add')
									 
		def asd (num1,num2): # this is parameter
												 # what are you going to do with the parameters?
			total = num1 + num2 # process of parameters
													# the parameters was declared by addition
													
			print(' total: ',total)
		asd(inp1,inp2) # call the function
									 # this will be the value of parameters
								 	# the value of the parameters is from the input of the user above.
	
								 								 	
	elif ope == 'min':
		def asd (num1,num2):
			total = num1 - num2
			print(' total: ',total)
		asd(inp1,inp2)

	elif ope == 'mul':
		def asd (num1,num2):
			total = num1 * num2
			print(' total: ',total)
		asd(inp1,inp2)
	
	elif ope == 'div':
		def asd (num1,num2):
			total = num1 / num2
			print(' total: ',total)
		asd(inp1,inp2)
		
	elif ope == 'rem':
		def asd (num1,num2):
			total = num1 % num2
			print(' total: ',total)
		asd(inp1,inp2)
		
	elif ope == 'power':
		def asd (num1,num2):
			total = num1 ** num2
			print(' total: ',total)
		asd(inp1,inp2)
	
	elif ope == 'round':
		def asd (num1,num2):
			total = num1 // num2
			print(' total: ',total)
		asd(inp1,inp2)
		
		
	con = input(''' Insert any key to End Program...
 Enter to Continue...''')
	print(' ------------------')

