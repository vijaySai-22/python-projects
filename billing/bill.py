from tkinter import Label,Button,Entry,Checkbutton,Text
import tkinter as tk

class App():
    
    def __init__(self,root):
        ##########--------------Company name-------------##########
        Label(root,text="Green Vegetables Market",font=('Arial',20,'bold','underline'),width=(80),bg="black",fg="white").place(x=0,y=0)
        Label(root,text="Customer Details",font=('Arial',20),width=(80),bg="grey",fg="black").place(x=0,y=38)
        Label(root,text="Enter Custmor Name",font=('Arial',12)).place(x=5,y=80)
        self.c_name=tk.StringVar()
        self.cname_entry=Entry(root,font=('Arial',12),width=(20),textvariable=self.c_name).place(x=163,y=81)
        Label(root,text="Enter contact number",font=('Arial',12)).place(x=380,y=80)
        self.c_phno=tk.StringVar()
        self.phno_entry=Entry(root,font=('Arial',12),width=(20),textvariable=self.c_phno).place(x=540,y=81)
        Label(root,text="Enter Address",font=('Arial',12)).place(x=760,y=80)
        self.c_add=tk.StringVar()
        self.add_entry=Entry(root,font=('Arial',12),width=(35),textvariable=self.c_add).place(x=870,y=81)
       

        ##########---------------Particulars-------------###########

        Label(root,text="Particulars",font=('Arial',20),fg='black',bg='grey',width=(45)).place(x=5,y=120)
        self.veg=['Potato','Tomato','Carrot','Brinjal','Onions','Cabage','Ginger','Chilli','Garlic','Beetroot']
        self.veg_price=[20,22,30,25,30,30,70,32,60,53]
        self.ck=[None]*len(self.veg)
        self.qty=[None]*len(self.veg)
        self.dis=[None]*len(self.veg)
        self.each_price=[None]*len(self.veg)
        self.y_value=200
        Label(root,text="   ItemNo                      Vegetables                           Qty                Discount              Total      ",font=('Arial',11)).place(x=10,y=170)
        for i in range(len(self.veg)):
            self.item_no='Item'+str(i+1)
            Label(root,text=self.item_no,font=('Arial',12)).place(x=26,y=self.y_value+3)

            self.ck[i]=tk.IntVar()
            Checkbutton(root, text = self.veg[i],variable = self.ck[i],
                    onvalue = 1,offvalue = 0,
                    font=('Arial',12),width = 16,anchor="w"
                    ).place(x=120,y=self.y_value)

            self.qty[i]=tk.DoubleVar()
            self.qty[i].set(0)
            Entry(root,font=('Arial',12),textvariable=self.qty[i],width=3).place(x=320,y=self.y_value+1)
            Label(root,text=".kg",font=('Arial',12)).place(x=355,y=self.y_value)

            self.dis[i]=tk.DoubleVar()
            self.dis[i].set(0)
            Entry(root,font=('Arial',12),textvariable=self.dis[i],width=3).place(x=430,y=self.y_value+1)
            Label(root,text="% ",font=('Arial',12)).place(x=465,y=self.y_value)

            self.each_price[i]=Label(root,text="0 Rs",font=('Arial',12))
            self.each_price[i].place(x=530,y=self.y_value)
            self.y_value=self.y_value+32
        self.ext=Button(root,text="Exit",font=('Arial',11),bg="red",fg="black",command=self.close).place(x=26,y=550)
        self.clr=Button(root,text="Clear",font=('Arial',11),bg="yellow",fg="black",command=self.clear).place(x=360,y=550)
        self.cal=Button(root,text="Total=",font=('Arial',11),bg="green",fg="black",command=self.calculate).place(x=430,y=550)
        self.total_price=Label(root,text="0 RS",font=('Arial',12),width=6)
        self.total_price.place(x=510,y=555)
        ##########-----------line-------------##########
        Label(root,font=(30),fg='black',bg='grey',width=(3),height=(40)).place(x=630,y=120)
        ##########-----------Bill-------------##########
        Label(root,text="Bill",font=('Arial',20),fg='black',bg='grey',width=(35)).place(x=630,y=120)
        self.bill_text=Text(root)
        self.bill_text.insert("insert", "\n\nGreen Vegetables Market\n")
        self.bill_text.insert("end","One and only market where you can find Organic Vegetables\nSrikakulam, Andhrapradesh, 532484\nContact: 9900887766,  Mail: greenvegmkt@gmail.com\nGST no:X1234567890XYZ")
        self.bill_text.tag_add("head", "3.0", "3.23")
        self.bill_text.tag_add("rest", "4.0", "7.22")
        self.bill_text.tag_config("head", font=('Arial',15,'bold','underline'),justify='center')
        self.bill_text.tag_config("rest", font=('Arial',10),justify='center')
        self.bill_text.config(state='disabled',width=55,height=22)
        self.bill_text.place(x=700,y=160)
        self.complete_and_save=Button(root,text="Complete and Save",font=('Arial',11),command=self.save_bill).place(x=880,y=550)
    def calculate(self):
        if self.c_name.get()!='' and self.c_phno.get()!='' and self.c_add.get()!='':
            self.tot=0.0
            line=13.0
            self.bill_text.config(state='normal')
            self.bill_text.delete("8.0","end")
            for i in range(len(self.veg)):
                each_tot=0.0
                if self.ck[i].get()==1 and self.qty[i].get()>0:
                    self.bill_text.insert("end", "\nCustomer Details\n\tCustmor Name   :"+self.c_name.get()+
                                            "\n\tContact number  :"+self.c_phno.get()+"\n\tAddress\t         :"+self.c_add.get())
                    self.bill_text.tag_add("details_head", "8.0","8.16")
                    self.bill_text.tag_config("details_head", font=('Arial',13,'underline'),justify='center')
                    self.bill_text.tag_add("details_body", "9.0","11.50")
                    self.bill_text.tag_config("details_body", font=('Arial',10),justify='left')
                    self.bill_text.insert("end", "\n\n"+"\t"+"item"+"\t"+"qty"+"\t"+"dis"+"\t"+"Total\n")
                    each_tot=each_tot+self.veg_price[i]*self.qty[i].get()
                    each_tot=each_tot-((each_tot/100)*self.dis[i].get())
                    self.each_price[i].config(text=str(each_tot)+" Rs")
                    self.tot=self.tot+each_tot
                    self.total_price.config(text=str(self.tot)+" Rs")
                    self.bill_text.config(state='normal')
                    self.bill_text.insert("end","\n"+"\t"+self.veg[i]+"\t"+str(self.qty[i].get())+"\t"+str(self.dis[i].get())+"\t"+str(each_tot))
                    self.bill_text.tag_add("items",str(line),"end")
                    self.bill_text.tag_config("items",font=('Arial',10),justify='left')
                    self.bill_text.config(state='disabled')
                    line=line+1
                else:
                    self.each_price[i].config(text="0 Rs")
                    self.qty[i].set(0)
                    self.dis[i].set(0)
            self.bill_text.config(state='normal')
            self.bill_text.insert("end", "\n\n\t\t               GST(18%) :"+"{:.2f}".format(((self.tot)/100)*18))
            self.bill_text.insert("end","\n\t\t              -------------------------")
            self.bill_text.insert("end","\n\t\t                 Total amt :"+"{:.2f}".format((self.tot+((self.tot)/100)*18)))
            self.bill_text.config(state='disabled')         
    def close(self):
        exit()
    def clear(self):
        for i in range(len(self.veg)):
            self.ck[i].set(0)
            self.each_price[i].config(text="0 Rs")
            self.qty[i].set(0)
            self.dis[i].set(0)
        self.bill_text.config(state='normal')
        self.bill_text.delete("8.0","end")
        self.bill_text.config(state='disabled')
    def save_bill(self):
        import datetime
        from tkinter import messagebox
        if self.c_name.get()!='' and self.c_phno.get()!='' and self.c_add.get()!='' and self.tot!=0:
            self.t = datetime.datetime.now()
            self.dt=str(self.t.day)+str(self.t.month)+str(self.t.year)+str(self.t.hour)+str(self.t.minute)
            self.file_name=self.c_name.get()+self.dt
            self.file=open(self.file_name+".txt","w")
            self.file.write(self.bill_text.get("1.0","end"))
            self.file.close()
            self.clear()
            messagebox.showinfo("showinfo", "Saved Successfully")
if __name__ == "__main__":
    win=tk.Tk()
    #title
    win.title("billing system")
    #setting tkinter window size
    win.geometry("1200x600+0+0")
    #bg color
    win.config(bg="blue")
    win.resizable(0,0)
    app=App(win)
    win.mainloop()
