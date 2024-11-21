import tkinter as tk
from tkinter import Label

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------GLOBAL VARIABLES----------------------#
timer_running = False
timer_count = 0
timer_after_id = None
pomodoro_count = 0

# ---------------------------- TIMER RESET ------------------------------- #
def reset_mechanism():
    global timer_running, timer_count, timer_after_id, pomodoro_count
    window.after_cancel(timer_after_id)
    timer_running = False
    timer_count = 0
    pomodoro_count = 0
    canvas.itemconfig(timer, text="00:00")
    timer_label.config(text="Timer")
    check_marks.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global timer_running, pomodoro_count
    if not timer_running:
        timer_running = True
        pomodoro_count += 1
        if pomodoro_count % 8 == 0:
            count_mechanism(LONG_BREAK_MIN * 60)
            timer_label.config(text="Long Break", fg=RED)
        elif pomodoro_count % 2 == 0:
            count_mechanism(SHORT_BREAK_MIN * 60)
            timer_label.config(text="Short Break", fg=PINK)
        else:
            count_mechanism(WORK_MIN * 60)
            timer_label.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_mechanism(count):
    global timer_running, timer_count, timer_after_id
    timer_count = count
    minutes = count // 60
    seconds = count % 60
    canvas.itemconfig(timer, text=f'{minutes:02d}:{seconds:02d}')
    if count > 0 and timer_running:
        timer_after_id = window.after(1000, count_mechanism, count - 1)
    elif count == 0:
        timer_running = False
        start_timer()
        marks = "✅" * (pomodoro_count // 2)
        check_marks.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro")
window.geometry('500x500')
window.config(padx=100, pady=100, bg=YELLOW)

canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tk.PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer = canvas.create_text(103, 105, text='00:00', fill='white', font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

timer_label = tk.Label(master=window, text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 25, "bold"))
timer_label.grid(row=0, column=1)

start_button = tk.Button(master=window, text='Start', font=(FONT_NAME, 10), highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = tk.Button(master=window, text='Reset', font=(FONT_NAME, 10), highlightthickness=0, command=reset_mechanism)
reset_button.grid(row=2, column=2)

check_marks = Label(text="", fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

window.mainloop()
