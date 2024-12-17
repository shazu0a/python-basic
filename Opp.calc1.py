import tkinter as tk 
from tkinter import ttk

class calc(tk.Tk):
    def __init__(self, title, w, h):
        super().__init__()
        self.title(title)
        self.geometry(f'{w}x{h}')

        self.interface()
        self.mainloop()

    def interface(self):
        self.screen_var = tk.StringVar()
        screen = ttk.Entry(master=self, font='arial 14' , textvariable=self.screen_var)
        screen.pack(side='top', fill='x', pady=10)

        self.btnpanel = ttk.Frame(self)
        self.btnpanel.pack()

        btnNums = []
        x = 0
        for i in range(0, 3):       # i = 1
         for j in range(0, 3):   # j = 
            x = x+1
            self.btns(self.btnpanel, x, i,j)

        self.btns(self.btnpanel,'/' , 0,3)
        self.btns(self.btnpanel,'*' , 1,3)
        self.btns(self.btnpanel,'+' , 2,3)
        self.btns(self.btnpanel,'-' , 3,3)
        self.btns(self.btnpanel,'0' , 3,0)
        btnCancel = ttk.Button(self.btnpanel, text='c', command=self.btnCancelFunction)
        btnCancel.grid(row=3, column=1)
        btnEqual = ttk.Button(self.btnpanel, text='=', command=self.equalFunction)
        btnEqual.grid(row=3, column=2)

    def shownNum(self, x):
        calc = self.screen_var.get()
        calc = calc + str(x)
        self.screen_var.set(calc)
        # print(x)

    def btns(self, panel, t, r, c):
        btn = ttk.Button(panel, text=t, command=lambda val=t: self.shownNum(val))
        btn.grid(row=r, column=c)

    def btnCancelFunction(self):
       self.screen_var.set(0)

    def equalFunction(self):
       calc = self.screen_var.get()
       ans = eval(calc)
       self.screen_var.set(ans)
calc('my calculator', 250, 300)
        
        
