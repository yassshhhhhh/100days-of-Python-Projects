#Exception Handling

# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["key"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist.")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise TypeError("This is an error that I made up.")

#BMI Example

# height = float(input("Height: "))
# weight = int(input("Weight: "))

# if height > 3:
#     raise ValueError("Human Height should not be over 3 meters.")

# if weight > 200:
#     raise ValueError("Human Height should not be over 3 meters.")

# bmi = weight / height ** 2
# print(bmi)


# facebook_posts = eval(input())

# total_likes = 0
# # Catching the KeyError exception in the dictionary
# for post in facebook_posts:
#   try:
#     total_likes = total_likes + post['Likes']
#   except KeyError:
#     pass 

# print(total_likes)

# **************************************************************************************************
# Errors and Exceptional Handling with Password Manager.

from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

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
    # print(password)
    password_entry.insert(0, password)
    pyperclip.copy(password)  # Copies password to clip board


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    username = username_entry.get()
    password = password_entry.get()
    website = website_entry.get()
    new_data = {website: {
        "Email/Username": username,
        "Password": password
    }}
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"These are the details entered: \nEmail: {username}\nPassword: {password}\nIs it okay to save?")
        if is_ok:
            try:    # First Implements this code.
                with open("data.json", "r") as file:
                    # reading the old file
                    data = json.load(file)
            except FileNotFoundError:   # If the try block gives an error of FileNotFound, then Implement this block of code.
                with open("data.json", "w") as file:
                    json.dump(new_data, file, indent=4)
            else:   # If there is no error found in try block, then Implement this block of code.
                # Updating old data with new data
                data.update(new_data)

                with open("data.json", "w") as file:
                    # Saving updated data
                    json.dump(data, file, indent=4)
            finally:    # Always implement this code.
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ----------------------------  SEARCH PASSWORD ------------------------------- #
def search_password():
    website = website_entry.get()
    if len(website) == 0:
        messagebox.showinfo(title="Info", message="Please enter website.")
    else:
        try:
            with open("data.json", "r") as file:
                # reading the old file
                data = json.load(file)
        except FileNotFoundError:  # If the try block gives an error of FileNotFound, then Implement this block of code.
            messagebox.showinfo(title="Error", message="No data file found.")
        else:
            if website in data:
                messagebox.showinfo(title=website,
                                    message=f"Email/Username: {data[website]['Email/Username']}\nPassword: {data[website]['Password']}")
            else:
                messagebox.showinfo(title="Info", message=f"No details for the {website} exists.")


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
website_entry = Entry(width=25)
website_entry.focus()
website_entry.grid(column=1, row=1, sticky='w')

username_entry = Entry(width=36)
username_entry.insert(0, string="Yashraj@gmail.com")
username_entry.grid(column=1, row=2)

password_entry = Entry(width=17)
password_entry.grid(column=1, row=3, sticky='w')

# Buttons
search_button = Button(text="   search   ", command=search_password)
search_button.grid(column=1, row=1, sticky='e')

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=1, row=3, sticky='e')

add_button = Button(text="Add", width=30, command=save_password)
add_button.grid(column=1, row=4)

window.mainloop()

