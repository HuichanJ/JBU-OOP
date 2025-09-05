while True:
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("Type any other number to quit\n")
    Option = int(input("Choose any options from above : "))

    if Option == 1:
        n1 = int(input("Give the first number : "))
        n2 = int(input("Give the second number : "))
        print(n1, " + ", n2, " = ", n1+n2)
    elif Option == 2:
        n1 = int(input("Give the first number : "))
        n2 = int(input("Give the second number : "))
        print(n1, " - ", n2, " = ", n1 - n2)
    elif Option == 3:
        n1 = int(input("Give the first number : "))
        n2 = int(input("Give the second number : "))
        print(n1, " * ", n2, " = ", n1 * n2)
    elif Option == 4:
        n1 = int(input("Give the first number : "))
        n2 = int(input("Give the second number : "))
        print(n1, " / ", n2, " = ", n1 / n2)
    else:
        print("You have quited")
        break

