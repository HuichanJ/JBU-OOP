from tokenize import String
from xml.etree.ElementTree import tostring


class Customer:
    cID = ""
    accNo = ""
    cName = ""
    phone = ""
    emailID = ""
    balance = 0.0
    card = []

    def __init__(self):
        self.cID = input("Enter Customer ID")
        self.accNo = input("Enter Account Number")
        self.cName = input("Enter Customer Name")
        self.phone = input("Enter Phone Number")
        self.emailID = input("Enter Email ID")
        self.balance = int(input("Enter Initial Balance"))

    def debit(self, m):
       self.balance -= m

    def credit(self, m):
        self.balance += m

    def assignCard(self, cardID):
        self.card.append(cardID)

    def display(self):
        print("Customer ID: ", self.cID,
              "\nAccount Number: ", self.accNo,
              "\nCustomer Name: ", self.cName,
              "\nPhone Number: ", self.phone,
              "\nEmail Account: ", self.emailID,
              "\nBalance: ", self.balance,
              "\nCard No.: ", self.card)


class Card:

    cardNo = ""
    cvv = ""
    expiryDate = ""
    balance = 0.0

    def __init__(self):
        self.cardNo = input("Enter Card Number")
        self.cvv = input("Enter CVV Number")
        self.expiryDate = input("Enter Expiry Date")
        self.balance = int(input("Enter Balance"))



    def display(self):
        print("CardNo: ", self.cardNo,
              "CVV: ", self.cvv,
              "ExpiryDate: ", self.expiryDate,
              "Balance: ", self.balance)



        #=============================================================================================================

import pickle



while 1:
    print("1. Create Customer Object\n"
          "2. Create Card Object\n"
          "3. Transfer fund between customer object\n"
          "4. Assign card objects to customer objects\n"
          "5. Display Customer info\n"
          "6. Display Card info\n"
          "7.Commit\n"
          "8.Exit")

    option = int(input("Enter Option"))

    if option == 1:
        c1 = Customer()
        c2 = Customer()

    elif option == 2:
        card1 = Card()
        card2 = Card()

    elif option == 3:
        id = input("Enter Your Customer ID")
        id2 = input("Enter Customer acc to debit")
        amount = int(input("Enter amount to debit"))

        if c1.cID == id:
            if c2.cID == id2:
                c1.debit(amount)
                c2.credit(amount)
            else:
                print("Somethings wrong")

        elif c2.cID == id:
            if c1.cID == id2:
                c2.debit(amount)
                c1.credit(amount)
            else:
                print("Somethings wrong")

        else: print("somethings wrong")

    elif option == 4:
        id = input("Enter Your Customer ID")
        card = input("Enter Card Number")
        if c1.cID == id:
            c1.assignCard(card)
        elif c2.cID == id:
            c2.assignCard(card)
        else:
            print("Somethings wrong")

    elif option == 5:
        id = input("Enter Your Customer ID")
        if c1.cID == id:
            c1.display()
        elif c2.cID == id:
            c2.display()
        else:
            print("Somethings wrong")

    elif option == 6:
        id = input("Enter Your Card Number")
        if card1.cardNo == id:
            card1.display()
        elif card2.cardNo == id:
            card2.display()
        else:
            print("Somethings wrong")

    elif option == 7:
        f = open("CustomerList.dat", "ab")
        pickle.dump(c1, f)
        pickle.dump(c2, f)
        pickle.dump(card1, f)
        pickle.dump(card2, f)
        f.close()

    elif option == 8:
        break