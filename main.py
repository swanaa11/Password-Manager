from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(numbers) for _ in range(randint(2, 4))]
    password_numbers = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letter + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    pass_entry.insert(0, password)
    pyperclip.copy(password)


def save():
    website = website_entry.get()
    mail = email_entry.get()
    password = pass_entry.get()
    new_data = {
        website: {
            "email": mail,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops",
                            message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            pass_entry.delete(0, END)
            email_entry.delete(0, END)


def find():
    website = website_entry.get()
    try:
        with open("data.json")as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email_1 = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email_1}, Password : {password}")
            pyperclip.copy(password)
        else:
            messagebox.showinfo(title="Error", message=f"No Details for {website} exists.")


window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=40, bg="black")

canvas = Canvas(width=200, height=200, bg="black", highlightthickness=0)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0)

web_label = Label(text="Website:", bg="black", fg="white")
web_label.grid(row=1, column=0)
email = Label(text="Email/Username:", bg="black", fg="white")
email.grid(row=2, column=0)
pass_label = Label(text="Password:", bg="black", fg="white")
pass_label.grid(row=3, column=0)

website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
pass_entry = Entry(width=35)
pass_entry.grid(row=3, column=1)

search = Button(text="Search", bg="black", fg="white", width=30, command=find)
search.grid(row=4, column=1, columnspan=2)
pass_button = Button(text="Generate Password", width=30, bg="black", fg="white", command=generate)
pass_button.grid(row=5, column=1, columnspan=2)
add = Button(text="Add", width=30, bg="black", fg="white", command=save)
add.grid(row=6, column=1, columnspan=2)

window.mainloop()
