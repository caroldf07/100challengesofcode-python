import csv
import random
from tkinter import *

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
           'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    password_easy = ""
    number_letters = 6
    number_symbols = 3
    number_numbers = 3
    while number_letters > 0:
        password_easy += random.choice(letters)
        number_letters -= 1
    while number_symbols > 0:
        password_easy += random.choice(symbols)
        number_symbols -= 1
    while number_numbers > 0:
        password_easy += random.choice(numbers)
        number_numbers -= 1

    password_hard = ''.join(random.sample(password_easy, len(password_easy)))
    password_space.insert(0, password_hard)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    with open("db.csv", "a") as db:
        ws = website_space.get()
        email = email_username_space.get()
        pw = password_space.get()
        new_row = [ws, email, pw]
        writer_db = csv.writer(db)
        writer_db.writerow(new_row)
        website_space.delete(0, END)
        email_username_space.delete(0, END)
        password_space.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("LockerPassword")
canvas = Canvas(height=200, width=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)
window.config(padx=50, pady=50)

website = Label(text="Website:")
website.grid(row=1, column=0)
website_space = Entry(width=35)
website_space.grid(row=1, column=1, columnspan=2)

email_username = Label(text="Email/Username:")
email_username.grid(row=2, column=0)
email_username_space = Entry(width=35)
email_username_space.grid(row=2, column=1, columnspan=2)

password = Label(text="Password:")
password.grid(row=3, column=0)
password_space = Entry(width=21)
password_space.grid(row=3, column=1)
generate_password = Button(text="Generate Password", command=password_generator)
generate_password.grid(row=3, column=2)

save = Button(text="Save", width=36, command=save_password)
save.grid(row=4, column=1, columnspan=2)
window.mainloop()
