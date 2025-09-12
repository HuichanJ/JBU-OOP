myList = []

while True:
    print("1. Add an Element on the list\n"
          "2. Remove an Element from the list\n"
          "3. Replace an Element in the List\n"
          "4. Sort the Elements in the List\n"
          "5. Reverse the Elements in the List\n"
          "6. Print the list Elements\n"
          "Type any other number to Exit")
    Option = int(input("Enter you choice: "))
    if Option == 1:
        myList.append(input("Type anything to add: "))
    elif Option == 2:
        myList.remove(input("What would you like to remove: "))
    elif Option == 3:
        x = int(input("Type the index"))
        myList[x] = input("Enter a new value to replace the index")
    elif Option == 4:
        myList.sort()
    elif Option == 5:
        myList.reverse()
    elif Option == 6:
        print(myList)
    else:
        break