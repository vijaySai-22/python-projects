import tkinter as tk
from tkinter import *

class App():
    
    def __init__(self,root):
        ##########--------------Company name-------------##########
        Label(root,text="Green Vegetables Market",font=('Arial',30,'bold','underline'),width=(84),bg="black",fg="white").place(x=0,y=0)
        Label(root,text="Customer Details",font=('Arial',30),width=(84),bg="grey",fg="black").place(x=0,y=60)
        Label(root,text="Enter Custmor Name",font=('Arial',18)).place(x=5,y=120)
        self.c_name=tk.StringVar()
        self.cname_entry=Entry(root,font=('Arial',18),width=(20),textvariable=self.c_name).place(x=245,y=120)
        Label(root,text="Enter contact number",font=('Arial',18)).place(x=525,y=120)
        self.c_phno=tk.StringVar()
        self.phno_entry=Entry(root,font=('Arial',18),width=(20),textvariable=self.c_phno).place(x=769,y=120)
        Label(root,text="Enter Address",font=('Arial',18)).place(x=1045,y=120)
        self.c_add=tk.StringVar()
        self.add_entry=Entry(root,font=('Arial',18),width=(46),textvariable=self.c_add).place(x=1210,y=120)
        # Label(root,text="Age",font=('Arial',18)).place(x=1695,y=120)
        # c_age=tk.StringVar()
        # self.age_entry=Entry(root,font=('Arial',18),width=(4)).place(x=1750,y=120)

        ##########---------------Particulars-------------###########

        Label(root,text="Particulars",font=('Arial',30),fg='black',bg='grey',width=(50)).place(x=5,y=180)
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
            self.each_price[i].place(x=950,y=self.y_value)
            self.y_value=self.y_value+60
        self.ext=Button(root,text="Exit",font=('Arial',23),bg="red",fg="black",command=self.close).place(x=50,y=900)
        self.clr=Button(root,text="Clear",font=('Arial',23),bg="yellow",fg="black",command=self.clear).place(x=600,y=900)
        self.cal=Button(root,text="Total=",font=('Arial',23),bg="green",fg="black",command=self.calculate).place(x=760,y=900)
        self.total_price=Label(root,text="0 RS",font=('Arial',27),width=9)
        self.total_price.place(x=900,y=900)
        ##########-----------line-------------##########
        Label(root,font=(30),fg='black',bg='grey',width=(3),height=(40)).place(x=1100,y=180)
        ##########-----------Bill-------------##########
        Label(root,text="Bill",font=('Arial',30),fg='black',bg='grey',width=(32)).place(x=1130,y=180)
        self.bill_text=Text(root)
        self.bill_text.insert("insert", "\n\nGreen Vegetables Market\n")
        self.bill_text.insert("end","One and only market where you can find Organic Vegetables\nSrikakulam, Andhrapradesh, 532484\nContact 9900887766\nGST no:X1234567890XYZ")
        self.bill_text.tag_add("head", "3.0", "3.23")
        self.bill_text.tag_add("rest", "4.0", "8.0")
        self.bill_text.tag_config("head", font=('Arial',30,'bold','underline'),justify='center')
        self.bill_text.tag_config("rest", font=('Arial',15),justify='center')
        self.bill_text.config(state='disabled',width=75,height=38)
        self.bill_text.place(x=1180,y=240)
        self.complete_and_save=Button(root,text="Complete and Save",font=('Arial',23),command=self.save_bill).place(x=1500,y=900)
    def calculate(self):
        if self.c_name.get()!='' and self.c_phno.get()!='' and self.c_add.get()!='':
            tot=0.0
            line=13.0
            self.bill_text.config(state='normal')
            self.bill_text.delete(str(line),"end")
            for i in range(len(self.veg)):
                each_tot=0.0
                if self.ck[i].get()==1 and self.qty[i].get()>0:
                    self.bill_text.insert("end", "\n\nCustomer Details"+"\n"+"\tCustmor Name: "+self.c_name.get()+
                                            "\n"+"\tContact number: "+self.c_phno.get()+"\n"+"\tAddress: "+self.c_add.get())
                    self.bill_text.tag_add("details_head", "9.0","9.16")
                    self.bill_text.tag_config("details_head", font=('Arial',20,'underline'),justify='center')
                    self.bill_text.tag_add("details_body", "10.0","12.50")
                    self.bill_text.tag_config("details_body", font=('Arial',15),justify='left')
                    self.bill_text.insert("end", "\n\n"+"\t"+"item"+"\t\t"+"qty"+"\t\t"+"dis"+"\t\t"+"Total\n")
                    each_tot=each_tot+self.veg_price[i]*self.qty[i].get()
                    each_tot=each_tot-((each_tot/100)*self.dis[i].get())
                    self.each_price[i].config(text=str(each_tot)+" Rs")
                    tot=tot+each_tot
                    self.total_price.config(text=str(tot)+" Rs")
                    self.bill_text.config(state='normal')
                    self.bill_text.insert("end","\n"+"\t"+self.veg[i]+"\t\t"+str(self.qty[i].get())+"\t\t"+str(self.dis[i].get())+"\t\t"+str(each_tot))
                    self.bill_text.tag_add("items",str(line),"end")
                    self.bill_text.tag_config("items",font=('Arial',15),justify='left')
                    self.bill_text.config(state='disabled')
                    line=line+1
                else:
                    self.each_price[i].config(text="0 Rs")
                    self.qty[i].set(0)
                    self.dis[i].set(0)
    def close(self):
        exit()
    def clear(self):
        for i in range(len(self.veg)):
            self.each_price[i].config(text="0 Rs")
            self.qty[i].set(0)
            self.dis[i].set(0)
        self.c_name.set('')
        self.c_phno.set('')
        self.c_add.set('')
        self.bill_text.config(state='normal')
        self.bill_text.delete("13.0","end")
        self.bill_text.config(state='disabled')
    def save_bill(self):
        import datetime 
        current_time = datetime.datetime.now() 
        self.file_name=str(self.c_name)+str(current_time)
        self.file=open(self.file_name+".txt","w")
        self.file.write(self.bill_text.get("1.0","end"))
        self.clear()
if __name__ == "__main__":
    win=tk.Tk()
    #title
    win.title("billing system")
    #setting tkinter window size
    width= win.winfo_screenwidth() 
    height= win.winfo_screenheight()
    win.geometry("%dx%d" % (width, height))
    #bg color
    win.config(bg="black")

    app=App(win)
    win.mainloop()
