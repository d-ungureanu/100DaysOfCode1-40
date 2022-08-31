import tkinter
import random

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label

# # Set text at initialization
# my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
# my_label.pack(side="top")
#
# # Change text with []
# my_label_2 = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
# my_label_2.pack(side="top")
# my_label_2["text"] = "New Label text"

# Change text using .config()
my_label_3 = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
# my_label_3.config(text="New Text using .config()")
my_label_3.config(text="New Text")
my_label_3.grid(column=1,row=0)


# Button
def button_clicked():
    # my_label_3.config(text=f"{random.randint(1, 100000)} number generated on button click!")
    my_label_3.config(text=f"{box_input.get()} was taken from input box.")


button = tkinter.Button(text="Click Me!", command=button_clicked)
button.grid(column=1, row=2)

# Entry
box_input = tkinter.Entry(width=10)
box_input.get()
box_input.grid(column=1, row=1)

window.mainloop()
