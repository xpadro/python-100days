from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

try:
    words = pandas.read_csv("data/to_learn.csv")
except FileNotFoundError:
    words = pandas.read_csv("data/english_words.csv")

dictionary = words.to_dict(orient="records")
chosen = {}


def get_random_word():
    global chosen, flip_timer
    window.after_cancel(flip_timer)
    chosen = random.choice(dictionary)
    canvas.itemconfig(card_title, text="English", fill="black")
    canvas.itemconfig(card_word, text=chosen["English"], fill="black")
    canvas.itemconfig(canvas_image, image=card_front_img)
    flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(canvas_image, image=card_back_img)
    canvas.itemconfig(card_title, text="Catalan", fill="white")
    canvas.itemconfig(card_word, text=chosen["Catalan"], fill="white")


def remove_word():
    dictionary.remove(chosen)
    to_learn = pandas.DataFrame(dictionary)
    to_learn.to_csv("data/to_learn.csv", index=False)
    get_random_word()

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)
flip_timer = window.after(3000, flip_card)

canvas = Canvas(height=540, width=800)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_front_img)

card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))

canvas.config(background=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=get_random_word)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=remove_word)
known_button.grid(row=1, column=1)

get_random_word()

window.mainloop()