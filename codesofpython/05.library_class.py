class Library:
    def __init__(self,library_name,book_list):
        self.library_name = library_name
        self.book_list = book_list

    def display(self):
        print(self.book_list)

    def add(self):
        book = input("Enter the book name: ")
        self.book_list.append(book)

    def lend(self):
        book = input("Enter the book name: ")
        if book not in book_list:
            print('Sorry the book you want to read is not available here')
        elif book in self.book_list:
             self.book_list[book] = Name
             print("This book has been allocated to you")
        else:
            print("The book you want to read is with other user")    


    def ret(self):
         book = input("Enter the book name: ")
         book_list[book] ='Available'

Dyanda_Library = Library('Dyanda_Library', ['Yayati','Mrutunjay','Chava','Champak'])
while True:
    action = input("Please select any one option from below list\n quit\n add\n lend\n return\n")
    if action == 'quit':
        break
    elif action == 'add':
        Dyanda_Library.add()
    elif action == 'lend':
        Dyanda_Library.display()
        Dyanda_Library.lend()
    elif action == 'return':
        Dyanda_Library.ret()
    else:
        print("please enter valid input")
    



