
menu1 = ["\n hotdog", " egg", " tocino", " shanghai", " bacon", " longganisa", " meatloaf"]

menu2 = ["\n menudo", " sinigang", " adobo", " inagamangan", " pinakbet", " bulalo", " batchoy", " dinuguan", " giniling"]


print('''
Menu 1 = 1
Menu 2 = 2
''')

menu = input("enter menu: ")

if menu == "1" :
	for breakfast in menu1 :
		print(breakfast)
	print('\n\n -- Program Ended. -- \n\n')
	
	
elif menu == "2" :	
	for lunch in menu2 :
		print(lunch)
	print('\n\n -- Program Ended. -- \n\n')
		
		
		
		
else:
	print("Invalid Input.")
	print('\n\n -- Program Ended. -- \n\n')
	
	