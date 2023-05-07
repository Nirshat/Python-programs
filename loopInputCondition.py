

re = "y"
while re == "y":

  print('\n Hello World')
	
  # Script Area...
  # Script Area...
  # Script Area...
  # Script Area...
  # Script Area...
  # Script Area...
  # Script Area...

	

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