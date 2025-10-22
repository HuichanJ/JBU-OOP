import numbers
from tkinter.tix import InputOnly


class Student:
    def __init__(self):
        self.StuID = ""
        self.StuName = ""
        self.Major = ""
        self.GPA = 0.0
        self.DOB = ""
        self.Course = []

    def addStudent(self):
        self.StuID = input("Enter Student ID")
        self.StuName = input("Enter Student Name")
        self.Major = input("Enter Major")
        self.GPA = float(input("Enter Student GPA"))
        self.DOB = input("Enter Date of Birth")

    def editStudent(self):
        self.StuID = input("Enter Student ID")
        self.StuName = input("Enter Student Name")
        self.Major = input("Enter Major")
        self.GPA = float(input("Enter Student GPA"))
        self.DOB = input("Enter Date of Birth")

    def display(self):
        print("Student ID : ", self.StuID,
              "\nName : ", self.StuName,
              "\nMajor : ", self.Major,
              "\nGPA : ", self.GPA,
              "\nDate of Birth : ", self.DOB)
        for x in self.Course:
            print("Course Registered: ", x.CourseName)

    def registerCourse(self, c1):
        self.Course.append(c1)



class Course:
    def __init__(self):
        self.CourseID = ""
        self.CourseName = ""

    def addCourse(self):
        self.CourseID = input("Enter Course ID")
        self.CourseName = input("Enter Course Name")

#=======================================================================================================================

s1 = Student()
s1.addStudent()
s1.display()

n = int(input("How many Courses would you like to add?"))


for x in range(0, n):
    c = Course()
    c.addCourse()
    s1.registerCourse(c)


s1.display()
