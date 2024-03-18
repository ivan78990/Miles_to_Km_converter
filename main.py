from tkinter import *


def convert():
    result = 1.609 * float(value_entry.get())
    km_value_label.config(text=f"{result}")


window = Tk()
window.title("Mile to Km Converter")
# window.geometry("190x100")

is_equal_label = Label(text="is equal_to")
is_equal_label.grid(column=0, row=1)

km_value_label = Label(text="0")
km_value_label.grid(column=1, row=1)

miles_text = Label(text="Miles")
miles_text.grid(column=2, row=0)

km_text = Label(text="Km")
km_text.grid(column=2, row=1)

value_entry = Entry(width=10)
value_entry.insert(END, string="0")
value_entry.grid(column=1, row=0)

button = Button(text="Calculate", command=convert)
button.grid(column=1, row=2)

window.mainloop()
