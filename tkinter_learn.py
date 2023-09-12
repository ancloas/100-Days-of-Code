import tkinter
window= tkinter.Tk()



def button_clicked():
    my_label['text']=input.get()

window.title('My first GUI Program')
window.minsize(width=500, height=300)
window.config(padx=100, pady=50)

#Label 
my_label = tkinter.Label(text="I am a Label", font= ("Arial", 24, "italic"))
# my_label.pack(side="top")
# my_label.place(x=100, y=100)
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)
# my_label['text']="This is new label"


button= tkinter.Button(text='Green button', command=button_clicked)
button.grid(column=1, row=1)

# button.pack(side="bottom")

# new button

button= tkinter.Button(text='yellow button', command=button_clicked)
button.grid(column=2, row=0)


# Entry component

input= tkinter.Entry()
input.grid(column=3, row=2)

# input.pack()


window.mainloop()
