import tkinter as tk
from tkinter import *

class App():
    def __init__(self,root):
        ##########--------------Company name-------------##########
        main_heading=Label(root,text="Green Vegetables Market",font=('Arial',30),width=(84)).place(x=0,y=0)
        customer_details=Label(root,text="Customer Details",font=('Arial',30),width=(84),bg="black",fg="white").place(x=0,y=60)
        cname_title=Label(root,text="Enter Custmor Name",font=('Arial',18)).place(x=5,y=120)
        cname_entry=Entry(root,font=('Arial',18),width=(20)).place(x=245,y=120)
        pno_title=Label(root,text="Enter contact number",font=('Arial',18)).place(x=525,y=120)
        pno_entry=Entry(root,font=('Arial',18),width=(20)).place(x=769,y=120)
        add_title=Label(root,text="Enter Address",font=('Arial',18)).place(x=1045,y=120)
        add_entry=Entry(root,font=('Arial',18),width=(20)).place(x=1210,y=120)
        gender_title=Label(root,text="Gender",font=('Arial',18)).place(x=1485,y=120)
        gender_entry=Radiobutton(root,text="Male",value=1,font=('Arial',18)).place(x=1575,y=120)
        gender_entry=Radiobutton(root,text="Female",value=2,font=('Arial',18)).place(x=1680,y=120)

        ##########---------------Particulars-------------###########

        items_heading=Label(root,text="Particulars",font=('Arial',30),fg='white',bg='black',width=(50)).place(x=5,y=180)
        veg=['Potato','Tomato','Carrot','Brinjal','Onions','Cabage','Ginger','Chilli','Garlic','Beetroot']
        i=1
        y_value=300
        Label(root,text="ItemNo     Vegetables              Qty         Discount        GST     Total                 ",font=('Arial',23)).place(x=10,y=240)
        for v in veg:
            name='Button'+str(i)
            item_no='Item'+str(i)
            qty_item=v+'qty'
            Label(root,text=item_no,font=('Arial',23)).place(x=10,y=y_value)
            name = Checkbutton(root, text = v, 
                    #variable = Checkbutton+i,
                    onvalue = 1,
                    offvalue = 0,
                    font=('Arial',23),
                    width = 13,
                    anchor="w"
                    ).place(x=130,y=y_value)
            qty_e=Entry(root,font=('Arial',23),width=2).place(x=430,y=y_value)
            Label(root,text=".kg",font=('Arial',23)).place(x=480,y=y_value)
            dis_e=Entry(root,font=('Arial',23),width=2).place(x=580,y=y_value)
            Label(root,text="% ",font=('Arial',23)).place(x=630,y=y_value)
            Label(root,text="18% ",font=('Arial',23)).place(x=750,y=y_value)
            Label(root,text="total Rs",font=('Arial',23)).place(x=850,y=y_value)
            i=i+1
            y_value=y_value+60
        cal=Button(root,text="Caculate",font=('Arial',23)).place(x=850,y=900)
        ##########-----------line-------------##########
        v_line=Label(root,font=(30),bg='black',width=(3),height=(40)).place(x=1100,y=180)
        ##########-----------Bill-------------##########
        bill_heading=Label(root,text="Bill",font=('Arial',30),fg='white',bg='black',width=(32)).place(x=1130,y=180)
        complete_and_save=Button(root,text="Complete and Save",font=('Arial',23)).place(x=1500,y=900)

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
