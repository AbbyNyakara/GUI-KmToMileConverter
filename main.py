from tkinter import *

window = Tk()
window.title("Km to Miles Converter")
window.config(padx=20, pady=20)

def convert():
    km_input = km.get()
    miles = float(km_input) * 0.62
    miles_out.config(text=f"{miles}")

# Create the km text box
km = Entry()
km.config(width=7)
km.grid(column=0, row=0)

# Create the equal sign
equal_sign = Label(text="=")
equal_sign.grid(column=1, row=0)

# Create the miles input
miles_out = Label(text="0")
miles_out.config(width=7)
miles_out.grid(column=2, row=0)

# km and miles labels
km_label = Label(text="Km")
km_label.grid(column=0, row=1)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=1)

# Calculate button
calc = Button(text="Calculate", command=convert)
calc.grid(column=1, row=2)


window.mainloop()
