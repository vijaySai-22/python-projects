import tkinter as tk
from tkinter import *

class App():
    
    def __init__(self,root):
        ##########--------------Company name-------------##########
        Label(root,text="Green Vegetables Market",font=('Arial',30),width=(84)).place(x=0,y=0)
        Label(root,text="Customer Details",font=('Arial',30),width=(84),bg="black",fg="white").place(x=0,y=60)
        Label(root,text="Enter Custmor Name",font=('Arial',18)).place(x=5,y=120)
        c_name=tk.StringVar()
        self.cname_entry=Entry(root,font=('Arial',18),width=(20)).place(x=245,y=120)
        Label(root,text="Enter contact number",font=('Arial',18)).place(x=525,y=120)
        c_phno=tk.StringVar()
        self.phno_entry=Entry(root,font=('Arial',18),width=(20)).place(x=769,y=120)
        Label(root,text="Enter Address",font=('Arial',18)).place(x=1045,y=120)
        c_add=tk.StringVar()
        self.add_entry=Entry(root,font=('Arial',18),width=(46)).place(x=1210,y=120)
        # Label(root,text="Age",font=('Arial',18)).place(x=1695,y=120)
        # c_age=tk.StringVar()
        # self.age_entry=Entry(root,font=('Arial',18),width=(4)).place(x=1750,y=120)

        ##########---------------Particulars-------------###########

        Label(root,text="Particulars",font=('Arial',30),fg='white',bg='black',width=(50)).place(x=5,y=180)
        self.veg=['Potato','Tomato','Carrot','Brinjal','Onions','Cabage','Ginger','Chilli','Garlic','Beetroot']
        self.veg_price=[20,22,30,25,30,30,70,32,60,53]
        self.ck=[None]*len(self.veg)
        self.qty=[None]*len(self.veg)
        self.dis=[None]*len(self.veg)
        self.each_price=[None]*len(self.veg)
        self.y_value=300
        Label(root,text="   ItemNo         Vegetables                           Qty          Discount          Total      ",font=('Arial',23)).place(x=10,y=240)
        for i in range(len(self.veg)):
            self.item_no='Item'+str(i+1)
            Label(root,text=self.item_no,font=('Arial',23)).place(x=50,y=self.y_value)

            self.ck[i]=tk.IntVar()
            name = Checkbutton(root, text = self.veg[i],variable = self.ck[i],
                    onvalue = 1,offvalue = 0,
                    font=('Arial',23),width = 18,anchor="w"
                    ).place(x=180,y=self.y_value)

            self.qty[i]=tk.DoubleVar()
            self.qty[i].set(0)
            Entry(root,font=('Arial',23),textvariable=self.qty[i],width=3).place(x=600,y=self.y_value)
            Label(root,text=".kg",font=('Arial',23)).place(x=660,y=self.y_value)

            self.dis[i]=tk.DoubleVar()
            self.dis[i].set(0)
            Entry(root,font=('Arial',23),textvariable=self.dis[i],width=3).place(x=760,y=self.y_value)
            Label(root,text="% ",font=('Arial',23)).place(x=820,y=self.y_value)

            self.each_price[i]=Label(root,text="0 Rs",font=('Arial',23))
            self.each_price[i].place(x=980,y=self.y_value)
            self.y_value=self.y_value+60
        self.cal=Button(root,text="Total=",font=('Arial',23),command=self.calculate).place(x=760,y=900)
        self.total_price=Label(root,text="0 RS",font=('Arial',27),width=9)
        self.total_price.place(x=900,y=900)
        ##########-----------line-------------##########
        Label(root,font=(30),bg='black',width=(3),height=(40)).place(x=1100,y=180)
        ##########-----------Bill-------------##########
        Label(root,text="Bill",font=('Arial',30),fg='white',bg='black',width=(32)).place(x=1130,y=180)
        complete_and_save=Button(root,text="Complete and Save",font=('Arial',23)).place(x=1500,y=900)
    def calculate(self):
        tot=0.0
        for i in range(len(self.veg)):
            each_tot=0.0
            if self.ck[i].get()==1 and self.qty[i].get()>0:
                each_tot=each_tot+self.veg_price[i]*self.qty[i].get()
                each_tot=each_tot-((each_tot/100)*self.dis[i].get())
                self.each_price[i].config(text=str(each_tot)+" Rs")
                tot=tot+each_tot
                self.total_price.config(text=str(tot)+" Rs")
            else:
                self.each_price[i].config(text="0 Rs")
                self.qty[i].set(0)
                self.dis[i].set(0)
if __name__ == "__main__":
    win=tk.Tk()
    #title
    win.title("billing system")
    #setting tkinter window size
    width= win.winfo_screenwidth() 
    height= win.winfo_screenheight()
    win.geometry("%dx%d" % (width, height))
    #bg color
    win.config(bg="green")

    app=App(win)
    win.mainloop()
