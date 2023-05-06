


print("\n\n  Written by: Aron Paul Gonzales")


stu_name = str (input("\n\n  Please enter the student Name: "))
print("\n   Student's name: ",stu_name)

sub1 = int(input("    Enter the Grade in Subject 1: "))
sub2 = int (input("    Enter the Grade in Subject 2: "))
sub3 = int (input("    Enter the Grade in Subject 3: "))
sub4 = int (input("    Enter the Grade in Subject 4: "))
sub5 = int (input("    Enter the Grade in Subject 5: "))

all = sub1 + sub2 + sub3 + sub4 + sub5
average = all / 5

print("\n     Average: " , average)
if  average <= 100.0 and average >= 75.0 :
	print ("\n   The student passed.")
else:
	print("\n   The student failed.")
	
	
print("\n\n\n	")