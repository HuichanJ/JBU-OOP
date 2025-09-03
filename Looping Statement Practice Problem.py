p = int(input("Print the principal loan amount : "))
r = int(input("Type the rate of interest : "))
n = int(input("Type the duration of loan : "))

r = r/12*100

emi = p * r * ((1+r)**n)/((1+r)**n - 1)
print("Monthly repayment : ", emi)

for number in range (1, n):
    print("emi: ", emi, "\nBalance:", p - emi)
    p = p - emi

