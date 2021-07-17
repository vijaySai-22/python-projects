import tkinter as tk
from tkinter import *
import random
class App:
    def __init__(self,root):
        Label(root,text="Password Generator").pack(fill=X)

        f1=LabelFrame(root)
        f1.place(x=0,y=50,relwidth=1)
        Label(f1,text="Enter number of characters: ").grid(row=0,column=0,padx=10,pady=10)
        self.n=tk.StringVar()
        self.n_Entry=Entry(f1,textvariable=self.n).grid(row=0,column=1,padx=10,pady=10)
        Button(f1,text="Generate",command=self.gen).grid(row=1,column=0,columnspan=2)
    def gen(self):
        pass
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
