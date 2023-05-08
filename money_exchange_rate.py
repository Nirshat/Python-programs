import colorama
from colorama import Fore, Style
colorama.init(autoreset=True)

print("\n EXCHANGE RATE")
print(' -exchange your money into foreign currency-')

x = ""
while x == "":
	print()
	print (''' • Japanese Yen [¥]
 • US Dollar [$]
 • Philippine Peso [₱]''')
	print('\n Keywords: [ yen, dollar, peso ]')

	money_class = str(input(" Enter your Currency: "+Fore.GREEN))
	
	keyword_A = ['yen','Yen','YEN']
	keyword_B = ['dollar','Dollar','DOLLAR']
	keyword_C = ['peso','Peso','PESO']
	
	#JAPANESE YEN
	if money_class in keyword_A:
		money = float(input(Fore.WHITE+" Enter value: "+Fore.GREEN))
		if money <= 0:
			print(Fore.RED+' Invalid...\n No value to exchange')
		else:
			print('  [ ¥'+str(money)+' ]','exchange to: dollar[$] or peso[₱]')
			choice = input(" Enter Foreign Currency: "+Fore.GREEN)
			if choice in keyword_B:
				#convert to dollar
				exchange = money * 0.0088
				moneyFormat = '${:,.2f}'.format(exchange)
				print(Fore.WHITE+Style.BRIGHT+" TOTAL VALUE:",Fore.GREEN+Style.BRIGHT+moneyFormat)
			elif choice in keyword_C:
				#convert to peso
				exchange = money * 0.44
				moneyFormat = '₱{:,.2f}'.format(exchange)
				print(Fore.WHITE+Style.BRIGHT+" TOTAL VALUE:",Fore.GREEN+Style.BRIGHT+moneyFormat)
			elif choice in keyword_A:
				print(Fore.RED+' Invalid...\n Cannot convert with same currency')
			else :
				print(Fore.RED+" Invalid Keyword...(Not defined)")
				

	#US DOLLAR		
	elif money_class in keyword_B:
		money = float(input(Fore.WHITE+" Enter value: "+Fore.GREEN))
		if money <= 0:
			print(Fore.RED+' Invalid...\n No Value to exchange')
		else:
			print('  [ $'+str(money)+' ]','exchange to: yen[¥] or peso[₱]')
			choice = input(" Enter Foreign Currency: "+Fore.GREEN)
			if choice in keyword_A :
				#convert to yen
				exchange = money * 114.11
				moneyFormat = '¥{:,.2f}'.format(exchange)
				print(Fore.WHITE+Style.BRIGHT+" TOTAL VALUE:",Fore.GREEN+Style.BRIGHT+moneyFormat)
			elif choice in keyword_C :
				#convert to peso
				exchange = money * 50.48
				moneyFormat = '₱{:,.2f}'.format(exchange)
				print(Fore.WHITE+Style.BRIGHT+" TOTAL VALUE:",Fore.GREEN+Style.BRIGHT+moneyFormat)
			elif choice in keyword_B:
				print(Fore.RED+' Invalid...\n Cannot convert with same currency')
			else:
				print(Fore.RED+" Invalid Keyword...(Not defined)")
				

	#PHILIPPINE PESO
	elif money_class in keyword_C :
		money = float(input(Fore.WHITE+" Enter value: "+Fore.GREEN))
		if money <= 0:
			print(Fore.RED+' Invalid...\n No Value to exchange')
		elif money > 0:
			print('  [ ₱'+str(money)+' ]','exchange to: yen[¥] or dollar[$]')
			choice = input(" Enter Foreign Currency: "+Fore.GREEN)
			if choice in keyword_A:
				#convert to yen
				exchange = money * 2.25
				moneyFormat = '¥{:,.2f}'.format(exchange)
				print(Fore.WHITE+Style.BRIGHT+" TOTAL VALUE:",Fore.GREEN+Style.BRIGHT+moneyFormat)
			elif choice in keyword_B :
				#convert to dollar
				exchange = money * 0.020
				moneyFormat = '${:,.2f}'.format(exchange)
				print(Fore.WHITE+Style.BRIGHT+" TOTAL VALUE:",Fore.GREEN+Style.BRIGHT+moneyFormat)
			elif choice in keyword_C:
				print(Fore.RED+' Invalid...\n Cannot convert with same currency')
			else:
				print(Fore.RED+" Invalid Keyword...(Not defined)")
			
		
		# this will shown when the input in choice is invalid
	else :
		print(Fore.RED+" Invalid Keyword...( Not defined)")
		
	# print(' ________________________________________')
	print(' press [enter] to continue or...')
	x = input(''' insert any key to end program: ''')
	print(' -----------------------------------------')
	if x != "":
		print('\n - Program Ended - \n')
	
	
	
	