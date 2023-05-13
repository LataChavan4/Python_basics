from tkinter import *
import pandas
import random
import time

import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
WHITE = "#FFFFFF"
current_card={}


## reading csv file ##
try:
    data = pandas.read_csv("to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("./data/french_words.csv")
    word_dict = original_data.to_dict(orient="records")
else:
    word_dict = data.to_dict(orient="records")

##Fuction to get new word##
def next_word():
    global current_card, flip_timer, word_dict
    window.after_cancel(flip_timer)    ### to avoid getting incorrect word after flip ###
    current_card = random.choice(word_dict)
    canvas.itemconfig(card_background, image=card_front)
    canvas.itemconfig(lang, text="French", fill="Black")
    canvas.itemconfig(word, text= current_card["French"], fill="Black")
    flip_timer = window.after(3000, func=flip_card)

#Function to flip card ###
def flip_card():
    canvas.itemconfig(card_background, image=card_back)
    canvas.itemconfig(lang, text="English", fill=WHITE)
    canvas.itemconfig(word, text=current_card["English"], fill=WHITE)

 ##Function to remove word from list
def is_known():
    global current_card, word_dict
    word_dict.remove(current_card)
    print(len(word_dict))
    to_learn = pd.DataFrame(word_dict)
    to_learn.to_csv("to_learn.csv", index=False)
    next_word()


#word_dict = {row.French: row.English for (index, row) in data.iterrows()}
print(word_dict)
## Creating window ##
window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
flip_timer = window.after(3000, func=flip_card)

## Creating canvas and placing other elements on it ##
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

card_front = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file="./images/card_back.png")
card_background= canvas.create_image(400, 263, image=card_front)

## Texts ##

lang = canvas.create_text(400, 150, text="Title", font=("Aerial", 40, "italic"))
word = canvas.create_text(400, 250, text="word", font=("Aerial", 60, "bold"))

#Buttons###

right_image = PhotoImage(file="./images/right.png")
right = Button(image=right_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=is_known)
right.grid(column=1, row=1)
wrong_image= PhotoImage(file="./images/wrong.png")
wrong = Button(image=wrong_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=next_word)
wrong.grid(column=0, row=1)

next_word()


window.mainloop()  ## will keep screen untiol we close it##
