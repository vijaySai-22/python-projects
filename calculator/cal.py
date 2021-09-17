import tkinter as tk
from tkinter import *

root=tk.Tk()
root.geometry('400x350')
root.resizable(0,0)
root.title('Calculator')


#GUI
field=Entry(root,width=20,font=('',20))
field.pack(pady=20)

eq=''
def addToEq(letter):
    global eq
    eq+=letter
    field.delete(0,'end')
    field.insert(0, eq)
def cal():
    try:
        global eq
        result=eval(eq)
        eq=str(result)
    except:
        eq='error'
    field.delete(0,'end')
    field.insert(0, eq)
def clear():
    global eq
    field.delete(0,'end')
    eq=''
def back():
    global eq
    if field.get()=='error':
        field.delete(0,'end')
        eq = ''
    else:
        fieldEq=field.get()
        fieldEq=fieldEq[:-1]
        field.delete(0,'end')
        field.insert(0, fieldEq)
        eq = fieldEq
btnframe=Frame(root)
btnframe.pack()

btn1=Button(btnframe,text='1',font=('Arial',20),width=5,command=lambda: addToEq('1')).grid(row=0,column=0)
btn2=Button(btnframe,text='2',font=('Arial',20),width=5,command=lambda: addToEq('2')).grid(row=0,column=1)
btn3=Button(btnframe,text='3',font=('Arial',20),width=5,command=lambda: addToEq('3')).grid(row=0,column=2)
btnbk=Button(btnframe,text='<',font=('Arial',20),width=5,command=lambda: back()).grid(row=0,column=3)
btn4=Button(btnframe,text='4',font=('Arial',20),width=5,command=lambda: addToEq('4')).grid(row=1,column=0)
btn5=Button(btnframe,text='5',font=('Arial',20),width=5,command=lambda: addToEq('5')).grid(row=1,column=1)
btn6=Button(btnframe,text='6',font=('Arial',20),width=5,command=lambda: addToEq('6')).grid(row=1,column=2)
btnc=Button(btnframe,text='C',font=('Arial',20),width=5,command=lambda: clear()).grid(row=1,column=3)
btn7=Button(btnframe,text='7',font=('Arial',20),width=5,command=lambda: addToEq('7')).grid(row=2,column=0)
btn9=Button(btnframe,text='8',font=('Arial',20),width=5,command=lambda: addToEq('8')).grid(row=2,column=1)
btn9=Button(btnframe,text='9',font=('Arial',20),width=5,command=lambda: addToEq('9')).grid(row=2,column=2)
btn0=Button(btnframe,text='0',font=('Arial',20),width=5,command=lambda: addToEq('0')).grid(row=2,column=3)
btna=Button(btnframe,text='+',font=('Arial',20),width=5,command=lambda: addToEq('+')).grid(row=3,column=0)
btns=Button(btnframe,text='-',font=('Arial',20),width=5,command=lambda: addToEq('-')).grid(row=3,column=1)
btnm=Button(btnframe,text='x',font=('Arial',20),width=5,command=lambda: addToEq('*')).grid(row=3,column=2)
btnd=Button(btnframe,text='/',font=('Arial',20),width=5,command=lambda: addToEq('/')).grid(row=3,column=3)
btnob=Button(btnframe,text='(',font=('Arial',20),width=5,command=lambda: addToEq('(')).grid(row=4,column=0)
btne=Button(btnframe,text='= Cal',font=('Arial',20),width=9,command=lambda: cal()).grid(row=4,column=1,columnspan=2)
btncb=Button(btnframe,text=')',font=('Arial',20),width=5,command=lambda: addToEq(')')).grid(row=4,column=3)

root.mainloop()
