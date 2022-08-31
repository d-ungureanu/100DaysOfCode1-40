from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=400, height=250)
window.config(padx=20, pady=20)
# Miles entry
miles_entry = Entry(width=7)
# miles_entry.get()
miles_entry.grid(row=0, column=1)

# miles label
miles_label = Label(text="Miles", font=("Arial", 24, "bold"))
miles_label.grid(row=0, column=2)

# explanatory label
text_label = Label(text="is equal to", font=("Arial", 24, "bold"))
text_label.grid(row=1, column=0)

# Km value label
km_label = Label(text="0", font=("Arial", 24, "bold"))
km_label.grid(row=1, column=1)

# explanatory label
text_label = Label(text="Km", font=("Arial", 24, "bold"))
text_label.grid(row=1, column=2)


# Button
def clicked_button():
    km_label.config(text=f"{round(float(miles_entry.get()) * 1.609, 2)}")


convert_btn = Button(text="Calculate", command=clicked_button)
convert_btn.grid(row=2, column=1)

window.mainloop()
