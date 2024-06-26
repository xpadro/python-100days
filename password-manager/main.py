from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_password():
    letters_list = [random.choice(letters) for _ in range(random.randint(8, 10))]
    symbols_list = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    numbers_list = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = letters_list + symbols_list + numbers_list

    random.shuffle(password_list)

    password = "".join(password_list)

    password_input.insert(0, password)

    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    email = email_input.get()
    web = website_input.get()
    password = password_input.get()

    new_data = {
        web: {
            "email": email,
            "password": password
        }
    }

    is_empty = len(web) == 0 or len(password) == 0
    if is_empty:
        messagebox.showerror(title="Oops", message="Some information is missing")
    else:
        try:
            with open("data.json", "r") as f:
                existing_data = json.load(f)
        except FileNotFoundError:
            with open("data.json", "w") as f:
                json.dump(new_data, f, indent=4)
        else:
            existing_data.update(new_data)

            with open("data.json", "w") as f:
                json.dump(existing_data, f, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)


def search():
    web = website_input.get()
    try:
        with open("data.json", "r") as f:
            existing_data = json.load(f)
    except FileNotFoundError:
        messagebox.showerror(title="Oops", message="No data found")
    else:
        if web in existing_data:
            email = existing_data[web]['email']
            password = existing_data[web]['password']
            messagebox.showinfo(title=f"{web}", message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showerror(title="Oops", message="Web not found")


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website")
website_label.grid(row=1, column=0)

email_label = Label(text="Email")
email_label.grid(row=2, column=0)

password_label = Label(text="Password")
password_label.grid(row=3, column=0)

website_input = Entry(width=21)
website_input.grid(row=1, column=1)
website_input.focus()

email_input = Entry(width=35)
email_input.grid(row=2, column=1, columnspan=2)
email_input.insert(0, "xavi@gmail.com")

password_input = Entry(width=21)
password_input.grid(row=3, column=1)

generate_button = Button(text="Generate", command=generate_password)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

search_button = Button(text="Search", command=search)
search_button.grid(row=1, column=2)

window.mainloop()