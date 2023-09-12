from tkinter import *


#Creating a new window and configurations
window = Tk()
window.title("Widget Examples")
# window.minsize(width=500, height=500)

def calcluate_func():
    val_in_km_empty_label.config(text=f'{float(Miles_input.get())*1.609}')




# adding text input for Miles 0, 1
Miles_input= Entry(width=7)
Miles_input.grid(row=0, column=1)
Miles_input.insert(END, string="0")

# adding label  Miles 0,2
Mile_label= Label(text="Miles")
Mile_label.grid(row=0,column=2)

# adding label for equals to 1,0
equals_label= Label(text='is euqal to')
equals_label.grid(row=1,column=0)

# adding label for value in km 1,1
val_in_km_empty_label= Label(text="0")
val_in_km_empty_label.grid(row=1,column=1)

# adding label Km  1,2
empty_label= Label(text="KM")
empty_label.grid(row=1,column=2)


# adding button calculate  2, 1
button= Button(text='calc', command=calcluate_func)
button.grid(rows=2, column=1)



window.mainloop()