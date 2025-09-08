myList  = []

while True:
    print("1. Append list\n"
          "2. Remove From the List\n"
          "3. Pop an element from the list\n"
          "4. Display the List\n"
          "Type any other number to quit\n")
    Option = int(input("Enter you choice: "))
    if Option == 1:
        myList.append(input("Type anything to add: "))
    elif Option == 2:
        myList.remove(input("What would you like to remove: "))
    elif Option == 3:
        myList.pop()
    elif Option == 4:
        print(myList)
    else:
        break