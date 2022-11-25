import random
systemno=random.randint(1,100)
count = 0
number=None
while (number!= systemno):
    count+=1
    number = int(input("Guess the number between 1 to 100: "))
    if (number==systemno):
        print("You guessed it correctly")
    else:
        if number>systemno:
            print("You are wrong, its smaller than this number")
        else:
            print("You are wrong, its greater than this number")
    
print(f"You took {count} attempts to guess the number correctly")
