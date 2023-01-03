
import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)
l1 =[]

for letter in chosen_word:
    l1 +="_"
while "_" in l1:
    guess = (input("Guess the letter: ")).lower()
    for i in range (len(chosen_word)):
        for letter in chosen_word:
            if chosen_word[i] == guess:
                l1[i] = guess
        
    print(l1)
print("You won")