print("\nNote: You must input a grade with minimum of 60 & maximum of 100.")

re = ""
while re == "":
    print()
    sub1 = int(input('English: '))
    sub2 = int(input('Math: '))
    sub3 = int(input('Science: '))

    bridgePoint = sub1 + sub2 + sub3
    totalAve = float(bridgePoint // 3)



    if sub1<60 or sub2<60 or sub3<60 or sub1>100 or sub2>100 or sub3>100:
        print("-------------------------")
        print("!!!COMPUTATION DENIED!!!")
        if sub1<60 or sub1>100:
            print("Invalid Grade in English")
        if sub2<60 or sub2>100:
            print("Invalid Grade in Math")
        if sub3<60 or sub3>100:
            print("Invalid Grade in Science")


    else:
        # Computed Successfully
        # Computed Successfully
        # Computed Successfully
        print("-------------------------")
        print("TOTAL AVERAGE: " , totalAve)


    re = input("Press enter to continue | Press any key & enter to exit...    ")
    print("\n")

print("\n---program ended---\n\n")



# Written by: Aron Paul Gonzales