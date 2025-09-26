import math


def area_rect():
    l = int(input("Enter Length"))
    b = int(input("Enter Base"))
    print(l*b)

def vol_cube():
    l = int(input("Enter Length"))
    b = int(input("Enter Base"))
    h = int(input("Enter Height"))
    print(l*b*h)

def area_circle():
    r = int(input("Enter radius"))
    print(math.pi*r.__pow__(2))

def vol_circle():
    r = int(input("Enter radius"))
    print(math.pi * r * 2)

def vol_sphere():
    r = int(input("Enter radius"))
    print((4/3)*math.pi*r.__pow__(3))

#-----------------------------------------------------------------------------------------------------------------------
while 1:
    print("1. Area of Rectangle\n"
          "2. Volume of a cube\n"
          "3. Area of a circle\n"
          "4. Volume of a circle\n"
          "5. Volume of Sphere\n"
          "Type any other number to quit")
    Option = int(input("Choose from the Option"))

    if Option == 1:
        area_rect()

    elif Option == 2:
        vol_cube()

    elif Option == 3:
        area_circle()

    elif Option == 4:
        vol_circle()

    elif Option == 5:
        vol_sphere()

    else:
        break
