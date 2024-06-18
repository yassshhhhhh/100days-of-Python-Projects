from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

# Flash Cards - To learn languages efficiently.
# ------------------------------------------- Reading CSV files -------------------------------------------------------------
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, timer_flip
    window.after_cancel(timer_flip)
    current_card = random.choice(to_learn)
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=current_card["French"], fill="black")
    canvas.itemconfig(canvas_image, image=card_front_image)
    timer_flip = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(canvas_image, image=card_back_image)
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=current_card["English"], fill="white")


def is_known():
    print(current_card)
    to_learn.remove(current_card)
    print(len(to_learn))
    data_ = pandas.DataFrame(to_learn)
    data_.to_csv("data/words_to_learn.csv", index=False)
    next_card()


# ------------------------------------------- UI Setup -------------------------------------------------------------
window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
timer_flip = window.after(3000, func=flip_card)

# Images
right_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")
card_back_image = PhotoImage(file="images/card_back.png")
card_front_image = PhotoImage(file="images/card_front.png")

# Canvas
canvas = Canvas(width=800, height=528,highlightthickness=0, background=BACKGROUND_COLOR)
canvas_image = canvas.create_image(400, 263, image=card_front_image)
canvas.grid(column=0, row=0, columnspan=2)

title_text = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"), fill="black")
word_text = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"), fill="black")

# Buttons
right_button = Button(image=right_image, highlightthickness=0, command=is_known)
right_button.grid(column=1, row=1)
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)

next_card()

window.mainloop()
