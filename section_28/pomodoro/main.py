import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    title_lbl.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    ticks_lbl.config(text="")
    global reps
    reps = 0
    start_btn["state"] = "active"


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_in_seconds = WORK_MIN * 60
    short_break_in_seconds = SHORT_BREAK_MIN * 60
    long_break_in_seconds = LONG_BREAK_MIN * 60

    if reps % 2 == 1:
        count_down(work_in_seconds)
        title_lbl.config(text="Work", foreground=GREEN)
    elif reps == 8:
        count_down(long_break_in_seconds)
        title_lbl.config(text="Break", foreground=RED)
    elif reps % 2 == 0:
        count_down(short_break_in_seconds)
        title_lbl.config(text="Break", foreground=PINK)
    start_btn["state"] = "disabled"


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_minutes = math.floor(count / 60)
    count_seconds = count % 60

    if count_minutes < 10:
        count_minutes = f"0{count_minutes}"

    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"
    canvas.itemconfig(timer_text, text=f"{count_minutes}:{count_seconds}")

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✓"
        ticks_lbl.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
background_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=background_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 28, "bold"))
canvas.grid(column=1, row=1)

# Title Label - "Timer"
title_lbl = Label(text="Timer", font=(FONT_NAME, 50))
title_lbl.grid(column=1, row=0)
title_lbl.config(foreground=GREEN, background=YELLOW)

# Start Button
start_btn = Button(text="Start", font=(FONT_NAME, 10, "bold"), command=start_timer)
start_btn.config(background="white", borderwidth=0)
start_btn.grid(column=0, row=2)

# Reset Button
reset_btn = Button(text="Reset", font=(FONT_NAME, 10, "bold"))
reset_btn.config(background="white", borderwidth=0, command=reset_timer)
reset_btn.grid(column=2, row=2)

# Green Ticks Label
ticks_lbl = Label(font=(FONT_NAME, 15, "bold"))
ticks_lbl.config(foreground=GREEN, background=YELLOW, borderwidth=0)
ticks_lbl.grid(column=1, row=3)

window.mainloop()
