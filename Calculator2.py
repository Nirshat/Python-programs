more = ""
while more == "":


	print()
	
	one = float(input(" enter num: "))
	two = float(input(" enter num: "))

	a = one + two
	b = one - two
	c = one * two
	d = one / two
	e = one % two
	f = one ** two
	g = one // two

	print()

	print(" + press a if add")
	print(" - press m if minus")
	print(" × press t if times")
	print(" ÷ press d if divide")
	print(" % press r if remainder")
	print(" ** press p if power")
	print(" // press f if floor")

	print()

	ope = input(" choose operator: ")

	def function (a) :
		if ope == "a" :
			print(" total:",a)
	function(a)

	def function (b):
		if ope == "m":
			print(" total:",b)
	function (b)

	def function (c):
		if ope == "t":
			print(" total:",c)
	function (c)

	def function (d):
		if ope == "d" :
			print(" total:",d)
	function (d)
	
	def function (e):
		if ope == "r" :
			print(" total:",e)
	function (e)
	
	def function (f):
		if ope == "p" :
			print(" total:",f)
	function (f)
	
	def function (g):
		if ope == "f" :
			print(" total:",g)
	function (g)
	
	print("")
	
	more = input(" enter to continue...")
	print(' ---------------------')