again = "y"
while again == "y":

	print("\n  [1]  Hamburger ---- 35 pesos")
	print("  [2]  French fries ---- 25 pesos")
	print("  [3]  Spaghetti ---- 45 pesos")
	print("  [4]  Softdrinks ---- 20 pesos")
	print("  [5]  Ice Cream ---- 25 pesos")

	hamburger = 35
	fries = 25
	spaghetti = 45
	softdrinks = 20 
	icecream = 25


	order = input("\n  Enter your order:  ")


	if order == "1" :
		cash = int(input("  Enter your Cash: "))
		change1 = cash - hamburger
		if cash >= hamburger:
			print("\n  Change: ",change1)
	
		elif cash < hamburger :
			print("\n  insufficient cash...")
		
		else :
			print("\n  input your cash")
		
		
	elif order == "2" :
		cash = int(input("  Enter your cash: "))
		change2 = cash - fries
		if cash >= fries:
			print("\n  Change: ",change2)
	
		elif cash < fries :
			print("\n  insufficient cash...")
		
		else :
			print("\n  input your cash")
			
			
			
	elif order == "3" :
		cash = int(input("  Enter your Cash: "))
		change3 = cash - spaghetti
		if cash >= spaghetti :
			print("\n  Change: ",change3)
	
		elif cash < spaghetti :
			print("\n  insufficient cash...")
		
		else :
			print("\n  input your cash")
		
		

	elif order == "4" :
		cash = int(input("  Enter your Cash: "))
		change4 = cash - softdrinks
		if cash >= softdrinks :
			print("\n  Change: ",change4)
	
		elif cash < softdrinks :
			print("\n  insufficient cash...")
		
		else :
			print("\n  input your cash")
		
		
		
	elif order == "5" :
		cash = int(input("  Enter your Cash: "))
		change5 = cash - icecream
		if cash >= icecream :
			print("\n  Change: ",change5)
	
		elif cash < icecream :
			print("\n  insufficient cash...")
		
		else :
			print("\n  input your cash")
		
		
	else :
		print("\n\n  error input / input your order first...")
		
	
	print("\n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
	
	again = str(input("\n\n  another order? press [y] if yes and press [n] if no : "))