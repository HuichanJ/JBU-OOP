myStudent = {}

while True:
    print("1. Add Student\n"
          "2. Delete a Student\n"
          "3. Edit a Student\n"
          "4. Print out Dictionary\n"
          "Type any other number to quit\n")
    Option = int(input("Type any number of your choice"))
    if Option == 1:
        myStudent.update({input("Enter Student ID"): {"name":input("Type name: "), "major":input("Type major: "),
                                                 "year":input("Type year: "), "credit":int(input("Type credit: ")),
                                                 "gpa":int(input("Type GPA: "))}})
    elif Option == 2:
        del myStudent[input("Type the student ID you want to Delete: ")]
    elif Option == 3:
        myStudent.update({input("Enter Student ID to Edit"): {"name": input("Type name: "), "major": input("Type major: "),
                                                      "year": input("Type year: "),
                                                      "credit": int(input("Type credit: ")),
                                                      "gpa": int(input("Type GPA: "))}})
    elif Option == 4:
        print(myStudent)
    else:
        break
