import tkinter as tk
from tkinter import *
from tkinter import messagebox
root=tk.Tk()
root.geometry('450x700')
root.resizable(0,0)
root.config(bg='black')
root.title("Todo App")

head=Label(root,text="ToDo App",fg='white',bg='black',font=('',40)).pack(pady=20)

#frame for text field and add button
frame1=Frame(root,bg='black')
frame1.pack(fill=BOTH,padx=20)
#frame for listbox and scrollbar
lbframe = Frame(root,bg='black')
lbframe.pack()
#listbox
lb = Listbox(lbframe, width=40, height=15,bg='black',fg='white', font=("", 15))
lb.pack(side="left")
#scrollbar
sb = Scrollbar(lbframe, orient="vertical")
sb.config(command=lb.yview)
sb.pack(side="right", fill="y")
lb.config(yscrollcommand=sb.set)
#rename frame
rFrame=Frame(root,bg='black')
rFrame.pack(fill=BOTH,padx=20,pady=10)
#clear, add, remove and renamefuncs for add item and remove item
def clear():
    entry.delete(0,'end')
def add():
    data=entry.get()
    if data == '':
        messagebox.showerror('Warning','nothing is entered')
    else:
        lb.insert(END,data)
        entry.delete(0,'end')
def remove():
    lb.delete(ANCHOR)
def rename():
    data=rEntry.get()
    if data != '':
        lb.delete(ANCHOR)
        lb.insert(ANCHOR,data)
        rEntry.delete(0,'end')
#entry for text
entry=Entry(frame1,width=20,font=('',13),bg='black',fg='white',insertbackground='white'))
entry.pack(side=LEFT,fill=BOTH,pady=20)
#button to clear
button=Button(frame1,text='Clear',bg='yellow',fg='black',command=clear)
button.pack(side=LEFT,fill=BOTH,pady=20,padx=3)
#button to add
button=Button(frame1,text='Add',bg='green',fg='white',command=add)
button.pack(side=RIGHT,fill=BOTH,pady=20)
#button to remove
rmv=Button(root,text='remove',bg='red',fg='white',command=remove).pack(pady=20)
#rename
rEntry=Entry(rFrame,width=20,font=('',13),bg='black',fg='white',insertbackground='white'))
rEntry.pack(side=LEFT,fill=BOTH,padx=20)
rBtn=Button(rFrame,text='Rename',bg='blue',fg='white',command=rename)
rBtn.pack(side=RIGHT,fill=BOTH,padx=20)
root.mainloop()
