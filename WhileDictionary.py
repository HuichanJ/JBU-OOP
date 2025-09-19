myStudent = {}

while True:
    print("1. Add a Student\n"
          "2. Delete a Student\n"
          "3. Modify a Student\n"
          "4. Display all students\n"
          "Type any other number to quit\n")
    Option = int(input("Type any number of your choice"))
    if Option == 1:
        StudentID = input("Enter Student ID")
        StudentName = input("Enter Student Name")
        Lab1 = int(input("Score for Lab 1 "))
        Lab2 = int(input("Score for Lab 2 "))
        Lab3 = int(input("Score for Lab 3 "))
        Lab4 = int(input("Score for Lab 4 "))
        Lab5 = int(input("Score for Lab 5 "))
        Total = (Lab1 + Lab2 + Lab3 + Lab4 + Lab5)
        myStudent.update({StudentID: {"Student Name":StudentName, "Lab 1":Lab1, "Lab 2":Lab2,
                                      "Lab 3":Lab3, "Lab 4":Lab4,
                                      "Lab 5":Lab5,"Total Score":Total, "Average Score":Total/5,
                                      "Average Score Percentage": Total / 50 * 100}})
    elif Option == 2:
        del myStudent[input("Type the student ID you want to Delete: ")]
    elif Option == 3:
        StudentID = input("Enter Student ID to modify")
        StudentName = input("Enter Student Name")
        Lab1 = int(input("Score for Lab 1 "))
        Lab2 = int(input("Score for Lab 2 "))
        Lab3 = int(input("Score for Lab 3 "))
        Lab4 = int(input("Score for Lab 4 "))
        Lab5 = int(input("Score for Lab 5 "))
        Total = (Lab1 + Lab2 + Lab3 + Lab4 + Lab5)
        myStudent.update({StudentID: {"Student Name":StudentName, "Lab 1":Lab1, "Lab 2":Lab2,
                                      "Lab 3":Lab3, "Lab 4":Lab4,
                                      "Lab 5":Lab5,"Total Score":Total, "Average Score":Total/5,
                                      "Average Score Percentage": Total / 50 * 100}})
    elif Option == 4:
        print(myStudent)
    else:
        break
