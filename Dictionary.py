myStudent = {"s1":"Abby", "s2":"Brian", "s3":"Cyan"}
myStudent.update({"s4":"Darry"})
myStudent.update({"s5":"Eddy"})

print(myStudent)

del myStudent["s3"]
myStudent.update({"s1":"Jimmy"})

print(myStudent["s1"])
