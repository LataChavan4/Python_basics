import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
l1 = []
lives = 6
end_of_game = False
print(chosen_word)

for letter in chosen_word:
    l1 +="_"
while end_of_game is False:
    guess = input("Guess the letter: ").lower()
    for i in range (len(chosen_word)):
        if guess == chosen_word[i]:
            l1[i] = guess
    if guess not in chosen_word:
        lives -= 1
    print(l1)
    print(stages[lives])
    if lives == 0:
        end_of_game = True
        print("You Lose...")
    if "_"not in l1:
        print("You Win..!!")
            










