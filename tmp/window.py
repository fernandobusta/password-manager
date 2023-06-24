#!/usr/bin/env python3

from tkinter import *

root = Tk()
root.title('User Data')
root.geometry("300x400")

# Check for Password
# Update a Password
# Input 



def save_data():
	pass

def show_selected():
	pass


# Create Text Boxes
program = Entry(root, width=30)
program.grid(row=0, column=1, padx=20, pady=(10, 0))
email = Entry(root, width=30)
email.grid(row=1, column=1)
pwd = Entry(root, width=30)
pwd.grid(row=2, column=1)
other = Entry(root, width=30)
other.grid(row=3, column=1)

# Create Text Box Labels
program_l = Label(root, text="Program")
program_l.grid(row=0, column=0, pady=(10, 0))
email_l = Label(root, text="Email")
email_l.grid(row=1, column=0)
pwd_l = Label(root, text="Password")
pwd_l.grid(row=2, column=0)
other_l = Label(root, text="Comments")
other_l.grid(row=3, column=0)


# Create the Save Button
save_btn = Button(root, text="Save", command=save_data)
save_btn.grid(row=5, column=1, columnspan=2, ipadx=100)

#Create Show Selected Button
show_btn = Button(root, text="Show", command=show_selected)
show_btn.grid(row=6, column=1, pady=10, padx=10, ipadx=100)



# Ends loop by clicking on the cross
root.mainloop()