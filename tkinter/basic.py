from tkinter import *
def add(*args):
    total = 0
    for n in args:
        total += n
    return total

print(add(5,4,6,9,7))

screen = Tk()
screen.title("First GUI program")
screen.minsize(width=300, height=300)

my_label = Label(text="label", font=("Aerial", 20, "bold"))
my_label.pack(side= "top")


input = Entry(width=10)
input.pack()

def button_clicked():
    my_label["text"] = input.get()
    print(input)

button = Button(text = "Click here",command= button_clicked)
button.pack()

mainloop()
