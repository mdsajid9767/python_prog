import sys

class Library:
    def __init__(self, listofbooks):
        self.availablebooks = listofbooks

    def displayavailablebooks(self):
        print("List of all books which is available.")
        # for b in self.availablebooks:
        #     print(b)
        print(self.availablebooks)

    def lendbook(self, requestbook):
        if requestbook in self.availablebooks:
            print("Book {} is borrowed".format(requestbook))
            self.availablebooks.remove(requestbook)
        else:
            print("Book {} is not present right now.".format(requestbook))

    def addbooks(self, returnedbook):
        self.availablebooks.append(returnedbook)
        print("Thanks for returning borrowed book!")

class Student:
    def requestbook(self):
        print("Enter the name of book you want to borrow:- ")
        self.book = input()
        return self.book

    def returnedbook(self):
        print("Enter the name of book you want to return:- ")
        self.book = input()
        return self.book

def main():
    lib = Library(["Java", "C++", "C", "DBMS", "Operating System"])
    student = Student()

    while(True):
        print(""" ============ LIBRARY MENU ============
        1. Display all available books
        2. Request a book
        3. Return a book
        0. Exit
        """)
        choice = int(input("Enter your choice:- "))
        if choice == 1:
            lib.displayavailablebooks()
        elif choice == 2:
            lib.lendbook(student.requestbook())
        elif choice == 3:
            lib.addbooks(student.requestbook())
        elif choice == 0:
            sys.exit()
main()