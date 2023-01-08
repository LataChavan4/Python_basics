alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encrypt(direction, message, move):
    encrypted_text = ""
    for letter in text:
        position = alphabet.index(letter)
        if direction == "encode":
            new_position = position + shift
        if direction == "decode":
            new_position = position - shift
        encrypted_text += alphabet[new_position]
    print(f"Your encrypted message is {encrypted_text}")
    
end_loop = False
while end_loop == False:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = (int(input("Type the shift number:\n"))) % 26

    encrypt(direction, text, shift)
    repeat = input("Type 'yes' if you want to continue otherwise type 'no\n'")
    if repeat == "no":
            end_loop = True

