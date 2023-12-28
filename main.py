from tkinter import *


def calculate_action():
    miles_num = float(input_miles.get())
    result = round(miles_num * 1.609, 2)
    label_result.config(text=result)


window = Tk()
window.title("Miles to Km Converter")
# window.minsize(width=150, height=100)
window.config(padx=30, pady=30)

# Create the labels with padding
label_miles = Label(text="Miles", font=("Arial", 15, "bold"), padx=10, pady=10)
label_equal = Label(text="is equal to", font=("Arial", 15, "bold"), padx=10, pady=10)
label_km = Label(text="Km", font=("Arial", 15, "bold"), padx=10, pady=10)
label_result = Label(text="0", font=("Arial", 15, "bold"), padx=10, pady=10)
# Position the labels on the screen
label_miles.grid(column=2, row=0)
label_equal.grid(column=0, row=1)
label_result.grid(column=1, row=1)
label_km.grid(column=2, row=1)

# Create the entry widget
input_miles = Entry(width=9, font=("Arial", 15, "bold"))
input_miles.insert(END, string="0")
input_miles.focus()
input_miles.grid(column=1, row=0)


# Create the calculate button
calculate_button = Button(text="Calculate", width=8, font=("Arial", 15, "bold"), command=calculate_action)
calculate_button.grid(column=1, row=2)

window.mainloop()
