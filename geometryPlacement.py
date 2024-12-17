from tkinter import*;

main = Tk();
main.geometry('600x600')
main.title("geometry intro")

mylabel = Label(main, text="label heading", bg='orange', fg='black', padx=10, pady=10)

#mylabel.pack(side='left', fill=Y, expand=True)
#
# mylabel.pack(anchor='e')
mylabel.place(x=0,y=0, relheight=1, relwidth=0.3)

main.mainloop()