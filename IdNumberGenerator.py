import time

print()
def done():
	num = int(input("enter num of students: "))
	for stu in range(num):
		time.sleep(0.05)
		print("Student",stu+1,"---",id(stu))
done()

print("\n")

def done1():
	mun = int(input("enter num of professors: "))
	for prof in range(mun):
		time.sleep(0.05)
		print("Professor",prof+1,"---",id(prof))
done1()