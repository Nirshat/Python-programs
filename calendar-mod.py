import calendar



re = ""
while re != "x" or re != "X":
    print()
    year = int(input("  Enter Year: "))
    month = int(input("  Enter Month: "))


    print()

    print(calendar.month(year,month))


    re = input("  press 'x' to end: ")