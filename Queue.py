qlist = []

def enqueue():
    qlist.append(input("Enter a value to add to the list"))

def dequeue():
    qlist.pop(0)

def display():
    print(qlist)

while 1:
    print("1. Add to the list\n"
          "2. Remove from the list\n"
          "3. Display the list\n"
          "Type any other number to quit")

    Option = int(input("Make a choice"))

    if Option == 1: enqueue()

    elif Option == 2: dequeue()

    elif Option == 3: display()

    else: break