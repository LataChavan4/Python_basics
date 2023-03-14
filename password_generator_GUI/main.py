from tkinter import *
from tkinter import messagebox

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = random.randint(8, 10)
nr_symbols = random.randint(2, 4)
nr_numbers = random.randint(2, 4)

password_list = []

for char in range(nr_letters):
  password_list.append(random.choice(letters))

for char in range(nr_symbols):
  password_list += random.choice(symbols)

for char in range(nr_numbers):
  password_list += random.choice(numbers)

random.shuffle(password_list)

password = ""
for char in password_list:
  password += char

print(f"Your password is: {password}")
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    pswrd = password.get()
    id = email_input.get()
    site = website_input.get()
    if len(pswrd) == 0 or len(id) == 0 or len(site) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any field empty")
    else:
        con = messagebox.askokcancel(title=site, message=f"The details entered are as follows:\n email: {id}\n password: {pswrd}")
        if con:
            with open ("data.txt", "a") as f:
                f.write(f" {site} | {id} | {pswrd}\n")
            password.delete(0, END)
            website_input.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
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
#### To put cursor in entry box ###
website_input.focus()

email_input = Entry(width=50)
email_input.grid(row=2, column=1, columnspan=2)
### 0/END represents index at which we want to display cursor ###
email_input.insert(0, "latuchavan@gmail.com")

password = Entry(width=32)
password.grid(row=3, column=1)


### Buttons ###
add = Button(text="Add", width=43, command=save)
add.grid(column=1, row=4, columnspan=2)

generate_pass = Button(text="Generate Password")
generate_pass.grid(column=2, row=3)

window.mainloop()
