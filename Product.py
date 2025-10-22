from fileinput import close
from itertools import product
from marshal import dumps


class Product:
    def __init__(self):
        self.pid = ""
        self.pname = ""
        self.price =0.0
        self.description = ""

    def getProductDetails(self):
        self.pid = input("Enter Product ID")
        self.pname = input("Enter Product Name")
        self.price = int(input("Enter Price"))
        self.description = input("Enter any description")

    def display(self):
        print(self.pid, "\n",
              self.pname, "\n",
              self.price, "\n",
              self.description)



#=======================================================================================================================
import pickle
p = Product()

while True:
    print("1. Show a Menu\n"
          "2. Add info of product\n"
          "3. Display product\n"
          "4. Write the product into a file\n"
          "5. Read from the file\n"
          "6. Exit")
    option = int(input("Choose your option"))

    if option == 1:
        print("Product ID, Name, Price, Description")

    elif option == 2:
        p.getProductDetails()

    elif option == 3:
        p.display()

    elif option == 4:
        f1 = open("ProductInventory.dat", "ab")
        pickle.dump(p, f1)
        f1.close()

    elif option == 5:
        f2 = open("ProductInventory.dat", "rb")
        data = pickle.load(f2)
        for x in data:
            try:
                x.display()
            except EOFError:
                print("There was an Error")
                break


        f2,close()

    elif option == 6:
        break
