
print('Written by: Aron Paul Gonzales')


num_input = int(input('\n Enter number:'))

# OUTER LOOP
for i in range(num_input):
 # range based from the number input by the user.
 # starting from 0.

 # INNER LOOP
	for j in range(i+1):
 # i+1 to add 1 for each iteration of outer loop (to make it start from 1).
 # range based from the range of outer loop.

		print('',j+1,end='')
		# j+1 to add 1 for each iteration of inner loop (to make it start from 1).
	print()