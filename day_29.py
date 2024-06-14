from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_password():
    nr_letters_list = [choice(letters) for _ in range(randint(8, 18))]
    nr_symbols_list = [choice(symbols) for _ in range(randint(2, 4))]
    nr_numbers_list = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = nr_letters_list + nr_symbols_list + nr_numbers_list
    shuffle(password_list)
    password = "".join(password_list)
    print(password)
    password_entry.insert(0, password)
    pyperclip.copy(password)  # Copies password to clip board


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    username = username_entry.get()
    password = password_entry.get()
    website = website_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"These are the details entered: \nEmail: {username}\nPassword: {password}\nIs it okay to save?")
        if is_ok:
            with open("data.txt", "a") as file:
                file.write(f"{website} | {username} | {password}\n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Canvas
canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(60, 100, image=lock_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Entries
website_entry = Entry(width=36)
website_entry.focus()
website_entry.grid(column=1, row=1)

username_entry = Entry(width=36)
username_entry.insert(0, string="Yashraj@gmail.com")
username_entry.grid(column=1, row=2)

password_entry = Entry(width=17)
password_entry.grid(column=1, row=3, sticky='w')

# Buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=1, row=3, sticky='e')

add_button = Button(text="Add", width=30, command=save_password)
add_button.grid(column=1, row=4)

window.mainloop()
