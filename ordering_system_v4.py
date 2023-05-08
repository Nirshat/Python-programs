

print('''\n [1] Fries --- 15
 [2] Burger --- 25
 [3] Coke --- 15 ''')

con = ""
while con == "":
	frs = int(input('\n Fries: '))
	brg = int(input(' Burger: '))
	cke = int(input(' Coke: '))
	print(' ------------')
	def amt (a,b,c):
		return 15*a + 25*b + 15*c
	if amt(frs,brg,cke) < 0:
		print(' System Denied...')
	else:
		print(' Amount:',amt(frs,brg,cke))
		csh = int(input(' Cash: '))
		if csh < amt(frs,brg,cke):
			print(' -Insufficient cash')
		else:
			print(' Change:',csh - amt(frs,brg,cke))

	con = input('\n Enter for next order or...\n Type any key to close: ')
	print(' __________________________')