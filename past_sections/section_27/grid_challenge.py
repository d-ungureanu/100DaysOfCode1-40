from tkinter import *

window = Tk()
window.title("Grid challenge")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label
my_label = Label(text="Label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

# New Button
new_button = Button(text="New Button")
new_button.grid(column=2, row=0)

# Button
button = Button(text="Button")
button.grid(column=1, row=1)

# Entry
entry = Entry(width=10)
entry.grid(column=3, row=2)

window.mainloop()
