def prime_checker(number):
    prime_num = True
    for i in range (2, number):
        if number % i == 0:
            prime_num = False

    if prime_num:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")
        
    
n = int(input("Check this number: "))
prime_checker(number=n)
