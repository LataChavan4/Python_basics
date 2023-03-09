from tkinter import *

windows = Tk()
windows.minsize(width=200, height=70)
windows.title("Mile to Km converter")
windows.config(padx=50)


def miles_to_km():
    miles_input = float(user_input.get())
    kilom = miles_input*1.609
    converted_km.config(text=f"{kilom}")


user_input = Entry(width=10)
user_input.insert(END,string="0")
user_input.grid(column=1, row=0)

miles = Label(text="Miles", font=("Aerial", 10))
miles.grid(column=2, row=0)

Km = Label(text="Km", font=("Aerial", 10))
Km.grid(column=2, row=1)

equal_to = Label(text="equal to", font=("Aerial", 10))
equal_to.grid(column=0, row=1)

converted_km = Label(text="0", font=("Aerial", 10))
converted_km.grid(column=1, row=1)

convert = Button(text="Convert", command=miles_to_km)
convert.grid(column=1, row= 2)


windows.mainloop()
