
book_list = {'ikigai': 'available',
                'alchemist':'lata',
                'atomic Habit' : 'available',
                'secrets': 'sagar' }
name = input('Please Enter your userid: ')
request = input("Enter the book you want to read: ")

if (book_list.get(request)) == 'Available':
    print(f" Book you want to read is available")
    confirmation = input("Please type Y to confirm your booking: ")
    if confirmation == 'Y':
        book_list[request] = name
        print("Book has been alloted to you, Thank you for visiting our library")
elif (book_list.get(request)) == 'None':
    print("Sorry the book you want to read is not available in our library, will try to get it as soon as possible\n")
else:
    print(f"Sorry..The book you want to read is with {(book_list.get(request))} we will notify you once its available")


    



# if request in available_books:
#     print(f"{request} is available in library et me check current its status")
# else:
#     print(f"Sorry..{request} is not available in this library")



