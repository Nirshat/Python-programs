
#CALCULATOR
#def function
#return statement

con = ""
while con == "":
	num1 = float(input('\n Enter 1st num: '))
	num2 = float(input(' Enter 2nd num: '))

	print('''\n Operator Keywords:
 [ add, sub, mul, div,
   rem, pwr, rnd ] ''')

	opt = str(input('\n Enter operator: '))

	def add (x,y):
		return x + y
	
	def minus (x,y):
		return x - y

	def times (x,y):
		return x * y

	def divide (x,y):
		return x / y

	def remain (x,y):
		return x % y 

	def power (x,y):
		return x ** y

	def round (x,y):
		return x // y

	if opt == 'add' :
		print(' Total:',add(num1,num2))
	elif opt == 'sub' :
		print(' Total:',minus(num1,num2))
	elif opt == 'mul' :
		print(' Total:',times(num1,num2))
	elif opt == 'div' :
		print(' Total:',divide(num1,num2))
	elif opt == 'rem' :
		print(' Total:',remain(num1,num2))
	elif opt == 'pwr' :
		print(' Total:',power(num1,num2))
	elif opt == 'rnd' :
		print(' Total:',round(num1,num2))
	else:
		print(' wrong keyword')
	
	print(' Enter to continue or...')
	con = input(' Type any key to End: ')
	print(' ______________________')
