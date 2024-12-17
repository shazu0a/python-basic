from tkinter import *

root = Tk()

root.geometry('400x400')
root.minsize(200,100)
root.maxsize(600, 600)

loginheading = Label(root, text="login form", fg = 'red', bg ='black', font='forte 18 bold', padx=7, pady=15)

IbIUsername = Label(text="username ").grid(row=2, column=0)
Txtusername = Text(height=1, width=24).grid(row=2, column=2)
IbIUsername = Label(text="password").grid(row=3, column=0)
Txtusername = Text(height=1, width=24).grid(row=3, column=2)

btnlogin = Button(text="login").grid(row=5, column=1)

loginheading.grid(row=0, column=0, columnspan=3)

root.mainloop()