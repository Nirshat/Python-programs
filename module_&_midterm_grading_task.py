
print(' Python Program Written by: Aron Paul Gonzales')

cont = "y"
while cont=="y":
	print('\n')

	# This area is for taking input from the user
	stu_name = input (" Enter the Student's name: ")
	mod1 = float(input("\n Enter the Student's Grade in Module 1: "))
	mod2 = float(input(" Enter the Student's Grade in Module 2: "))
	mod3 = float(input(" Enter the Student's Grade in Module 3: "))
	mod4 = float(input(" Enter the Student's Grade in Module 4: "))
	mod5 = float(input(" Enter the Student's Grade in Module 5: "))
	stu_MT = float(input(" Enter the Student's Grade in Midterm Examination: "))


	# This is the computation for the midterm grade
	# • Module 1 Grade (15% of the Midterm Grade)
	# • Module 2 Grade (10% of the Midterm Grade)
	# • Module 3 Grade (10% of the Midterm Grade)
	# • Module 4 Grade (5% of the Midterm Grade)
	# • Module 5 Grade (20% of the Midterm Grade)
	# • Midterm Exam (40% of the Midterm Grade)
	totalAve = (0.15*mod1 + 0.1*mod2 + 0.1*mod3 + 0.05*mod4 + 0.2*mod5 + 0.4*stu_MT) // 1

	# The user must enter a grade with a minimum/maximum of 0 to 100
	if mod1>100 or mod2>100 or mod3>100 or mod4>100 or mod5>100 or stu_MT>100 :
		# Or this Statements will be Displayed
		print('''\n  Computation Denied...
  You have entered a invalid grade...
  You must enter a grade with a minimum/maximum 0 to 100''')
	elif mod1<0 or mod2<0 or mod3<0 or mod4<0 or mod5<0 or stu_MT<0 :
		print('''\n  Computation Denied...
  You have entered a invalid grade...
  You must enter a grade with a minimum/maximum 0 to 100''')
	else:
		print('\n  The Computed Midterm Grade of',stu_name,'is:',totalAve)
		if totalAve <= 100 and totalAve >= 96:
			print('  Remarks: PASSED, EXCELLENT!')
		elif totalAve <= 95 and totalAve >= 91:
			print('  Remarks: PASSED, VERY GOOD!')
		elif totalAve <= 90 and totalAve >= 85:
			print('  Remarks: PASSED, GOOD')
		elif totalAve <= 84 and totalAve >= 80:
			print('  Remarks: PASSED, FAIR')
		elif totalAve <= 79 and totalAve >= 75:
			print('  Remarks: PASSED, POOR!')
		else:
			print('  Remarks: FAILED, SORRY :(')
	
	

	
	# This condition below is declared using while loop in above
	# The user must insert "y" to continue
	# and try again the computation of midterm grade
	# or else the user must insert "n" key to end the program
	print('\n Insert "y" key to continue'),print(' or...')
	cont = input(' Insert "n" key to End Program: ')


	if cont=="n":
		print('\n - Program Ended - \n')
		break

	else:
		while cont!="y":
			print('\n Insert "y" key to continue'),print(' or...')
			cont = input(' Insert "n" key to End Program: ')

			if cont=="n":
				print('\n - Program Ended - \n')
				break
	
