import tkinter as tk
import pandas as pd
import random
import os

# Constants
BACKGROUND_COLOR = "#B1DDC6"
DATA_FILE = "data/words_to_learn.csv"
ORIGINAL_FILE = "data/french_words.csv"

# Load data
try:
    data = pd.read_csv(DATA_FILE)
except FileNotFoundError:
    data = pd.read_csv(ORIGINAL_FILE)

to_learn = data.to_dict(orient="records")
current_card = {}

# Functions
def update_card(title, word, bg_image, title_color="black", word_color="black"):
    """Update card content dynamically."""
    canvas.itemconfig(card_title, text=title, fill=title_color)
    canvas.itemconfig(card_word, text=word, fill=word_color)
    canvas.itemconfig(card_background, image=bg_image)

def next_card():
    global current_card, flip_timer
    if not to_learn:
        update_card("Congratulations!", "You've learned all the words!", card_front_img)
        window.after_cancel(flip_timer)
        return
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    update_card("French", current_card["French"], card_front_img)
    flip_timer = window.after(3000, flip_card)

def flip_card():
    update_card("English", current_card["English"], card_back_img, title_color="white", word_color="white")

def is_known():
    to_learn.remove(current_card)
    pd.DataFrame(to_learn).to_csv(DATA_FILE, index=False)
    next_card()

# GUI Setup
window = tk.Tk()
window.title("FLASH CARDS")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

# Canvas
canvas = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = tk.PhotoImage(file=os.path.join("images", "card_front.png"))
card_back_img = tk.PhotoImage(file=os.path.join("images", "card_back.png"))
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
cross_image = tk.PhotoImage(file=os.path.join("images", "wrong.png"))
unknown_button = tk.Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

check_image = tk.PhotoImage(file=os.path.join("images", "right.png"))
known_button = tk.Button(image=check_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

next_card()

window.mainloop()
