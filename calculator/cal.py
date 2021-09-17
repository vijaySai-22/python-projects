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

btn1=Button(btnframe,text='1',font=('Arial',20),width=5,command=lambda: addToEq('1'))
btn2=Button(btnframe,text='2',font=('Arial',20),width=5,command=lambda: addToEq('2'))
btn3=Button(btnframe,text='3',font=('Arial',20),width=5,command=lambda: addToEq('3'))
btnbk=Button(btnframe,text='<',font=('Arial',20),width=5,command=lambda: back())
btn4=Button(btnframe,text='4',font=('Arial',20),width=5,command=lambda: addToEq('4'))
btn5=Button(btnframe,text='5',font=('Arial',20),width=5,command=lambda: addToEq('5'))
btn6=Button(btnframe,text='6',font=('Arial',20),width=5,command=lambda: addToEq('6'))
btnc=Button(btnframe,text='C',font=('Arial',20),width=5,command=lambda: clear())
btn7=Button(btnframe,text='7',font=('Arial',20),width=5,command=lambda: addToEq('7'))
btn8=Button(btnframe,text='8',font=('Arial',20),width=5,command=lambda: addToEq('8'))
btn9=Button(btnframe,text='9',font=('Arial',20),width=5,command=lambda: addToEq('9'))
btn0=Button(btnframe,text='0',font=('Arial',20),width=5,command=lambda: addToEq('0'))
btna=Button(btnframe,text='+',font=('Arial',20),width=5,command=lambda: addToEq('+'))
btns=Button(btnframe,text='-',font=('Arial',20),width=5,command=lambda: addToEq('-'))
btnm=Button(btnframe,text='x',font=('Arial',20),width=5,command=lambda: addToEq('*'))
btnd=Button(btnframe,text='/',font=('Arial',20),width=5,command=lambda: addToEq('/'))
btnob=Button(btnframe,text='(',font=('Arial',20),width=5,command=lambda: addToEq('('))
btne=Button(btnframe,text='= Cal',font=('Arial',20),width=9,command=lambda: cal())
btncb=Button(btnframe,text=')',font=('Arial',20),width=5,command=lambda: addToEq(')'))

btn1.grid(row=0,column=0)
btn2.grid(row=0,column=1)
btn3.grid(row=0,column=2)
btnbk.grid(row=0,column=3)
btn4.grid(row=1,column=0)
btn5.grid(row=1,column=1)
btn6.grid(row=1,column=2)
btnc.grid(row=1,column=3)
btn7.grid(row=2,column=0)
btn8.grid(row=2,column=1)
btn9.grid(row=2,column=2)
btn0.grid(row=2,column=3)
btna.grid(row=3,column=0)
btns.grid(row=3,column=1)
btnm.grid(row=3,column=2)
btnd.grid(row=3,column=3)
btnob.grid(row=4,column=0)
btne.grid(row=4,column=1,columnspan=2)
btncb.grid(row=4,column=3)

btnbk['bg']='yellow'
btnc['bg']='red'
btne['bg']='lightgreen'

root.mainloop()
