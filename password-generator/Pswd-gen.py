import tkinter as tk
from tkinter import *
from tkinter import messagebox
import random
import pyperclip as pc
class App:
    def __init__(self,root):
        Label(root,text="Password Generator").pack(fill=X)
        f1=LabelFrame(root)
        f1.place(x=0,y=50,relwidth=1)
        Label(f1,text="Enter number of characters: ").grid(row=0,column=0,padx=10,pady=10)
        self.n=tk.StringVar()
        self.n_Entry=Entry(f1,textvariable=self.n).grid(row=0,column=1,columnspan=2,padx=10,pady=10)
        Button(f1,text="Generate",command=self.gen).grid(row=1,column=0,columnspan=3)
        self.pswrd=Text(f1)
        self.cpyBtn=Button(f1,text="Copy",command=self.cpy)
        self.rateLbl=Label(f1)
    def gen(self):
        if self.n.get().isnumeric() and int(self.n.get())>=4 and int(self.n.get())<=12:
            self.ucAlpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            self.lcAlpha="abcdefghijklmnopqrstuvwxyz"
            self.digits = "0123456789"
            self.special = "!@#$%^&*()[]}{"
            self.raw=[self.ucAlpha,self.lcAlpha,self.digits,self.special]
            self.pw=''
            self.pw=self.pw+random.choice(self.ucAlpha)+random.choice(self.lcAlpha)+random.choice(self.digits)+random.choice(self.special)
            for i in range(int(self.n.get())-4):
                self.pw=self.pw+random.choice(random.choice(self.raw))
                #text field of password
                self.pswrd.config(state='normal')
                self.pswrd.delete('0.0','end')
                self.pswrd.insert('insert',self.pw)
                self.pswrd.config(width=12,height=1,state='disabled')
                self.pswrd.grid(row=2,column=0)
                #cpy btn
                self.cpyBtn.grid(row=2,column=1)
                #rating
                self.x=u'\u26AB'
                self.y=u'\u26AA'
                self.rate=''
                if int(self.n.get())>=4 and int(self.n.get())<6:
                    self.rate=self.rate+self.x+self.y*4+'very weak'
                elif int(self.n.get())>=6 and int(self.n.get())<8:
                    self.rate=self.rate+self.x*2+self.y*3+'weak'
                elif int(self.n.get())>=8 and int(self.n.get())<10:
                    self.rate=self.rate+self.x*3+self.y*2+'average'
                elif int(self.n.get())>=10 and int(self.n.get())<12:
                    self.rate=self.rate+self.x*4+self.y+'strong'
                else:
                    self.rate=self.rate+self.x*5+'very strong'
                self.rateLbl.config(text=self.rate)
                self.rateLbl.grid(row=2,column=2)
        elif self.n.get()=='':
            self.cpyBtn.grid_forget()
            self.rateLbl.grid_forget()
            self.pswrd.grid_forget()
        else:
            self.pswrd.config(state='normal')
            self.pswrd.delete('0.0','end')
            self.pswrd.insert('insert','Enter valid input(eg: 4,5 upto 12)')
            self.pswrd.config(width=35,height=1,state='disabled')
            self.pswrd.grid(row=2,column=0,columnspan=2)
            self.cpyBtn.grid_forget()
            self.rateLbl.grid_forget()
            #msgbox
            messagebox.showwarning("Warning", "Enter valid input")
    def cpy(self):
        #for copy button
        cpyText = self.pw
        pc.copy(cpyText)
if __name__=='__main__':
    win=tk.Tk()
    #title
    win.title("Password Generator")
    #setting tkinter window size
    win.geometry("400x400")
    #bg color
    win.config(bg="black")
    win.resizable(0,0)
    app=App(win)
    win.mainloop()
