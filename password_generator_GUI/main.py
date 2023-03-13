# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
from tkinter import *
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image = logo)
canvas.grid(column=1, row=0)

### Labels ###
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)


### Text ####
website_input = Entry(width=50)
website_input.grid(row=1, column=1, columnspan=2)
website_input.focus()

email_input = Entry(width=50)
email_input.grid(row=2, column=1, columnspan=2)
email_input.insert("latuchavan@gmail.com")

password = Entry(width=32)
password.grid(row=3, column=1)


### Buttons ###
add = Button(text="Add", width=43)
add.grid(column=1, row=4, columnspan=2)

generate_pass = Button(text="Generate Password")
generate_pass.grid(column=2, row=3)

window.mainloop()
