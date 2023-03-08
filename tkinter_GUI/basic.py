from tkinter import *
def add(*args):
    total = 0
    for n in args:
        total += n
    return total

print(add(5,4,6,9,7))

## creating screen object and deciding its minimum size and its title ##
screen = Tk()
screen.title("First GUI program")
screen.minsize(width=300, height=300)

## creating lable and desiding its font and position on the screen ###
my_label = Label(text="label", font=("Aerial", 20, "bold"))
my_label.pack(side= "top")

## creating small window where user can provide input ##
input = Entry(width=10)
input.pack()


## creating click button on screen ##
def button_clicked():
    my_label["text"] = input.get()
    print(input)

button = Button(text = "Click here",command= button_clicked)
button.pack()

mainloop()
