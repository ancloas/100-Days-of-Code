from tkinter import *
import pandas as pd
import os
from tkinter import messagebox
from password_generation_code import generate_random_password
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password=generate_random_password()
    pass_input.delete(0, END)
    pass_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    credentials={}
    credentials['Website'] = website_input.get()
    credentials['Email'] = email_input.get()
    credentials['Password'] = pass_input.get()

    if not(credentials['Website']) or not(credentials['Email']) or not(credentials['Password']):
        messagebox.showerror(title='error', message="You can't leave any field empty")
        return

    is_ok= messagebox.askokcancel(title='save password', message=f'These are the details: \nWebsite: {credentials["Website"]} \nEmail: {credentials["Email"]}\nPassword: {credentials["Password"]}\n Is it ok to save?')
    
    if not is_ok:
        return
    
    # Define the CSV file path
    csv_file_path = './Passwsord Generator/credentials.csv'
    
    # Create a DataFrame from the data
    data = [[credentials['Website'], credentials['Email'], credentials['Password']]]

    
    # check if file not present add headers
    if not os.path.isfile(csv_file_path):
        with open(csv_file_path, 'w') as file:
            file.write("Website\tEmail\tPassword\n")


    existing_df= pd.read_csv(csv_file_path, sep='\t')
    df = pd.DataFrame(data, columns=["Website", "Email", "Password"])

    df_updated = pd.concat([existing_df, df], ignore_index=True)


    # Append the DataFrame to the CSV file with tab separator
    df_updated.to_csv(csv_file_path, sep='\t', index=False)
    website_input.delete(0, END)
    pass_input.delete(0, END)
    email_input.delete(0, END)
    email_input.insert(0, df_updated['Email'].mode().to_list()[0])
    


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
website_input = Entry(width=52)
website_input.focus()
# website_input.insert(END, "enter website name")
website_input.grid(row=1, column=1, columnspan=2)

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
button_generate_password = Button(text="Generate Password", command=generate_password)
button_generate_password.grid(row=3, column=2)

# Button Add password
button_add = Button(text="Add", width=44, command=save_password)
button_add.grid(row=4, column=1, columnspan=2)




window.mainloop()
