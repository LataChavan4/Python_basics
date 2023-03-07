## Read data from csv file ##
data = pandas.read_csv("nato_phonetic_alphabet.csv")
alphabets = data.to_dict()

# creating dictionary in below format ##
#{"A": "Alfa", "B": "Bravo"}
alpha = {row.letter : row.code for (index, row) in data.iterrows()}


# Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter the word: ").upper() ## converting user input into uppercase ##
phonetic_code = []
for letter in user_input:
    phonetic_code.append(alpha[letter])

print(phonetic_code)
