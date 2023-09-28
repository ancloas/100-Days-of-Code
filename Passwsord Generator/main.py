from tkinter import *
import pandas as pd
import os
from tkinter import messagebox
from password_generation_code import generate_random_password
import pyperclip
import json

#------------------------------Search-------------------------------------------#
def search():
    query_website=website_input.get()
    if not(query_website):
        messagebox.showerror(title='error', message="Please enter website to be searched")
        return

    creds_fils_path = './Passwsord Generator/credentials.json'
    
    try:
        with open(creds_fils_path, 'r') as data_file:
            credentials=json.load(data_file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        credentials={}
    
    try:
        messagebox.showinfo(title=query_website, message=f"Email: {credentials[query_website]['Email']}\nPassword: {credentials[query_website]['Password']}")
    except KeyError:
        messagebox.showinfo(title='Not Found', message=f"Credentials not found for {query_website}") 





# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password=generate_random_password()
    pass_input.delete(0, END)
    pass_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    new_website=website_input.get()
    new_email=email_input.get()
    new_password=pass_input.get()
    
    # return if fields are empty
    if not(new_website) or not(new_email) or not(new_password):
        messagebox.showerror(title='error', message="You can't leave any field empty")
        return

    # Define the json file path
    creds_fils_path = './Passwsord Generator/credentials.json'

    # check if file not present add headers
    try:
        with open(creds_fils_path, 'r') as data_file:
            credentials=json.load(data_file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        credentials={}
    else:
        #add new data
        credentials[new_website] = {
            "Email": new_email, "Password": new_password
        }
    
        # check if file not present add headers
        with open(creds_fils_path, 'w') as data_file:
            json.dump(credentials, data_file, indent=4)
    finally:        
        website_input.delete(0, END)
        pass_input.delete(0, END)
        email_input.delete(0, END)
        email_input.insert(0, 'anugrahgupta.52@gmail.com')
    


# ---------------------------- UI SETUP ------------------------------- #

#Creating a new window and configurations
window = Tk()
window.title("Passwrod Manager")
window.config(padx=50, pady=50)
# window.minsize()

#creating canvas for logo
canvas = Canvas(width=200, height=200)
# canvas.create_line(10, 10, 200, 50, fill='red', width=3)
#creating image for lock
logo = PhotoImage(file='./Passwsord Generator\logo.png')
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0,column=1)


# Creating widgets
#website_label
website_label = Label(text="Website:")
website_label.grid(row=1,column=0)

#email label
email_label = Label(text="Email:")
email_label.grid(row=2,column=0)

# Password Label
pass_label = Label(text="Password:")
pass_label.grid(row=3, column=0)

# Website inpput

#Text
website_input = Entry(width=40)
website_input.focus()
# website_input.insert(END, "enter website name")
website_input.grid(row=1, column=1,columnspan=2,sticky=W)

# Input Email
email_input = Entry(width=52)
# email_input.insert(END, "enter email")
email_input.grid(row=2, column=1, columnspan=2)
email_input.insert(0, 'anugrahgupta.52@gmail.com')

# Input Passord
pass_input = Entry(width=33)
# pass_input.insert(END, "enter password")
pass_input.grid(row=3, column=1)
# Button: Generate Password
button_search = Button(text="Search", command=search, width=9)
button_search.grid(row=1, column=2,  sticky=E)

# Button: Generate Password
button_generate_password = Button(text="Generate Password", command=generate_password)
button_generate_password.grid(row=3, column=2)

# Button Add password
button_add = Button(text="Add", width=44, command=save_password)
button_add.grid(row=4, column=1, columnspan=2)




window.mainloop()
