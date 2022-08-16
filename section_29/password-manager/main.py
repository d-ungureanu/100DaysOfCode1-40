import tkinter

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

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
email_entry = tkinter.Entry(width=52, borderwidth=1, relief="solid")
email_entry.grid(row=2, column=1, columnspan=2)
password_entry = tkinter.Entry(width=33, borderwidth=1, relief="solid")
password_entry.grid(row=3, column=1)

# Buttons
generate_btn = tkinter.Button(text="Generate Password", borderwidth=0.5, relief="groove", bg="white", width=15)
generate_btn.grid(row=3, column=2)
add_button = tkinter.Button(text="Add", borderwidth=0.5, relief="groove", bg="white", width=44)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
