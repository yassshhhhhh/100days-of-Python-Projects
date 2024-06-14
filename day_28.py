from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
Reps = 0
Timer = ''
# ---------------------------- TIMER RESET ------------------------------- # 


def reset():
    print("Resets Timer")
    window.after_cancel(Timer)
    global Reps
    Reps = 0
    timer.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    check_mark.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start():
    global Reps
    # print("Starts Timer")
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    Reps += 1
    if Reps % 8 == 0:
        timer.config(text="Break", fg=RED)
        count_down(long_break_sec)
    elif Reps % 2 == 0:
        timer.config(text="Break", fg=PINK)
        count_down(short_break_sec)
    else:
        timer.config(text="Work", fg=GREEN)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(num):
    # print(num)
    count_min = math.floor(num/60)
    # print(count_min)
    count_sec = num % 60
    # print(count_sec)
    if count_sec <= 9:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if num > 0:
        global Timer
        Timer = window.after(1000, count_down, num - 1)
    else:
        start()
        marks = ""
        work_sessions = math.floor(Reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        check_mark.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


# Label
timer = Label(text="Timer", font=(FONT_NAME, 34, "bold"), fg=GREEN, bg=YELLOW)
timer.grid(column=1, row=0)

check_mark = Label(font=(FONT_NAME, 14), fg=GREEN, bg=YELLOW)
check_mark.grid(column=1, row=3)

# Canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
# tomato_img = PhotoImage(file="tomato.png")
# canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 28, "bold"), fill="black")
canvas.grid(column=1, row=1)

# Buttons

# calls command when pressed
start_button = Button(text="Start", command=start, width=8, highlightthickness=0)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset, width=8, highlightthickness=0)
reset_button.grid(column=2, row=2)

window.mainloop()
