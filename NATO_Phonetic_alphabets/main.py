data = pandas.read_csv("nato_phonetic_alphabet.csv")
### converting csv file data to dictonary##
alphabets = data.to_dict()
print(data)


alpha = {row.letter : row.code for (index, row) in data.iterrows()}
print(alpha)



#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
phonetic_code = []
def code():
    user_input = input("Enter the word: ").upper()
    try:
        phonetic_code = [alpha[letter] for letter in user_input]
    except KeyError:
        print("Sorry only letters in alphabet please")
        code()
    else:
        print(phonetic_code)
code()
