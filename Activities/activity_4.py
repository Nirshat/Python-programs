
print(' Program Written by: Aron Paul Gonzales')

# 1.) Create a List of Students Names containing the following items.
	   # -"John"
	   # -"Miguel"
  	 # -"Carlo"
  	 # -"Mark"
  	 # -"Ian"
  	 # -"Kris"
  	 # -"Josh"
  	 # -"Lawrence"		  		
stu = ['John','Miguel','Carlo','Mark','Ian','Kris','Josh','Lawrence']


# 2.) Print the complete list to the screen.
print('\n',stu)

# 3.) Print the length of the list to the screen.
print('\n  Number of Students:',len(stu))

# 4.) Print the 5th item of the list to the screen.
print('  Student Number 5:',stu[4])

# 5.) Check if student "Bryan" exists in the list. 
#     If yes print "Found!", else print "Not Found." to the screen.
if 'Bryan' in stu:
	print('  Found.')
else:
	print('  Not Found.')

# 6.) Change the 7th item to "Sonny".
	stu[6] = 'Sonny'

# 7.) Add new item at the end of the list. Append "Rico" to list.
	stu.append('Rico')
	
# 8.) Remove "Mark" and "Ian" from the list.
	stu.pop(3) #This index is 'Mark'
	stu.pop(3) #This index is 'Ian'
	
# 9.) Sort the list in descending order.
	stu.sort(reverse=True) 
  
# 10.) Print again the complete list to screen.
	print('\n',stu)
	