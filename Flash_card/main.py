from tkinter import *
import pandas
import random
import time

BACKGROUND_COLOR = "#B1DDC6"
WHITE = "#FFFFFF"
current_card={}
def next_word():
    global current_card
    current_card= random.choice(word_dict)
    canvas.itemconfig(card_background, image=card_front)
    canvas.itemconfig(lang, text="French", fill="Black")
    canvas.itemconfig(word, text= current_card["French"], fill="Black")
    window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_background, image=card_back)
    canvas.itemconfig(lang, text="English", fill=WHITE)
    canvas.itemconfig(word, text=current_card["English"], fill=WHITE)


## reading csv file ##
data = pandas.read_csv("./data/french_words.csv")
word_dict= data.to_dict(orient="records")
#word_dict = {row.French: row.English for (index, row) in data.iterrows()}
print(word_dict)
## Creating window ##
window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)


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
right = Button(image=right_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=next_word)
right.grid(column=1, row=1)
wrong_image= PhotoImage(file="./images/wrong.png")
wrong = Button(image=wrong_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=next_word)
wrong.grid(column=0, row=1)

next_word()


window.mainloop()
