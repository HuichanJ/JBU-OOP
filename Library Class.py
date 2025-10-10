from encodings.punycode import insertion_unsort


class Book:
    def __init__(self):
        self.myBook = {}
        self.BookID = ""
        self.publisher = ""
        self.Title = ""
        self.Author = ""
        self.publication = ""


    def addBook(self):

        self.BookID = input("Enter Book ID")
        self.Title = input("Enter Book Title")
        self.Author = input("Enter Author ID")
        self.publisher = input("Enter Publisher")
        self.publication = input("Enter Publication")

        self.myBook = {self.BookID:{"Title: ":self.Title,"Author: ":self.Author,
                               "Book ID: ":self.BookID, "Publisher: ": self.publisher,
                               "Publication: ": self.publication}}


    def display(self):
        print(self.myBook[input("Enter Book ID")])

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

    def display(self):
        id = input("Enter Author ID")
        print(self.myAuthor[id])


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


    def BorrowBooks(self):
        self.myUser[input("Enter ID")]["Books Borrowed: "].append(input("Enter Book ID"))

    def display(self):
        id = input("Enter User ID")
        print(self.myUser[id])



#=======================================================================================================================
Users = User()
Authors = Author()
Books = Book()


while True:
    print("1. Add User\n"
          "2. Add Author\n"
          "3. Add Book\n"
          "4. BorrowBooks\n"
          "5. Display\n"
          "Type any other number to Exit")
    n = int(input("Choose your option"))
    if n == 1:
        Users.addUser()

    elif n == 2:
        Authors.addAuthor()

    elif n == 3:
        Books.addBook()

    elif n == 4:
        Users.BorrowBooks()

    elif n == 5:
        while True:
            print("1. Display User\n"
                  "2. Display Author\n"
                  "3. Display Books\n"
                  "4. Display Borrowed Books\n"
                  "Any number to go back to menu")
            n1 = int(input("Enter your option"))
            if n1 == 1:
                Users.display()
            elif n1 == 2:
                Authors.display()
            elif n1 == 3:
                Books.display()
            elif n1 == 4:
                for x in Users.myUser[input("Enter user ID")]["Books Borrowed: "]:
                    print("Books Borrowed: ", Books.myBook[x]["Title: "])
            else:
                break
    else:
        break


