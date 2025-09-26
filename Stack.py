slist = []


def push():
    slist.append(input("Enter a value to add to the list"))


def pop():
    slist.pop()

def display():
    print(slist)

while 1:
    print("1. Add to the list\n"
          "2. Remove from the list\n"
          "3. Display the list\n"
          "Type any other number to quit")

    Option = int(input("Make a choice"))

    if Option == 1: push()

    elif Option == 2: pop()

    elif Option == 3: display()

    else: break