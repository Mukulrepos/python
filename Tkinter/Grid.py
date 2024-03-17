from tkinter import *
import sys

# Correcting the import statement to include the correct path
sys.path.append(r'D:\programming\python\function')

# Importing the necessary function/class from the tkinter_hello.py file


root = Tk()
name = Label(root, text="Name")
password = Label(root, text="Password")
check = Checkbutton(root, text="Check")

input1 = Entry(root)  # Renaming input variable to input1 to avoid conflict with built-in function input()
input2 = Entry(root)

name.grid(row=0, sticky=E)
input1.grid(row=0, column=1)

password.grid(row=1)
input2.grid(row=1, column=1)

check.grid(columnspan=2)

root.mainloop()
