import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip
# Creating GUI
root = tk.Tk()
root.title("Password Generator using GUI")
lable = tk.Label(root,text="Password Length:")
lable.pack()
entry = tk.Entry(root)
entry.pack()  

# creating function
def password_generator(Password_len):
    password = ''
    for digit in range(Password_len):
        char_type = random.choice(["lower","digit","upper","special"])
        if char_type == "lower":
            password += random.choice(string.ascii_lowercase)
        elif char_type == "upper":
            password += random.choice(string.ascii_uppercase)
        elif char_type == "digit":
            password += random.choice(string.digits)
        else:
            password += random.choice(string.punctuation)
    return password

button = tk.Button(root,text="Generate Password",command=lambda:print(password_generator(int(entry.get()))))
button.pack()
# copy the generated password

def copy_generated_password(password):
    pyperclip.copy(password)
    messagebox.showinfo("Password Copied")
button_copy = tk.Button(root,text="Copy to the clipboard",command=lambda:copy_generated_password(password_generator(int(entry.get()))))
button_copy.pack()

root.mainloop()

