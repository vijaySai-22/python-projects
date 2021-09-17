import tkinter as tk
from tkinter import *
import tkinter.font as font

root=tk.Tk()
root.geometry('500x500')
root.resizable(0,0)
root.title('Tic Tac Toe')


f=Frame(root)
f.pack()

Label(f,text='Tic Tac Toe',font=('',40)).grid(row=0,column=0)

f2=Frame(root)
f2.pack()
b1=Button(f2,font=('Arial',50),width=2,bg='black',command=lambda: clicked(1))
b2=Button(f2,font=('Arial',50),width=2,bg='black',command=lambda: clicked(2))
b3=Button(f2,font=('Arial',50),width=2,bg='black',command=lambda: clicked(3))
b4=Button(f2,font=('Arial',50),width=2,bg='black',command=lambda: clicked(4))
b5=Button(f2,font=('Arial',50),width=2,bg='black',command=lambda: clicked(5))
b6=Button(f2,font=('Arial',50),width=2,bg='black',command=lambda: clicked(6))
b7=Button(f2,font=('Arial',50),width=2,bg='black',command=lambda: clicked(7))
b8=Button(f2,font=('Arial',50),width=2,bg='black',command=lambda: clicked(8))
b9=Button(f2,font=('Arial',50),width=2,bg='black',command=lambda: clicked(9))
b1.grid(row=0,column=0)
b2.grid(row=0,column=1)
b3.grid(row=0,column=2)
b4.grid(row=1,column=0)
b5.grid(row=1,column=1)
b6.grid(row=1,column=2)
b7.grid(row=2,column=0)
b8.grid(row=2,column=1)
b9.grid(row=2,column=2)

r=Label(root,text='Player X Turn',font=('',20))
r.pack()

rb=Button(root,text='Reset',bg='red',fg='white',command=lambda: reset())
rb.pack()

x=0
b=[b1,b2,b3,b4,b5,b6,b7,b8,b9]
clkd=[]
def clicked(num):
    if num not in clkd:
        global x
        clkd.insert(x,num)
        if x%2==0:
            player='X'
            next='O'
            bg='green'
        else:
            player='O'
            next='X'
            bg='red'
        b[num-1].configure(text=player,bg=bg)
        x+=1
        r.config(text='Player '+next+' Turn')
        chk()
v=[None,None,None,None,None,None,None,None,None]
def chk():
    for i in range(9):
        v[i]=b[i]['text']
    if v[0]==v[1]==v[2]=='X' or v[3]==v[4]==v[5]=='X' or v[6]==v[7]==v[8]=='X' or v[0]==v[3]==v[6]=='X' or v[1]==v[4]==v[7]=='X' or v[2]==v[5]==v[8]=='X' or v[0]==v[4]==v[8]=='X' or v[2]==v[4]==v[6]=='X':
        r.config(text='Player X Won')
        stop()
    elif v[0]==v[1]==v[2]=='O' or v[3]==v[4]==v[5]=='O' or v[6]==v[7]==v[8]=='O' or v[0]==v[3]==v[6]=='O' or v[1]==v[4]==v[7]=='O' or v[2]==v[5]==v[8]=='O' or v[0]==v[4]==v[8]=='O' or v[2]==v[4]==v[6]=='O':
        r.config(text='Player O Won')
        stop()
    elif '' not in v:
        r.config(text='Draw')
        stop()
def stop():
    for i in range(9):
        b[i]['state']='disabled'
    rb['bg']='green'
    rb['text']='Restart'
    
def reset():
    global x
    x=0
    global b
    for i in range(9):
        b[i]['text']=''
        b[i]['bg']='black'
        b[i]['state']='normal'
    b=[b1,b2,b3,b4,b5,b6,b7,b8,b9]
    rb['bg']='red'
    rb['text']='Reset'
    global clkd
    clkd.clear()
    v=[None,None,None,None,None,None,None,None,None]
    r['text']='Player X Turn'
root.mainloop()
