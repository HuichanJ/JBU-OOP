from encodings.punycode import insertion_unsort


class Book:
    def __init__(self):
        self.myBook = {}
        self.BookID = ""
        self.publisher = ""
        self.Title = ""
        self.Author = ""
        self.publication = ""


    def addBook(self, a1):

        self.BookID = input("Enter Book ID")
        self.Title = input("Enter Book Title")
        self.Author = a1
        self.publisher = input("Enter Publisher")
        self.publication = input("Enter Publication")

        self.myBook = {self.BookID:{"Title: ":self.Title,"Author: ":self.Author,
                               "Book ID: ":self.BookID, "Publisher: ": self.publisher,
                               "Publication: ": self.publication}}


    def display(self):
        print("Book ID: ", self.BookID,
              "\nBook Title: ", self.Title,
              "\nBook Author: ", self.Author,
              "\nPublisher :", self.publisher,
              "\nPublication :", self.publication)

class Author:
    def __init__(self):
        self.myAuthor = {}
        self.AuthorID = ""
        self.AuthorName = ""
        self.Affiliation = ""
        self.country = ""
        self.phone = ""
        self.emailID = ""

    def addAuthor(self):
        self.AuthorID = input("Enter author id")
        self.AuthorName = input("Enter Author Name")
        self.Affiliation = input("Enter Affiliation")
        self.country = input("Enter country")
        self.phone = input("Enter Phone Number")
        self.emailID = input("Enter Email ID ")

        self.myAuthor = {self.AuthorID:{"Name: ":self.AuthorName, "Affiliation: ":self.Affiliation,
                                        "Country: ":self.country, "Phone Number: ":self.phone,
                                        "Email ID: ":self.emailID}}



class User:
    def __init__(self):
        self.myUser = {}
        self.userID = ""
        self.userName = ""
        self.bookBorrowed = []
        self.emailID = ""
        self.passWord = ""
        self.phone = ""

    def addUser(self):
        self.userID = input("Enter User ID")
        self.userName = input("Enter USer Name")
        self.emailID = input("Enter Email ID")
        self.passWord = input("Enter Password")
        self.phone = input("Enter Phone Number")

        self.myUser = {self.userID:{"Name :":self.userName, "Email ID: ":self.emailID,
                                    "Password: ":self.passWord, "Phone Number: ":self.phone,
                                    "Books Borrowed: ":self.bookBorrowed}}


    def BorrowBooks(self, b1):
        self.bookBorrowed.append(b1)

    def display(self):
        id = input("Enter User ID")
        print(self.myUser[id])

    def displayBorrowedBooks(self):
        id = input("Enter User ID")
        for x in self.myUser[id]["Books Borrowed: "]:
            print("Borrowed Book: ", x)

#=======================================================================================================================

while True:
    print("1. Add User\n"
          "2. Add Author\n"
          "3. Add Book\n"
          "4. BorrowBooks\n"
          "Type any other number to Exit")
    n = int(input("Choose your option"))
    if n == 1:
