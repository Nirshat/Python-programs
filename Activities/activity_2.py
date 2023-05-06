import time

print("\n\nPython Program Written by: Aron Paul Gonzales")



num1 = float (input("\n\nEnter the 1st number: "))
num2 = float (input("Enter the 2nd number: "))
	
	
plus = num1 + num2
minus = num1 - num2 
times = num1 * num2
divide = num1 / num2
remain = num1 % num2
raise_to_the_power = num1 ** num2
round_off = num1 // num2
	

	
time.sleep(0.09)
print("\n\nThe Addition result is: " , plus)
time.sleep(0.09)		
print("\nThe Subtraction result is:  " , minus)
time.sleep(0.09)	
print("\nThe Multiplication result is : " , times)
time.sleep(0.09)
print("\nThe Division result is: " , divide)
time.sleep(0.09)
print("\nThe Remainder of two numbers is: " , remain)
time.sleep(0.09)
print("\n" + str(num1), "raise to" , str(num2),"is", str(raise_to_the_power))
time.sleep(0.09)
print("\nThe Floor Division result is: " , round_off)
