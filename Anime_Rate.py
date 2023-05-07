import time


re = "y"
while re == "y":
	anime = input("\n\n Anime: ")

	print(' Rating...')
	time.sleep(.1)
	print(' 20% for the story line')
	time.sleep(.1)
	print(' 15% for the design')
	time.sleep(.1)
	print(' 30% for the animation')
	time.sleep(.1)
	print(' 10% for the character development')
	time.sleep(.1)
	print(' 25% for the Plot ')
	time.sleep(.1)


	print('\n Rate from 0 to 100')

	stry = int(input('\n Story Line: '))
	des = int(input(' Design: '))
	anm = int(input(' Animation: '))
	cd = int(input(' Character Development: '))
	plt = int(input(' Plot: '))


	if stry>100 or des>100 or anm>100 or cd>100 or plt>100 :
		if stry > 100 or stry < 0 :
			print(' invalid rate for Story Line')

		if des > 100 or des < 0 :
			print(' invalid rate for Design')

		if anm > 100 or anm < 0:
			print(' invalid rate for Animation')

		if cd > 100 or cd < 0:
			print(' invalid rate for Character Development')

		if plt > 100 or plt < 0:
			print(' invalid rate for Plot')

	elif stry<0 or des<0 or anm<0 or cd<0 or plt<0 :
		if stry > 100 or stry < 0 :
			print(' invalid rate for Story Line')

		if des > 100 or des < 0 :
			print(' invalid rate for Design')

		if anm > 100 or anm < 0 :
			print(' invalid rate for Animation')

		if cd > 100 or cd < 0 :
			print(' invalid rate for Character Development')

		if plt > 100 or plt < 0 :
			print(' invalid rate for Plot')


	else:
		rate = (stry*.2 + des*.15 + anm*.3 + cd*.1 + plt*.25) // 1
		print(' RATING:',rate)
		if rate <= 100 and rate >= 96:
			print ('',anime,'is God tier')

		elif rate <= 95 and rate >= 91:
			print ('',anime,'is Masterpiece')
		
		elif rate <= 90 and rate >= 86:
			print ('',anime,'is Very Good')
		
		elif rate <= 85 and rate >= 80:
			print ('',anime,'is Good')
		
		elif rate <= 79 and rate >= 75:
			print ('',anime,'is Fine? •_•')
		
		elif rate <= 74 and rate >= 70:
			print ('',anime,'is Boring asf')
		
		else:
			print (' Poor anime :(')


	# This condition below is declared using while loop in above
	# The user must insert "y" to continue
	# and try again the computation of midterm grade
	# or else the user must insert "n" key to end the program
	print('\n Insert "y" key to continue'),print(' or...')
	re = input(' Insert "n" key to End Program: ')

	if re=="n":
		print('\n - Program Ended - \n')
		break

	else:
		while re!="y" and re!="n":
			print('\n Insert "y" key to continue'),print(' or...')
			re = input(' Insert "n" key to End Program: ')

			if re=="n":
				print('\n - Program Ended - \n')
				break




# Program Written by: Aron Paul Gonzales