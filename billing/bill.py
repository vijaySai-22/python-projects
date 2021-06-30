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
        self.add_entry=Entry(root,font=('Arial',18),width=(36)).place(x=1210,y=120)
        Label(root,text="Age",font=('Arial',18)).place(x=1695,y=120)
        c_age=tk.StringVar()
        self.age_entry=Entry(root,font=('Arial',18),width=(4)).place(x=1750,y=120)

        ##########---------------Particulars-------------###########

        Label(root,text="Particulars",font=('Arial',30),fg='white',bg='black',width=(50)).place(x=5,y=180)
        self.veg=['Potato','Tomato','Carrot','Brinjal','Onions','Cabage','Ginger','Chilli','Garlic','Beetroot']
        #self.veg_price=[20,22,30,25,30,30,70,32,60,53]
        self.ck=[None]*len(self.veg)
        self.qty=[None]*len(self.veg)
        self.dis=[None]*len(self.veg)
        self.y_value=300
        Label(root,text="ItemNo     Vegetables              Qty         Discount        GST     Total                 ",font=('Arial',23)).place(x=10,y=240)
        for i in range(len(self.veg)):
            self.item_no='Item'+str(i)
            Label(root,text=self.item_no,font=('Arial',23)).place(x=10,y=self.y_value)

            self.ck[i]=tk.StringVar()
            name = Checkbutton(root, text = self.veg[i],variable = self.ck[i],
                    onvalue = 1,offvalue = 0,
                    font=('Arial',23),width = 13,anchor="w"
                    ).place(x=130,y=self.y_value)

            self.qty[i]=tk.StringVar()
            Entry(root,font=('Arial',23),textvariable=self.qty[i],width=2).place(x=430,y=self.y_value)
            Label(root,text=".kg",font=('Arial',23)).place(x=480,y=self.y_value)

            self.dis[i]=tk.StringVar()
            Entry(root,font=('Arial',23),textvariable=self.dis[i],width=2).place(x=580,y=self.y_value)
            Label(root,text="% ",font=('Arial',23)).place(x=630,y=self.y_value)

            Label(root,text="18% ",font=('Arial',23)).place(x=750,y=self.y_value)
            Label(root,text="0 Rs",font=('Arial',23)).place(x=880,y=self.y_value)
            self.y_value=self.y_value+60
        self.cal=Button(root,text="Caculate",font=('Arial',23),command=self.calculate).place(x=850,y=900)
        ##########-----------line-------------##########
        Label(root,font=(30),bg='black',width=(3),height=(40)).place(x=1100,y=180)
        ##########-----------Bill-------------##########
        bill_heading=Label(root,text="Bill",font=('Arial',30),fg='white',bg='black',width=(32)).place(x=1130,y=180)
        complete_and_save=Button(root,text="Complete and Save",font=('Arial',23)).place(x=1500,y=900)
    def calculate(self):
        pass
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
