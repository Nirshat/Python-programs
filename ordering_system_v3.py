print()
print(''' Boku no Japanese Restaurant e yōkuso
	  いらっしゃい ません
	  Irasshaimasen! ^_^ ''')
print()
print(''' MENU:   	     PRICE:
 [1] Ramen  	   280 pesos
 [2] Takoyaki	   25 pesos (1 ball)
 [3] Udon      	   230 pesos (1 bowl)
 [4] Tofu      	   50 pesos (1 pack)
 [5] Yakisoba      380 pesos
 [6] Sushi         900 pesos''')


again = ""
while again == "":
	print()
	order = input(" enter your order: ")
	
	ramen = 280
	takoyaki = 25
	udon = 230
	tofu = 50
	yakisoba = 380
	sushi = 900
	
	if order == "1" :
		num_of_order = int(input(" number of orders: "))
		if num_of_order <= 0 :
			print(" ∆ input error !!! ∆ \n pls enter num of orders you want to take")
		elif num_of_order >= 1 :
			computation = num_of_order * ramen
			print(" Total:",computation)
			cash = int(input(" Cash: "))
			if cash < computation:
				print(" Insufficient cash...")
			else:
				change = cash - computation
				print(" Change:",change)
			
			
	elif order == "2" :
		num_of_order = int(input(" number of orders: "))
		if num_of_order <= 0 :
			print(" ∆ input error !!! ∆ \n pls enter num of orders you want to take")
		elif num_of_order >= 1 :
			computation = num_of_order * takoyaki
			print(" Total:",computation)
			cash = int(input(" Cash: "))
			if cash < computation:
				print(" Insufficient cash...")
			else:
				change = cash - computation
				print(" Change:",change)
			
			
	elif order == "3" :
		num_of_order = int(input(" number of orders: "))
		if num_of_order <= 0 :
			print(" ∆ input error !!! ∆ \n pls enter num of orders you want to take")
		elif num_of_order >= 1 :
			computation = num_of_order * udon
			print(" Total:",computation)
			cash = int(input(" Cash: "))
			if cash < computation:
				print(" Insufficient cash...")
			else:
				change = cash - computation
				print(" Change:",change)
		
			
	elif order == "4" :
		num_of_order = int(input(" number of orders: "))
		if num_of_order <= 0 :
			print(" ∆ input error !!! ∆ \n pls enter num of orders you want to take")
		elif num_of_order >= 1 :
			computation = num_of_order * tofu
			print(" Total:",computation)
			cash = int(input(" Cash: "))
			if cash < computation:
				print(" Insufficient cash...")
			else:
				change = cash - computation
				print(" Change:",change)
			
			
	elif order == "5" :
		num_of_order = int(input(" number of orders: "))
		if num_of_order <= 0 :
			print(" ∆ input error !!! ∆ \n pls enter num of orders you want to take")
		elif num_of_order >= 1 :
			computation = num_of_order * yakisoba
			print(" Total:",computation)
			cash = int(input(" Cash: "))
			if cash < computation:
				print(" Insufficient cash...")
			else:
				change = cash - computation
				print(" Change:",change)
			
			
	elif order == "6" :
		num_of_order = int(input(" number of orders: "))
		if num_of_order <= 0 :
			print(" ∆ input error !!! ∆ \n pls enter num of orders you want to take")
		elif num_of_order >= 1 :
			computation = num_of_order * sushi
			print(" Total:",computation)
			cash = int(input(" Cash: "))
			if cash < computation:
				print(" Insufficient cash...")
			else:
				change = cash - computation
				print(" Change:",change)
			
			
	else :
		print(" ∆ input error !!! ∆...pls enter your order")
				
	
	
	
	again = input(" >> order again? \n -press enter if yes \n -insert any letter or num key if no:" )
	print(" -------------------------------")
print('\n- Program Ended -\n')