import random # Random module will be used to take input from computer

# Defining game rules
def gamewin(comp,you):
    if comp == you:
        return None
    elif comp == 's':
        if you == 'w':
             return False
        elif you == 'g':
            return True
    elif comp == 'w':
        if you == 's':
         return True
        elif you == 'g':
         return False
    elif comp == 'g':
        if you == 's':
            return False
        elif you == 'w':
             return True


# computer will select one option out of snake, water, gun

randomno = random.randint(1,3)
if randomno == 1:
    comp = 's'
elif randomno == 2:
    comp = 'w'
elif randomno == 3:
    comp = 'g'

# Input taken from user    
you = input("you choose snake(s) or water(W) or gun(g)?")
a = gamewin(comp, you)
print(f"Computer choose {comp}")  # will show option selected by computer
print(f"You choose {you}") # will show option selected by user


# will dislplay result of the game
if a == None:
    print("Its a Tie!")
elif a == True:
    print("You Win!")
elif a == False:
    print("You lose..")





