import tkinter as tk
from tkinter import *
from tkinter import messagebox
import random
#import pyperclip as pc
class App:
    def __init__(self,root):
        Label(root,text="Random Password Generator").pack(fill=X)

        f1=LabelFrame(root)
        f1.place(x=0,y=25,relwidth=1)
        Label(f1,text="Enter number of characters: ").grid(row=1,column=0,padx=10,pady=10)
        self.n=tk.StringVar()
        self.n_Entry=Entry(f1,textvariable=self.n,width=4).grid(row=1,column=1,padx=10,pady=10)
        Button(f1,text="Generate",command=self.gen).grid(row=1,column=2,padx=10,pady=10)
        self.f2=LabelFrame(root)
        self.f2.place(x=0,y=75,relwidth=1)
        self.pswrd=Text(self.f2)
        self.cpyBtn=Button(self.f2,text="Copy",command=self.cpy)
        self.colour = StringVar()
        self.colour.set('black')
        self.rateLbl=Label(self.f2,fg=self.colour.get())
    def gen(self):
        if self.n.get().isnumeric() and int(self.n.get())>=4 and int(self.n.get())<=12:
            self.cpyBtn.grid_forget()
            self.rateLbl.grid_forget()
            self.pswrd.grid_forget()
            self.f2.place(x=0,y=75,relwidth=1)
            self.ucAlpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            self.lcAlpha="abcdefghijklmnopqrstuvwxyz"
            self.digits = "0123456789"
            self.special = "!@#$%^&*()[]}{"
            self.raw=[self.ucAlpha,self.lcAlpha,self.digits,self.special]
            self.pw=''
            
            self.pw=self.pw+random.choice(self.ucAlpha)+random.choice(self.lcAlpha)+random.choice(self.digits)+random.choice(self.special)
            self.pw=''.join(random.sample(self.pw,len(self.pw)))#shuffle the word
            
            for i in range(int(self.n.get())-4):
                self.pw=self.pw+random.choice(random.choice(self.raw))
            #text field of password
            self.pswrd.config(state='normal')
            self.pswrd.delete('0.0','end')
            self.pswrd.insert('insert',self.pw)
            self.pswrd.config(width=12,height=1,state='disabled')
            self.pswrd.grid(row=3,column=0,padx=10,pady=10)
            #cpy btn
            self.cpyBtn.grid(row=3,column=1,padx=10,pady=10)

            #rating
            self.x=u'\u26AB'
            self.y=u'\u26AA'
            self.rate=''
            if int(self.n.get())>=4 and int(self.n.get())<6:
                self.rate=self.rate+self.x+self.y*4+'Very Weak'
                self.colour.set('red')
            elif int(self.n.get())>=6 and int(self.n.get())<8:
                self.rate=self.rate+self.x*2+self.y*3+'Weak'
                self.colour.set('tomato')
            elif int(self.n.get())>=8 and int(self.n.get())<10:
                self.rate=self.rate+self.x*3+self.y*2+'Average'
                self.colour.set('orange')
            elif int(self.n.get())>=10 and int(self.n.get())<12:
                self.rate=self.rate+self.x*4+self.y+'Strong'
                self.colour.set('lawn green')
            else:
                self.rate=self.rate+self.x*5+'Very Strong'
                self.colour.set('green2')
            self.rateLbl.config(text=self.rate,fg=self.colour.get(),bg='black')
            self.rateLbl.grid(row=3,column=2,padx=10,pady=10)
        elif self.n.get()=='':
            self.f2.place_forget()
        else:
            self.f2.place_forget()
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
    win.geometry("400x125+750+400")
    #bg color
    win.config(bg="black")
    win.resizable(0,0)
    app=App(win)
    win.mainloop()
