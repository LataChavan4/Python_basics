class Library:
    def __init__(self, library_name, book_list):
        self.library_name = library_name
        self.book_list = book_list
        self.records = {}


    def display(self):
        print(self.book_list)

    def add(self):
        book = input("Enter the book name: ")
        self.book_list.append(book)
        print('Here is the list of updated books')

    def lend(self):
        book = input("Enter the book name: ")
        if book not in self.book_list:
            print('Sorry the book you want to read is not available here')
        elif book in self.book_list:
            name = input('Enter your name: ')
            self.book_list.remove(book)
            self.records[book] = name
            print(f"This book has been allocated to you {self.records}")
        else:
            print(f"The book you want to read is with {self.records[book]}")    


    def ret(self):
         book = input("Enter the book name: ")
         self.book_list.append(book)
         self.records[book] = 'Available'
         print("Your book has been submitted successfully")

Dyanda_Library = Library('Dyanda_Library', ['Yayati','Mrutunjay','Chava','Champak'])
while True:
    action = input("Please select any one option from below list\n quit\n add\n lend\n return\n")
    if action == 'quit':
        break
    elif action == 'add':
        Dyanda_Library.add()
        Dyanda_Library.display()
    elif action == 'lend':
        Dyanda_Library.display()
        Dyanda_Library.lend()
    elif action == 'return':
        Dyanda_Library.ret()
    else:
        print("please enter valid input")


    print('Thank You..!! for visiting our library\n')
    


