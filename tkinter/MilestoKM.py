import tkinter as tk
from lib2to3.pytree import convert
from tkinter import ttk

def convert():
    try:
        miles = float(entry.get())
        kilometers = miles * 1.60934
        output_label.config(text=f'{kilometers:.2f} km')
    except ValueError:
        output_label.config(text ='Enter a correct value ')

# Create the main window
window = tk.Tk()
window.title("Demo")
window.geometry('300x150')

# Title label
title_label = ttk.Label(master=window, text='Miles to Kilometers', font='Calibri 24 bold')
title_label.pack()

# Input frame
input_frame = ttk.Frame(master=window)
input_frame.pack()  # Ensure the frame itself is packed

# Entry widget for miles input
entry = ttk.Entry(master=input_frame)
entry.pack(side='left',padx = 10)  # Use side='left' to align properly within the frame

# Button to trigger conversion (currently no functionality)
button = ttk.Button(master=input_frame, text="Convert", command=convert)
button.pack(side='left',pady =10)  # Align next to the entry widget


# output
output_label = ttk.Label(master=window, text="output", font='Calibri 20')
output_label.pack(pady = 5)

# Run the application
window.mainloop()
