re = ""
while re != "x":

    print()
    num1 = int(input("Enter operand 1: "))
    num2 = int(input("Enter operand 2: "))


    def add():
        print("Total: " , num1 + num2)

    def sub():
        print("Total: " , num1 - num2)

    def mul():
        print("Total: " , num1 * num2)

    def div():
        print("Total: " , num1 / num2)



    print("[ + ]   [ - ]    [ ⨯ ]   [ ÷ ]")


    ope = input("select operator: ")


    if ope == "+":
        add()

    elif ope == "-":
        sub()

    elif ope == "⨯":
        mul()

    elif ope == "÷":
        div()

    else:
        print("Invalid Operator...")




    re = input("Press x if you want to end: ")