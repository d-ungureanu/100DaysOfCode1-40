import random
import tkinter
import pyperclip
from tkinter import messagebox


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letters_list = [random.choice(letters) for _ in range(random.randint(8, 10))]
    symbols_list = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    numbers_list = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = letters_list + symbols_list + numbers_list

    random.shuffle(password_list)

    password = "".join(password_list)

    pyperclip.copy(password)
    password_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_data = website_entry.get()
    email_data = email_entry.get()
    password_data = password_entry.get()
    if len(website_data) == 0 or len(email_data) == 0 or len(password_data) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        # messagebox.showinfo(title="Info", message="Message")
        is_ok_to_save = messagebox.askokcancel(title=website_data,
                                               message=f"These are the details entered:\nEmail: {email_data}\n"
                                                       f"Password:{password_data}\nIs it ok to save?")
        if is_ok_to_save:
            with open("saved_data.txt", "a") as saved_file:
                saved_file.write(f"{website_data}, {email_data}, {password_data}\n")
            website_entry.delete(0, tkinter.END)
            password_entry.delete(0, tkinter.END)
            website_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")

canvas = tkinter.Canvas(width=200, height=200, highlightthickness=0, bg="white")
background_image = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=background_image)
canvas.grid(row=0, column=1)

# Labels
website_lbl = tkinter.Label(text="Website:", bg="white")
website_lbl.grid(row=1, column=0)
email_lbl = tkinter.Label(text="Email/Username:", bg="white")
email_lbl.grid(row=2, column=0)
password_lbl = tkinter.Label(text="Password:", bg="white")
password_lbl.grid(row=3, column=0)

# Entries
website_entry = tkinter.Entry(width=52, borderwidth=1, relief="solid")
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = tkinter.Entry(width=52, borderwidth=1, relief="solid")
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "tiptil@gmail.com")
password_entry = tkinter.Entry(width=33, borderwidth=1, relief="solid")
password_entry.grid(row=3, column=1)

# Buttons
generate_btn = tkinter.Button(text="Generate Password", borderwidth=0.5, relief="groove", bg="white", width=15,
                              command=password_generator)
generate_btn.grid(row=3, column=2)
add_button = tkinter.Button(text="Add", borderwidth=0.5, relief="groove", bg="white", width=44, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
