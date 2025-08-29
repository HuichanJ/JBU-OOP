grade1 = int(input("Type grade"))
grade2 = int(input("Type grade"))
grade3 = int(input("Type grade"))
grade4 = int(input("Type grade"))
grade5 = int(input("Type grade"))

total = (grade1+grade2+grade3+grade4+grade5)
avg = total/5

if avg >= 90:
    print("A")
elif avg >= 80:
    print("B")
elif avg >= 70:
    print("C")
elif avg >= 60:
    print("D")
elif avg < 60:
    print("F")
elif avg < 0:
    print("You have a negative grade")
