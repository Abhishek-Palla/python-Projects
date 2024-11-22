import tkinter as tk
from tkinter import messagebox
import  random

from numpy.ma.core import append

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
                   'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                   's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A',
                   'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
                   'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                   'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '"', '#', '$', '%', '&', "'", '(', ')',
           '*', '+', ',', '-', '.', '/', ':', ';', '<',
           '=', '>', '?', '@', '^', '_',
           '`', '{', '|', '}', '~']

def generetor():
    nr_letters = random.randint(8,10)
    nr_symbols = random.randint(2,4)
    nr_numbers = random.randint(2,4)

    password_list =[]
    for char in range(nr_letters):
        password_list.append(random.choice(letters))
    for char in range(nr_symbols):
        password_list.append(random.choice(symbols))
    for char in range(nr_numbers):
        password_list.append(random.choice(numbers))

    random.shuffle(password_list)
    password =''.join(password_list)
    print(password)
    password_entry.insert(0,password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def get_all_inputs():
    website_info =website_entry.get()
    email_info   = email_entry.get()
    password_info = password_entry.get()


    if len(password_info) == 0 or len(website_info) ==0 or len(email_info)  == 0:
        messagebox.showinfo(title="Error" ,message ="Don't leave any field empty")
        return
    is_ok =messagebox.askokcancel(title ='Yes/No'
                   ,message=f'{website_info} |{email_info} |{password_info}')

    # create a message box to check the info
    if is_ok:
        print(f'{website_info}|{email_info}|{password_info}')
        with open('password_manager.txt' ,'a') as file:
            file.write(f'{website_info} | {email_info} | {password_info}\n')
            file.write("")
            website_entry.delete(0, tk.END)
            password_entry.delete(0,tk.END)

# ---------------------------- UI SETUP ------------------------------- #


window = tk.Tk()
window.title("Password Manager")
# window.geometry('600x600')
window.config(padx=20, pady=20)

# Creating a canvas
canvas = tk.Canvas(width=200, height=200, highlightthickness=0)
lock_img = tk.PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1, pady=(20, 10))  # Add vertical padding

# Website label and input
website_label = tk.Label(master=window, text='Website')
website_label.grid(row=1, column=0, padx=(10, 5), pady=5, sticky="e")  # Add padding for alignment
email_label = tk.Label(master=window, text='Email/Username')
email_label.grid(row=2, column=0, padx=(10, 5), pady=5, sticky="e")
password_label = tk.Label(master=window, text='Password')
password_label.grid(row=3, column=0, padx=(10, 5), pady=5, sticky="e")


website_entry = tk.Entry(master=window, width=35)
website_entry.grid(row=1, column=1, padx=(5, 10), pady=5, sticky="w" , columnspan =2)  # Align inputs to the left
website_entry.focus()
# Email/Username label and input
email_entry= tk.Entry(master=window, width=35)
email_entry.grid(row=2, column=1,
                 padx=(5, 10), pady=5,
                 sticky="w" , columnspan =2)
email_entry.insert(0,"pallaabhi45@gmail.com")
# Password label and input
password_entry = tk.Entry(master=window, width=21)
password_entry.grid(row=3, column=1, padx=(5, 5), pady=5, sticky="w")

# Buttons
generate_password_button = tk.Button(text='Generate Password' , command = generetor)
generate_password_button.grid(row=3, column=2 )  # Align close to input field
add_button = tk.Button(text='Add', width=36 , command =get_all_inputs)
add_button.grid(row=4, column=1, columnspan=2 )  # Center "Add" button

window.mainloop()

