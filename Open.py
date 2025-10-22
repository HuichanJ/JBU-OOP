file1 = open("Test1", "w")

file1.writelines("1. Say \"hi\"\n")
file1.writelines("2. Look for your phone\n")
file1.writelines("3. Leave\n")

file1.close()

file2 = open("Test1", "r")

for line in file2:
    print(line)

file2.close()

import pickle

d = {"s1":{"Random1":"heh", "Random2":"hehe", "Random3":"heheh", "raandomm":"hehehehe"},
     "s2":{"Random1":"heh", "Random2":"hehe", "Random3":"heheh", "raandomm":"hehehehe"},
     "s3":{"Random1":"heh", "Random2":"hehe", "Random3":"heheh", "raandomm":"hehehehe"},
     "s4":{"Random1":"heh", "Random2":"hehe", "Random3":"heheh", "Random4":"hehehehe"}}

with open("Dictionary.dat", "wb") as file3:
    pickle.dump(d, file3)

file3.close()

file4 = open("Dictionary.dat", "rb")

Dictionary2 = pickle.load(file4)

file4.close()

for x in Dictionary2["s1"]:
    print(x)


i=1
for x in d:
    val = "s"+str(i)
    print(d[val]["Random"+str(i)])
    i+=1

while True:
    if Dictionary2[input("Enter Student ID")]["Random3"] == input("Enter Password"):
        print("Successfully logged in")
        break
    else:
        print("Wrong Password")



