from gamedata import logo, vs, data
import random
print(logo)

def get_details(account):
    name = account['name']
    description = account ['description']
    country = account['country']
    return f"{name}, a {description}, from {country}"


def guess_follower(guess, a_follower, b_follower):
    if a_follower > b_follower:
        return guess == 'a'
    else:
        return guess == 'b'
def game():
    score = 0
    print(logo)
    continue_game = True

    account_b = random.choice(data)
    while continue_game:
        account_a = account_b
        account_b = random.choice(data)

        while account_a == account_b:
            account_b = random.choice(data)

        print(f"{get_details(account_a)}")
        print(vs)
        print(f"{get_details(account_b)}")

        a_follower = account_a['follower_count']
        b_follower = account_b['follower_count']

        guess = input("Who has more follower 'A' or 'B'? ").lower()

        is_correct=guess_follower(guess, a_follower, b_follower)

        if is_correct:
            score += 1
            print(f"You are correct, Current score is {score}")
        else:
            continue_game = False
            print(f"Sorry! that's wrong, final score is {score}")

game()




        
    
    


