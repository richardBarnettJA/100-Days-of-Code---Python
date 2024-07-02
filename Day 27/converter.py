from tkinter import * 


def miles_to_km():
    mls = int(miles.get())
    kilo = round(mls * 1.60934, 2)
    km.config(text=f"{kilo}")
    


screen = Tk()
# screen.minsize(width=500, height=300)
screen.title("Mile to KM Converter")
screen.config(padx=20, pady=20)


miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

equal_to = Label(text="is equal to")
equal_to.grid(column=0, row=1)

miles = Entry()
miles.insert(END, 0)
miles.grid(column=1, row=0)

km = Label(text="0")
km.grid(column=1, row=1)


button = Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=2)







screen.mainloop()