from tkinter import *

window = Tk()
window.title("Mile to km converter")
window.minsize(width=400, height=200)

# Entry for miles
miles_entry = Entry()
miles_entry.grid(column=1, row=0)

# Label for miles
miles_label = Label(text="Miles")
miles_label.grid(column=2,  row=0)

# Label for km
label = Label(text="is equal to")
label.grid(column=0, row=1)
km_value = Label(text="0")
km_value.grid(column=1, row=1)
km_text = Label(text="km")
km_text.grid(column=2, row=1)

# Button


def mile_to_km():
    mile = float(miles_entry.get())
    km = float(mile * 1.6)

    km_value.config(text=km)


calculate_button = Button(text="calculate", command=mile_to_km)
calculate_button.grid(column=1, row=2)

window.mainloop()
