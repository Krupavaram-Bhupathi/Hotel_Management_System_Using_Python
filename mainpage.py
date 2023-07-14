from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql
from tkinter import ttk
import mysql.connector
import random
from tkinter import ttk
from time import strptime
from datetime import datetime

root=Tk()
root.title("Hotel Management System Using Python")
root.geometry('1370x760')
my_img=ImageTk.PhotoImage(Image.open("C:\\Users\\Krupa\\Downloads\\minimages\\main.png"))
my_l=Label(image=my_img)
my_l.pack()
def checking():
    root=Toplevel()
    root.geometry('1366x768')
    root.title("Checking")
    my_img=PhotoImage(file="C:\\Users\\Krupa\\Downloads\\checking.png")
    k=Label(root,image=my_img).pack()
    logo=PhotoImage(file="C:\\Users\\Krupa\\Downloads\\minimages\\LOGO.png")
    b1=Button(root,image=logo,bd=0,bg="#050a30",activebackground="#050a30",cursor="hand2",command=home).place(x=30,y=15)
    def fetch_datafeed():
        conn=mysql.connector.connect(host="localhost",username="root",password="binny219",database="userdata")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from feedback")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            feed_table.delete(*feed_table.get_children())
            for i in rows:
                feed_table.insert("",END,values=i)
        conn.commit()
        conn.close()

    def fetch_databook():
            conn=mysql.connector.connect(host="localhost",username="root",password="binny219",database="userdata")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from room")
            rows=my_cursor.fetchall()
            if len(rows)!=0:
                room_table.delete(*room_table.get_children())
                for i in rows:
                    room_table.insert("",END,values=i)
            conn.commit()
            conn.close()
    def fetch_dataroom():
            conn=mysql.connector.connect(host="localhost",username="root",password="binny219",database="userdata")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from details")
            rows=my_cursor.fetchall()
            if len(rows)!=0:
                room_table.delete(*room_table.get_children())
                for i in rows:
                    room_table.insert("",END,values=i)
            conn.commit()
            conn.close()
    def fetch_datacustomers():
        conn=mysql.connector.connect(host="localhost",username="root",password="binny219",database="userdata")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from customer")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            cust_details_table.delete(*cust_details_table.get_children())
            for i in rows:
                cust_details_table.insert("",END,values=i)
        conn.commit()
        conn.close()
    ltable1=LabelFrame(root,bd=1,relief=RIDGE,text="Customer Details ",font=("times new roman",18,'bold'),padx=2,bg="#fbf5e9")
    ltable1.place(x=60,y=155,width=660,height=250)

    details_table=Frame(ltable1,bd=2,relief=RIDGE)
    details_table.place(x=0,y=10,width=640,height=200)

    scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
    scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

    cust_details_table=ttk.Treeview(details_table,column=("Ref","Name","Age","Gender","mobile no","email","nationality","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_y.pack(side=RIGHT,fill=Y)

    scroll_x.config(command=cust_details_table.xview)
    scroll_y.config(command=cust_details_table.yview)

    cust_details_table.heading("Ref",text="Refer no")
    cust_details_table.heading("Name",text="Name")
    cust_details_table.heading("Age",text="Age")
    cust_details_table.heading("Gender",text="Gender")
    cust_details_table.heading("mobile no",text="mobile no")
    cust_details_table.heading("email",text="email")
    cust_details_table.heading("nationality",text="nationality")
    cust_details_table.heading("address",text="address")

    cust_details_table["show"]="headings"
    cust_details_table.column("Ref",width=100)
    cust_details_table.column("Name",width=100)
    cust_details_table.column("Age",width=100)
    cust_details_table.column("Gender",width=100)
    cust_details_table.column("mobile no",width=100)
    cust_details_table.column("email",width=100)
    cust_details_table.column("nationality",width=100)
    cust_details_table.column("address",width=100)

    cust_details_table.pack(fill=BOTH,expand=1)
    #cust_details_table.bind("<ButtonRelease-1>",get_cursor)
    fetch_datacustomers()
    #-------------------------------------------------------------------------------------------------------------------------------
    ltable2=LabelFrame(root,bd=1,relief=RIDGE,text="Booking Details",font=("times new roman",18,'bold'),padx=2,bg="#fbf5e9")
    ltable2.place(x=730,y=155,width=620,height=250)
    details_table2=Frame(ltable2,bd=2,relief=RIDGE)
    details_table2.place(x=0,y=10,width=600,height=200)

    scroll_x=ttk.Scrollbar(details_table2,orient=HORIZONTAL)
    scroll_y=ttk.Scrollbar(details_table2,orient=VERTICAL)

    room_table=ttk.Treeview(details_table2,column=("contact","checkindate","checkoutdate","roomtype","meal","nofdays"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_y.pack(side=RIGHT,fill=Y)

    scroll_x.config(command=room_table.xview)
    scroll_y.config(command=room_table.yview)

    room_table.heading("contact",text="Contact")
    room_table.heading("checkindate",text="Check in date")
    room_table.heading("checkoutdate",text="Check out date")
    room_table.heading("roomtype",text="Room Type")
    #room_table.heading("roomavailable",text="Room Available")
    room_table.heading("meal",text="Meal")
    room_table.heading("nofdays",text="No of Days")
    #room_table.heading("paidtax",text="Paid tax")
    #room_table.heading("subtotal",text="Sub total")
    #room_table.heading("total",text="Total")

    room_table["show"]="headings"
    room_table.column("contact",width=100)
    room_table.column("checkindate",width=100)
    room_table.column("checkoutdate",width=100)
    room_table.column("roomtype",width=100)
    #room_table.column("roomavailable",width=100)
    room_table.column("meal",width=100)
    room_table.column("nofdays",width=100)
    #room_table.column("paidtax",width=100)
    #room_table.column("subtotal",width=100)
    #room_table.column("total",width=100)

    room_table.pack(fill=BOTH,expand=1)
    fetch_databook()
    #--------------------------------------------------------------------------------------------------------------------------------
    ltable3=LabelFrame(root,bd=1,relief=RIDGE,text="Feedback Details",font=("times new roman",18,'bold'),padx=2,bg="#fbf5e9")
    ltable3.place(x=60,y=410,width=660,height=250)
    scroll_x=ttk.Scrollbar(ltable3,orient=HORIZONTAL)
    scroll_y=ttk.Scrollbar(ltable3,orient=VERTICAL)

    feed_table=ttk.Treeview(ltable3,column=("Rating","Aspects","Improvements","Addtional_feedback"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_y.pack(side=RIGHT,fill=Y)

    scroll_x.config(command=feed_table.xview)
    scroll_y.config(command=feed_table.yview)

    feed_table.heading("Rating",text="Rating")
    feed_table.heading("Aspects",text="Aspects")
    feed_table.heading("Improvements",text="Improvements")
    feed_table.heading("Addtional_feedback",text="Addtional_feedback")



    feed_table["show"]="headings"
    feed_table.column("Rating",width=100)
    feed_table.column("Aspects",width=200)
    feed_table.column("Improvements",width=200)
    feed_table.column("Addtional_feedback",width=200)



    feed_table.pack(fill=BOTH,expand=1)
    #room_table.bind("<ButtonRelease-1>",get_cursor)
    fetch_datafeed()
    #--------------------------------------------------------------------------------------------------------------------------------------
    ltable4=LabelFrame(root,bd=1,relief=RIDGE,text="Room Details",font=("times new roman",18,'bold'),padx=2,bg="#fbf5e9")
    ltable4.place(x=730,y=410,width=620,height=250)
    scroll_x=ttk.Scrollbar(ltable4,orient=HORIZONTAL)
    scroll_y=ttk.Scrollbar(ltable4,orient=VERTICAL)

    room_table=ttk.Treeview(ltable4,column=("Floor no","Room No","Room Type"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_y.pack(side=RIGHT,fill=Y)

    scroll_x.config(command=room_table.xview)
    scroll_y.config(command=room_table.yview)

    room_table.heading("Floor no",text="Floor No")
    room_table.heading("Room No",text="Room No")
    room_table.heading("Room Type",text="Room Type")


    room_table["show"]="headings"
    room_table.column("Floor no",width=100)
    room_table.column("Room No",width=100)
    room_table.column("Room Type",width=100)


    room_table.pack(fill=BOTH,expand=1)
    #room_table.bind("<ButtonRelease-1>",get_cursor)
    fetch_dataroom()

    root.mainloop()
def feedback():
    root=Toplevel()
    root.geometry('1366x768')
    root.title("Feedback")
    my_img=PhotoImage(file="C:\\Users\\Krupa\\Downloads\\feedback.png")
    k=Label(root,image=my_img).pack()
    logo=PhotoImage(file="C:\\Users\\Krupa\\Downloads\\minimages\\LOGO.png")
    b1=Button(root,image=logo,bd=0,bg="#050a30",activebackground="#050a30",cursor="hand2",command=home).place(x=30,y=15)
    frame=Frame(root,width=700,height=460,bg='#fbf5e9')
    frame.place(x=630,y=149)
    img=ImageTk.PhotoImage(Image.open("C:\\Users\\Krupa\\Downloads\\minimages\\fedback.png"))
    Label(root,image=img,border=0,bg="white").place(x=100,y=180)
    def adddata():
                if user.get()=="" or code.get()=="" or q3.get()=="" or q4.get()=="":
                    messagebox.showerror("Error","All fields are required",parent=root)
                else:
                    try:
                        conn=mysql.connector.connect(host="localhost",username="root",password="binny219",database="userdata")
                        my_cursor=conn.cursor()
                        my_cursor.execute("insert into feedback values(%s,%s,%s,%s)",(user.get(),code.get(),q3.get(),q4.get()))
                        conn.commit()
                        conn.close()
                        messagebox.showinfo("success","Feedback submitted",parent=root)
                        
                    except Exception as es:
                        messagebox.showwarning("Warning",f"Something went wrong:{str(es)}",parent=root)
    # q1 
    lcustcon=Label(frame,text="Q1. How satisfied are you with our service?(Rate 1 to 5)",font=("times new roman",15,'bold'),padx=2,pady=7,bg="#fbf5e9").place(x=20,y=10)

    user=Entry(frame,width=25,fg='black',border=0,bg='#fbf5e9',font=('Microsoft Yahei UI Light',11))
    user.place(x=25,y=60)

    Frame(frame,width=600,height=2,bg='black').place(x=25,y=85)
    # q2
    Label(frame,text="Q2. What aspects of our service do you find most valuable?",font=("times new roman",15,'bold'),padx=2,pady=7,bg="#fbf5e9").place(x=20,y=95)
    code=Entry(frame,width=25,fg='black',border=0,bg='#fbf5e9',font=('Microsoft Yahei UI Light',11))
    code.place(x=30,y=150)
    Frame(frame,width=600,height=2,bg='black').place(x=25,y=175)
    #q3
    Label(frame,text="Q3. What areas do you think we can improve?",font=("times new roman",15,'bold'),padx=2,pady=7,bg="#fbf5e9").place(x=20,y=185)
    q3=Entry(frame,width=25,fg='black',border=0,bg='#fbf5e9',font=('Microsoft Yahei UI Light',11))
    q3.place(x=30,y=240)
    Frame(frame,width=600,height=2,bg='black').place(x=25,y=270)

    #q4
    Label(frame,text="Q4. Is there additional feedback you would like to provide?",font=("times new roman",15,'bold'),padx=2,pady=7,bg="#fbf5e9").place(x=20,y=285)
    q4=Entry(frame,width=25,fg='black',border=0,bg='#fbf5e9',font=('Microsoft Yahei UI Light',11))
    q4.place(x=30,y=340)
    Frame(frame,width=600,height=2,bg='black').place(x=25,y=370)
    #q5

    btnAdd=Button(frame,text="SUBMIT",font=("times new roman",18,'bold'),bg="#050a30",fg="white",width=12,bd=0,command=adddata)
    btnAdd.place(x=50,y=400)
    root.mainloop()
def checkout():
    root=Toplevel()
    root.geometry('1366x768')
    root.title("Check Out")
    my_img=PhotoImage(file="C:\\Users\\Krupa\\Downloads\\checkout.png")
    k=Label(root,image=my_img).pack()
    logo=PhotoImage(file="C:\\Users\\Krupa\\Downloads\\minimages\\LOGO.png")
    b1=Button(root,image=logo,bd=0,bg="#050a30",activebackground="#050a30",cursor="hand2",command=home).place(x=30,y=15)
    img=ImageTk.PhotoImage(Image.open("C:\\Users\\Krupa\\Downloads\\minimages\\checko.png"))
    Label(root,image=img,border=0,bg="white").place(x=100,y=145)
    def checko():
                if u.get()=="" or user.get()=="" or code.get()=="":
                    messagebox.showerror("Error","All fields are required")
                else:
                    mDelete=messagebox.askyesno("Hotel Management System","Do you really want to check-out?",parent=root)
                    if mDelete>0:
                        conn=mysql.connector.connect(host="localhost",username="root",password="binny219",database="userdata")
                        my_cursor=conn.cursor()
                        query="delete from customer where Mobile=%s"
                        q="delete from room where contact=%s"
                        value=(user.get(),)
                        my_cursor.execute(query,value)
                        my_cursor.execute(q,value)
                        r1=my_cursor.fetchall()
                        r2=my_cursor.fetchall()
                        if len(r1)!=0 and len(r2)!=0:
                            messagebox.showinfo("Success","Check-out Done",parent=root)
                        else:
                            messagebox.showerror("Error","User doesn't exists")
                    else:
                        if not mDelete:
                            return
                    conn.commit()
                    conn.close()
    frame=Frame(root,width=500,height=300,bg='#fbf5e9')
    frame.place(x=780,y=240)
    def on_enter(e):
        u.delete(0,'end')
    def on_leave(e):
        name=u.get()
        if name=='':
            user.insert(0,'Username')
    u=Entry(frame,width=25,fg='black',border=0,bg='#fbf5e9',font=('Microsoft Yahei UI Light',11))
    u.place(x=30,y=28)
    u.insert(0,'Reference No')
    u.bind('<FocusIn>',on_enter)
    #user.bind('<FocusOut>',on_leave)
    Frame(frame,width=295,height=2,bg='black').place(x=25,y=60)
    # user 
    def on_enter(e):
        user.delete(0,'end')
    def on_leave(e):
        name=user.get()
        if name=='':
            user.insert(0,'Username')
    user=Entry(frame,width=25,fg='black',border=0,bg='#fbf5e9',font=('Microsoft Yahei UI Light',11))
    user.place(x=30,y=88)
    user.insert(0,'Mobile No')
    user.bind('<FocusIn>',on_enter)
    #user.bind('<FocusOut>',on_leave)
    Frame(frame,width=295,height=2,bg='black').place(x=25,y=120)
    # 
    def on_enter(e):
        code.delete(0,'end')
    def on_leave(e):
        name=code.get()
        if name=='':
            code.insert(0,'Name')
    code=Entry(frame,width=25,fg='black',border=0,bg='#fbf5e9',font=('Microsoft Yahei UI Light',11))
    code.place(x=30,y=145)
    code.insert(0,'Name')
    code.bind('<FocusIn>',on_enter)
    Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)
    btnAdd=Button(frame,text="CHECK-OUT",font=("times new roman",18,'bold'),bg="#050a30",fg="white",width=15,bd=0,command=checko)
    btnAdd.place(x=50,y=230)
    root.mainloop()
def addroom():
    root=Toplevel()
    root.geometry('1366x768')
    root.title("Adding Rooms")
    my_img=PhotoImage(file="C:\\Users\\Krupa\\Downloads\\addrooms.png")
    k=Label(root,image=my_img).pack()
    logo=PhotoImage(file="C:\\Users\\Krupa\\Downloads\\minimages\\LOGO.png")
    b1=Button(root,image=logo,bd=0,bg="#050a30",activebackground="#050a30",cursor="hand2",command=home).place(x=30,y=15)

    #---functions---
    def reset():
        var_floor.set("")
        var_room.set("")
        var_roty.set("")
        
    def delete_data():
            mDelete=messagebox.askyesno("Hotel Management System","Do you really want to delete this room",parent=root)
            if mDelete>0:
                conn=mysql.connector.connect(host="localhost",username="root",password="binny219",database="userdata")
                my_cursor=conn.cursor()
                query="delete from details where RoomNo=%s"
                value=(var_room.get(),)
                my_cursor.execute(query,value)
                
            else:
                if not mDelete:
                    return
            conn.commit()
            fetch_data()
            conn.close()
    def update_data():
            if var_floor.get()=="":
                messagebox.showerror("Error","Please enter room number",parent=root)
            else:
                conn=mysql.connector.connect(host="localhost",username="root",password="binny219",database="userdata")
                my_cursor=conn.cursor()
                my_cursor.execute("update details set Floor=%s,Roomtype=%s where RoomNo=%s",(var_floor.get(),var_roty.get(),var_room.get()))
                
                conn.commit()
                fetch_data()
                conn.close()
                messagebox.showinfo("Update","Room details has been updated Successfully",parent=root)
    def get_cursor(event=""):
            cursor_row=room_table.focus()
            content=room_table.item(cursor_row)
            row=content["values"]

            var_floor.set(row[0])
            var_room.set(row[1])
            var_roty.set(row[2])
            
    def fetch_data():
            conn=mysql.connector.connect(host="localhost",username="root",password="binny219",database="userdata")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from details")
            rows=my_cursor.fetchall()
            if len(rows)!=0:
                room_table.delete(*room_table.get_children())
                for i in rows:
                    room_table.insert("",END,values=i)
            conn.commit()
            conn.close()
    def add_data():
            if var_floor.get()=="" or var_roty.get()=="" or var_room.get()=="":
                messagebox.showerror("Error","All fields are required",parent=root)
            else:
                try:
                    conn=mysql.connector.connect(host="localhost",username="root",password="binny219",database="userdata")
                    my_cursor=conn.cursor()
                    my_cursor.execute("insert into details values(%s,%s,%s)",(var_floor.get(),var_room.get(),var_roty.get()))
                    
                    conn.commit()
                    fetch_data()
                    conn.close()
                    messagebox.showinfo("success","Room added",parent=root)
                    
                except Exception as es:
                    messagebox.showwarning("Warning",f"Something went wrong:{str(es)}",parent=root)


    #---variables----
    var_floor=StringVar()
    var_room=StringVar()
    var_roty=StringVar()

    #--------------customer details frame----------
    lleft=LabelFrame(root,bd=1,relief=RIDGE,text="Adding New Rooms",font=("times new roman",18,'bold'),padx=2,pady=5,bg="#fbf5e9")
    lleft.place(x=70,y=150,width=425,height=510)

    #-------labels and entry----------------------
    #customer contact
    lcustcon=Label(lleft,text="Floor:-",font=("times new roman",12,'bold'),padx=2,pady=7,bg="#fbf5e9")
    lcustcon.grid(row=0,column=0,sticky=W)

    enty_con=ttk.Entry(lleft,width=20,font=("times new roman",13,'bold'),textvariable=var_floor)
    enty_con.grid(row=0,column=1,padx=3,sticky=W)

    #checkin date
    lcustcheckin=Label(lleft,text="Room No:-",font=("times new roman",12,'bold'),padx=2,pady=7,bg="#fbf5e9")
    lcustcheckin.grid(row=1,column=0,sticky=W)

    enty_checkin=ttk.Entry(lleft,width=20,font=("times new roman",13,'bold'),textvariable=var_room)
    enty_checkin.grid(row=1,column=1,padx=3)
    #checkout date
    lcustcheckout=Label(lleft,text="Room Type:-",font=("times new roman",12,'bold'),padx=2,pady=7,bg="#fbf5e9")
    lcustcheckout.grid(row=2,column=0,sticky=W)
    combo_nat=ttk.Combobox(lleft,font=("times new roman",13,'bold'),width=20,textvariable=var_roty)
    combo_nat["value"]=("Single","Double","Luxury","Duplex")
    combo_nat.current()
    combo_nat.grid(row=2,column=1,padx=3)
    


    #-----------btns-----------------
    btn_frame=Frame(lleft,bd=0,relief=RIDGE,bg="#fbf5e9")
    btn_frame.place(x=300,y=230,width=100,height=200)

    btnAdd=Button(btn_frame,text="Add",font=("times new roman",18,'bold'),bg="#050a30",fg="white",width=5,bd=0,command=add_data)
    btnAdd.grid(row=0,column=0,pady=5)

    btnupdate=Button(btn_frame,text="Update",font=("times new roman",18,'bold'),bg="#050a30",fg="white",width=5,bd=0,command=update_data)
    btnupdate.grid(row=1,column=0,pady=5)

    btnreset=Button(btn_frame,text="Reset",font=("times new roman",18,'bold'),bg="#050a30",fg="white",width=5,bd=0,command=reset)
    btnreset.grid(row=2,column=0,pady=5)

    btndel=Button(btn_frame,text="Delete",font=("times new roman",18,'bold'),bg="#050a30",fg="white",width=5,bd=0,command=delete_data)
    btndel.grid(row=3,column=0,pady=5)

    #table frame
    ltable=LabelFrame(root,bd=1,relief=RIDGE,text="View Details and Search",font=("times new roman",18,'bold'),padx=2,bg="#fbf5e9")
    ltable.place(x=500,y=160,width=845,height=500)

    scroll_x=ttk.Scrollbar(ltable,orient=HORIZONTAL)
    scroll_y=ttk.Scrollbar(ltable,orient=VERTICAL)

    room_table=ttk.Treeview(ltable,column=("Floor no","Room No","Room Type"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_y.pack(side=RIGHT,fill=Y)

    scroll_x.config(command=room_table.xview)
    scroll_y.config(command=room_table.yview)

    room_table.heading("Floor no",text="Floor No")
    room_table.heading("Room No",text="Room No")
    room_table.heading("Room Type",text="Room Type")


    room_table["show"]="headings"
    room_table.column("Floor no",width=100)
    room_table.column("Room No",width=100)
    room_table.column("Room Type",width=100)


    room_table.pack(fill=BOTH,expand=1)
    room_table.bind("<ButtonRelease-1>",get_cursor)
    fetch_data()
    root.mainloop()


def roombooking():
    root=Toplevel()
    root.geometry('1366x768')
    root.title("Room Booking")
    my_img=PhotoImage(file="C:\\Users\\Krupa\\Downloads\\minimages\\roombook.png")
    k=Label(root,image=my_img).pack()
    logo=PhotoImage(file="C:\\Users\\Krupa\\Downloads\\minimages\\LOGO.png")
    b1=Button(root,image=logo,bd=0,bg="#050a30",activebackground="#050a30",cursor="hand2",command=home).place(x=30,y=15)



    #---functions---
    def search():
            conn=mysql.connector.connect(host="localhost",username="root",password="binny219",database="userdata")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from room where "+str(search_var.get())+" LIKE '%"+str(txt_search.get())+"%'")
            rows=my_cursor.fetchall()
            if len(rows)!=0:
                room_table.delete(*room_table.get_children())
                for i in rows:
                    room_table.insert("",END,values=i)
                conn.commit()
            conn.close()
    def total():
        indate=var_checkin.get()
        outdate=var_checkout.get()
        indate=datetime.strptime(indate,"%d/%m/%Y")
        outdate=datetime.strptime(outdate,"%d/%m/%Y")
        k=(outdate-indate).days
        if k>0:
            var_nofdays.set(k)
        else:
            messagebox.showerror("Error","Please enter valid dates",parent=root)
        d={"Single":500,"Double":800,"Luxury":1000,"Duplex":1500}
        if(var_meal.get()=="BreakFast"):
            q1=float(300)
            q2=float(d[(var_roty.get()[4:])])
            q3=float(var_nofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            tax="Rs."+str("%.2f"%((q5)*0.1))
            st="Rs."+str("%.2f"%((q5)))
            tt="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            var_tax.set(tax)
            var_stotal.set(st)
            var_total.set(tt)
        elif(var_meal.get()=="Lunch"):
            q1=float(500)
            q2=float(d[(var_roty.get()[4:])])
            q3=float(var_nofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            tax="Rs."+str("%.2f"%((q5)*0.1))
            st="Rs."+str("%.2f"%((q5)))
            tt="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            var_tax.set(tax)
            var_stotal.set(st)
            var_total.set(tt)
        elif(var_meal.get()=="Dinner"):
            q1=float(400)
            q2=float(d[(var_roty.get()[4:])])
            q3=float(var_nofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            tax="Rs."+str("%.2f"%((q5)*0.1))
            st="Rs."+str("%.2f"%((q5)))
            tt="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            var_tax.set(tax)
            var_stotal.set(st)
            var_total.set(tt)
                          

        
    def reset():
        var_contact.set("")
        var_checkin.set("")
        var_checkout.set("")
        var_roty.set("")
        #var_roomavail.set("")
        var_meal.set("")
        var_nofdays.set("")
        var_tax.set("")
        var_stotal.set("")
        var_total.set("")
        
    def delete_data():
            mDelete=messagebox.askyesno("Hotel Management System","Do you really want to delete this room",parent=root)
            if mDelete>0:
                conn=mysql.connector.connect(host="localhost",username="root",password="binny219",database="userdata")
                my_cursor=conn.cursor()
                query="delete from room where contact=%s"
                value=(var_contact.get(),)
                my_cursor.execute(query,value)
                
            else:
                if not mDelete:
                    return
            conn.commit()
            fetch_data()
            conn.close()
    def update_data():
            if var_contact.get()=="":
                messagebox.showerror("Error","Please enter mobile number",parent=root)
            else:
                conn=mysql.connector.connect(host="localhost",username="root",password="binny219",database="userdata")
                my_cursor=conn.cursor()
                my_cursor.execute("update room set checkin=%s,checkout=%s,roomtype=%s,meal=%s,noofdays=%s where contact=%s",(var_checkin.get(),var_checkout.get(),var_roty.get(),var_meal.get(),var_nofdays.get(),var_contact.get()))
                
                conn.commit()
                fetch_data()
                conn.close()
                messagebox.showinfo("Update","Room details has been updated Successfully",parent=root)
    def get_cursor(event=""):
            cursor_row=room_table.focus()
            content=room_table.item(cursor_row)
            row=content["values"]

            var_contact.set(row[0])
            var_checkin.set(row[1])
            var_checkout.set(row[2])
            var_roty.set(row[3])
            #var_roomavail.set(row[4])
            var_meal.set(row[4])
            var_nofdays.set(row[5])
    def fetch_data():
            conn=mysql.connector.connect(host="localhost",username="root",password="binny219",database="userdata")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from room")
            rows=my_cursor.fetchall()
            if len(rows)!=0:
                room_table.delete(*room_table.get_children())
                for i in rows:
                    room_table.insert("",END,values=i)
            conn.commit()
            conn.close()
    def add_data():
            if var_contact.get()=="" or var_checkin.get()=="":
                messagebox.showerror("Error","All fields are required",parent=root)
            else:
                try:
                    conn=mysql.connector.connect(host="localhost",username="root",password="binny219",database="userdata")
                    my_cursor=conn.cursor()
                    my_cursor.execute("insert into room values(%s,%s,%s,%s,%s,%s)",(var_contact.get(),var_checkin.get(),var_checkout.get(),var_roty.get(),var_meal.get(),var_nofdays.get()))
                    
                
                    conn.commit()
                    fetch_data()
                    conn.close()
                    messagebox.showinfo("success","Room booked,Pay through QR provided!",parent=root)
                    
                except Exception as es:
                    messagebox.showwarning("Warning","This room already booked,choose another room",parent=root)

    def Fetch_contact():
        if var_contact.get()=="":
            messagebox.showerror("Error","Please enter mobile no",parent=root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="binny219",database="userdata")
            my_cursor=conn.cursor()
            query=("select Name from customer where Mobile=%s")
            value=(var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            if row==None:
                messagebox.showerror("Error","This number not found",parent=root)
            else:
                conn.commit()
                conn.close()

                showdataframe=Frame(root,bd=1,relief=RIDGE,padx=2,bg="#fbf5e9")
                showdataframe.place(x=516,y=155,width=265,height=190)
                #---name---
                lname=Label(showdataframe,text="Name:",font=("times new roman",12,"bold"),bg="#fbf5e9")
                lname.place(x=0,y=0)

                lbl=Label(showdataframe,text=row,font=("times new roman",12,"bold"),bg="#fbf5e9")
                lbl.place(x=90,y=0)
                #---age----
                conn=mysql.connector.connect(host="localhost",username="root",password="binny219",database="userdata")
                my_cursor=conn.cursor()
                query=("select Age from customer where Mobile=%s")
                value=(var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lage=Label(showdataframe,text="Age:",font=("times new roman",12,"bold"),bg="#fbf5e9")
                lage.place(x=0,y=30)

                lbl2=Label(showdataframe,text=row,font=("times new roman",12,"bold"),bg="#fbf5e9")
                lbl2.place(x=90,y=30)
                
                #---gender---
                conn=mysql.connector.connect(host="localhost",username="root",password="binny219",database="userdata")
                my_cursor=conn.cursor()
                query=("select Gender from customer where Mobile=%s")
                value=(var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lgend=Label(showdataframe,text="Gender:",font=("times new roman",12,"bold"),bg="#fbf5e9")
                lgend.place(x=0,y=60)

                lbl3=Label(showdataframe,text=row,font=("times new roman",12,"bold"),bg="#fbf5e9")
                lbl3.place(x=90,y=60)
                #----email---
                conn=mysql.connector.connect(host="localhost",username="root",password="binny219",database="userdata")
                my_cursor=conn.cursor()
                query=("select Email from customer where Mobile=%s")
                value=(var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lemail=Label(showdataframe,text="Email:",font=("times new roman",12,"bold"),bg="#fbf5e9")
                lemail.place(x=0,y=90)

                lbl4=Label(showdataframe,text=row,font=("times new roman",12,"bold"),bg="#fbf5e9")
                lbl4.place(x=90,y=90)
                #------nationlaity----
                conn=mysql.connector.connect(host="localhost",username="root",password="binny219",database="userdata")
                my_cursor=conn.cursor()
                query=("select Nationality from customer where Mobile=%s")
                value=(var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lnat=Label(showdataframe,text="Nationality:",font=("times new roman",12,"bold"),bg="#fbf5e9")
                lnat.place(x=0,y=120)

                lbl5=Label(showdataframe,text=row,font=("times new roman",12,"bold"),bg="#fbf5e9")
                lbl5.place(x=90,y=120)

                #-----Address---
                conn=mysql.connector.connect(host="localhost",username="root",password="binny219",database="userdata")
                my_cursor=conn.cursor()
                query=("select Address from customer where Mobile=%s")
                value=(var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                laddr=Label(showdataframe,text="Address:",font=("times new roman",12,"bold"),bg="#fbf5e9")
                laddr.place(x=0,y=150)

                lbl6=Label(showdataframe,text=row,font=("times new roman",12,"bold"),bg="#fbf5e9")
                lbl6.place(x=90,y=150)
                


                

    #----varaibles----
    var_contact=StringVar()
    var_checkin=StringVar()
    var_checkout=StringVar()
    var_roty=StringVar()
    #var_roomavail=StringVar()
    var_meal=StringVar()
    var_nofdays=StringVar()
    var_tax=StringVar()
    var_stotal=StringVar()
    var_total=StringVar()






    #--------------customer details frame----------
    lleft=LabelFrame(root,bd=1,relief=RIDGE,text="Room Booking",font=("times new roman",18,'bold'),padx=2,pady=5,bg="#fbf5e9")
    lleft.place(x=70,y=150,width=425,height=510)

    #-------labels and entry----------------------
    #customer contact
    lcustcon=Label(lleft,text="Customer Contact:-",font=("times new roman",12,'bold'),padx=2,pady=7,bg="#fbf5e9")
    lcustcon.grid(row=0,column=0,sticky=W)

    enty_con=ttk.Entry(lleft,width=20,font=("times new roman",13,'bold'),textvariable=var_contact)
    enty_con.grid(row=0,column=1,padx=3,sticky=W)
    #fetch data button
    btnfet=Button(lleft,text="Fetch data",font=("times new roman",12,'bold'),bg="#050a30",fg="white",width=8,bd=0,padx=5,command=Fetch_contact)
    btnfet.place(x=330,y=5)
    #checkin date
    '''def on_enter(*args):
        enty_checkin.delete(0,'end')
    def on_leave(*args):
        enty_checkin.delete(0,'end')
        enty_checkin.insert(0,"dd/mm/yyyy")
        root.focus()
            
    lcustcheckin=Label(lleft,text="Check_in Date:-",font=("times new roman",12,'bold'),padx=2,pady=7,bg="#fbf5e9")
    lcustcheckin.grid(row=1,column=0,sticky=W)

    enty_checkin=ttk.Entry(lleft,width=29,font=("times new roman",13,'bold'),textvariable=var_checkin)
    enty_checkin.grid(row=1,column=1,padx=3)
    enty_checkin.insert(0,"dd/mm/yyyy")
    enty_checkin.bind("<Button-1>",on_enter)
    enty_checkin.bind("<Leave>",on_leave)'''
    def on_enter(*args):
        enty_checkin.delete(0,'end')
    def on_leave(*args):
        enty_checkin.delete(0,'end')
        enty_checkin.insert(0,"dd/mm/yyyy")
        root.focus()
    lcustcheckin=Label(lleft,text="Check_in Date:-",font=("times new roman",12,'bold'),padx=2,pady=7,bg="#fbf5e9")
    lcustcheckin.grid(row=1,column=0,sticky=W)

    enty_checkin=ttk.Entry(lleft,width=29,font=("times new roman",13,'bold'),textvariable=var_checkin)
    enty_checkin.grid(row=1,column=1,padx=3)
    enty_checkin.insert(0,"dd/mm/yyyy")
    enty_checkin.bind("<Button-1>",on_enter)
    #enty_checkin.bind("<Leave>",on_leave)
    #checkout date
    def on_enter(*args):
        enty_checkout.delete(0,'end')
    def on_leave(*args):
        if var_checkout.get()=="":
            enty_checkout.insert(0,"dd/mm/yyyy")
        root.focus()
    lcustcheckout=Label(lleft,text="Check_out Date:-",font=("times new roman",12,'bold'),padx=2,pady=7,bg="#fbf5e9")
    lcustcheckout.grid(row=2,column=0,sticky=W)

    enty_checkout=ttk.Entry(lleft,width=29,font=("times new roman",13,'bold'),textvariable=var_checkout)
    enty_checkout.grid(row=2,column=1,padx=3)
    enty_checkout.insert(0,"dd/mm/yyyy")
    enty_checkout.bind("<Button-1>",on_enter)
    #enty_checkout.bind("<Leave>",on_leave)

    #room type
    lcustroty=Label(lleft,text="Room :-",font=("times new roman",12,'bold'),padx=2,pady=7,bg="#fbf5e9")
    lcustroty.grid(row=3,column=0,sticky=W)

    conn=mysql.connector.connect(host="localhost",username="root",password="binny219",database="userdata")
    my_cursor=conn.cursor()
    my_cursor.execute("select RoomNo,Roomtype from details")
    rows=my_cursor.fetchall()
    combo_roty=ttk.Combobox(lleft,font=("times new roman",12,'bold'),width=30,state="readonly",textvariable=var_roty)
    combo_roty["value"]=rows
    combo_roty.current()
    combo_roty.grid(row=3,column=1)
    '''#available room
    lavail=Label(lleft,text="Available room:-",font=("times new roman",12,'bold'),padx=2,pady=7,bg="#fbf5e9")
    lavail.grid(row=4,column=0,sticky=W)

    #enty_avail=ttk.Entry(lleft,width=29,font=("times new roman",13,'bold'),textvariable=var_roomavail)
    #enty_avail.grid(row=4,column=1,padx=3)
    conn=mysql.connector.connect(host="localhost",username="root",password="binny219",database="userdata")
    my_cursor=conn.cursor()
    my_cursor.execute("select RoomNo from details")
    rows=my_cursor.fetchall()
    combo_roav=ttk.Combobox(lleft,font=("times new roman",12,'bold'),width=30,state="readonly",textvariable=var_roomavail)
    combo_roav["value"]=rows
    combo_roav.current()
    combo_roav.grid(row=4,column=1)'''
    #meal
    lmeal=Label(lleft,text="Meal",font=("times new roman",12,'bold'),padx=2,pady=7,bg="#fbf5e9")
    lmeal.grid(row=4,column=0,sticky=W)

    #enty_meal=ttk.Entry(lleft,width=29,font=("times new roman",13,'bold'),textvariable=var_meal)
    enty_meal=ttk.Combobox(lleft,font=("times new roman",12,'bold'),width=30,textvariable=var_meal)
    enty_meal["value"]=("BreakFast","Lunch","Dinner")
    enty_meal.current()
    enty_meal.grid(row=4,column=1,padx=3)
    #no of days
    ldays=Label(lleft,text="No of days:-",font=("times new roman",12,'bold'),padx=2,pady=7,bg="#fbf5e9")
    ldays.grid(row=5,column=0,sticky=W)

    enty_days=ttk.Entry(lleft,width=29,font=("times new roman",13,'bold'),textvariable=var_nofdays,state="readonly")
    enty_days.grid(row=5,column=1,padx=3)
    #paid tax
    ltax=Label(lleft,text="Paid tax:-",font=("times new roman",12,'bold'),padx=2,pady=7,bg="#fbf5e9")
    ltax.grid(row=6,column=0,sticky=W)

    enty_checkin=ttk.Entry(lleft,width=29,font=("times new roman",13,'bold'),textvariable=var_tax,state="readonly")
    enty_checkin.grid(row=6,column=1,padx=3)
    #subtotal
    lstotal=Label(lleft,text="Sub Total:-",font=("times new roman",12,'bold'),padx=2,pady=7,bg="#fbf5e9")
    lstotal.grid(row=7,column=0,sticky=W)

    enty_stotal=ttk.Entry(lleft,width=29,font=("times new roman",13,'bold'),textvariable=var_stotal,state="readonly")
    enty_stotal.grid(row=7,column=1,padx=3)
    #total cost
    ltotal=Label(lleft,text="Total:-",font=("times new roman",12,'bold'),padx=2,pady=7,bg="#fbf5e9")
    ltotal.grid(row=8,column=0,sticky=W)

    enty_total=ttk.Entry(lleft,width=29,font=("times new roman",13,'bold'),textvariable=var_total,state="readonly")
    enty_total.grid(row=8,column=1,padx=3)
    #bill-button
    btn_bill=Button(lleft,text="BILL",font=("times new roman",15,'bold'),bg="#050a30",fg="white",bd=0,command=total)
    btn_bill.grid(row=10,column=1,padx=5,pady=3,sticky=E)

    #-----------btns-----------------
    btn_frame=Frame(lleft,bd=0,relief=RIDGE,bg="#fbf5e9")
    btn_frame.place(x=0,y=400,width=400,height=40)

    btnAdd=Button(btn_frame,text="Add",font=("times new roman",15,'bold'),bg="#050a30",fg="white",width=5,bd=0,command=add_data)
    btnAdd.grid(row=0,column=0,padx=15)

    btnupdate=Button(btn_frame,text="Update",font=("times new roman",15,'bold'),bg="#050a30",fg="white",bd=0,command=update_data)
    btnupdate.grid(row=0,column=1,padx=15)

    btnreset=Button(btn_frame,text="Reset",font=("times new roman",15,'bold'),bg="#050a30",fg="white",bd=0,command=reset)
    btnreset.grid(row=0,column=2,padx=15)

    btndel=Button(btn_frame,text="Delete",font=("times new roman",15,'bold'),bg="#050a30",fg="white",bd=0,command=delete_data)
    btndel.grid(row=0,column=3,padx=15)

    #table frame
    ltable=LabelFrame(root,bd=1,relief=RIDGE,text="View Details and Search",font=("times new roman",18,'bold'),padx=2,bg="#fbf5e9")
    ltable.place(x=500,y=360,width=845,height=300)

    lsearch=Label(ltable,text="Search By:",font=("times new roman",14,'bold'),bg="#fbf5e9")
    lsearch.grid(row=0,column=0,sticky=W)

    search_var=StringVar()
    combo_search=ttk.Combobox(ltable,textvariable=search_var,font=("times new roman",12,'bold'),width=22,state="readonly")
    combo_search["value"]=("contact","roomavailable")
    combo_search.current()
    combo_search.grid(row=0,column=1,padx=4)

    txt_search=StringVar()
    txtsearch=ttk.Entry(ltable,textvariable=txt_search,width=20,font=("times new roman",13,'bold'))
    txtsearch.grid(row=0,column=2,padx=4)


    btnsearch=Button(ltable,text="Search",font=("times new roman",13,'bold'),bg="#050a30",fg="white",bd=0,command=search)
    btnsearch.grid(row=0,column=3,padx=9)

    btnreshowall=Button(ltable,text="Show all",font=("times new roman",13,'bold'),bg="#050a30",fg="white",bd=0,command=fetch_data)
    btnreshowall.grid(row=0,column=4,padx=6)

    #show data table
    details_table=Frame(ltable,bd=2,relief=RIDGE)
    details_table.place(x=0,y=50,width=800,height=180)

    scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
    scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

    room_table=ttk.Treeview(details_table,column=("contact","checkindate","checkoutdate","roomtype","meal","nofdays"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_y.pack(side=RIGHT,fill=Y)

    scroll_x.config(command=room_table.xview)
    scroll_y.config(command=room_table.yview)

    room_table.heading("contact",text="Contact")
    room_table.heading("checkindate",text="Check in date")
    room_table.heading("checkoutdate",text="Check out date")
    room_table.heading("roomtype",text="Room Type")
    #room_table.heading("roomavailable",text="Room Available")
    room_table.heading("meal",text="Meal")
    room_table.heading("nofdays",text="No of Days")
    #room_table.heading("paidtax",text="Paid tax")
    #room_table.heading("subtotal",text="Sub total")
    #room_table.heading("total",text="Total")

    room_table["show"]="headings"
    room_table.column("contact",width=100)
    room_table.column("checkindate",width=100)
    room_table.column("checkoutdate",width=100)
    room_table.column("roomtype",width=100)
    #room_table.column("roomavailable",width=100)
    room_table.column("meal",width=100)
    room_table.column("nofdays",width=100)
    #room_table.column("paidtax",width=100)
    #room_table.column("subtotal",width=100)
    #room_table.column("total",width=100)

    room_table.pack(fill=BOTH,expand=1)
    room_table.bind("<ButtonRelease-1>",get_cursor)
    fetch_data()



    root.mainloop()

    

def addcustomer():
    root=Toplevel()
    root.geometry('1366x768')
    root.title("Add Customer details")
    my_img=PhotoImage(file="C:\\Users\\Krupa\\Downloads\\minimages\\addcust.png")
    k=Label(root,image=my_img).pack()
    logo=PhotoImage(file="C:\\Users\\Krupa\\Downloads\\minimages\\LOGO.png")
    b1=Button(root,image=logo,bd=0,bg="#050a30",activebackground="#050a30",cursor="hand2",command=home).place(x=30,y=15)

    book=PhotoImage(file="C:\\Users\\Krupa\\Downloads\\minimages\\bookroom.png")
    b2=Button(root,image=book,bd=0,bg="#050a30",activebackground="#050a30",cursor="hand2",command=roombooking).place(x=830,y=610)
    #-------functions of buttons-------------
    def search():
        conn=mysql.connector.connect(host="localhost",username="root",password="binny219",database="userdata")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from customer where "+str(search_var.get())+" LIKE '%"+str(txt_search.get())+"%'")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            cust_details_table.delete(*cust_details_table.get_children())
            for i in rows:
                cust_details_table.insert("",END,values=i)
            conn.commit()
        conn.close()
        
    def reset():
        x=random.randint(1000,9999)
        var_ref.set(str(x))
        var_custname.set("")
        var_age.set("")
        var_gend.set("")
        var_mob.set("")
        var_email.set("")
        var_nat.set("")
        var_addr.set("")
        
    def delete_data():
        mDelete=messagebox.askyesno("Hotel Management System","Do you really want to delete this cusomer",parent=root)
        if mDelete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="binny219",database="userdata")
            my_cursor=conn.cursor()
            query="delete from customer where Ref=%s"
            value=(var_ref.get(),)
            my_cursor.execute(query,value)
            reset()
            
        else:
            if not mDelete:
                return
        conn.commit()
        fetch_data()
        conn.close()
            
    def update_data():
        if var_mob.get()=="":
            messagebox.showerror("Error","Please enter mobile number",parent=root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="binny219",database="userdata")
            my_cursor=conn.cursor()
            my_cursor.execute("update customer set Name=%s,Age=%s,Gender=%s,Mobile=%s,Email=%s,Nationality=%s,Address=%s where Ref=%s",(var_custname.get(),var_age.get(),var_gend.get(),var_mob.get(),var_email.get(),var_nat.get(),var_addr.get(),var_ref.get()))
            
            conn.commit()
            fetch_data()
            conn.close()
            messagebox.showinfo("Update","Customer details has been updated Successfully",parent=root)

            
    def get_cursor(event=""):
        cursor_row=cust_details_table.focus()
        content=cust_details_table.item(cursor_row)
        row=content["values"]

        var_ref.set(row[0])
        var_custname.set(row[1])
        var_age.set(row[2])
        var_gend.set(row[3])
        var_mob.set(row[4])
        var_email.set(row[5])
        var_nat.set(row[6])
        var_addr.set(row[7])
        
                          
    def fetch_data():
        conn=mysql.connector.connect(host="localhost",username="root",password="binny219",database="userdata")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from customer")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            cust_details_table.delete(*cust_details_table.get_children())
            for i in rows:
                cust_details_table.insert("",END,values=i)
        conn.commit()
        conn.close()
    def add_data():
        if var_custname.get()=="" or var_mob.get()=="" or var_ref.get()=="" or var_age.get()=="" or var_gend.get()=="" or var_email.get()=="" or var_nat.get()=="" or var_addr.get()=="":
            messagebox.showerror("Error","All fields are required",parent=root)
        else:
            if len(var_mob.get())==10:
                
                try:
                    conn=mysql.connector.connect(host="localhost",username="root",password="binny219",database="userdata")
                    my_cursor=conn.cursor()
                    my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s)",(var_ref.get(),var_custname.get(),var_age.get(),var_gend.get(),var_mob.get(),var_email.get(),var_nat.get(),var_addr.get()))
                    conn.commit()
                    fetch_data()
                    conn.close()
                    messagebox.showinfo("success","Customer has been added",parent=root)
                    
                except Exception as es:
                    messagebox.showwarning("Warning",f"Something went wrong:{str(es)}",parent=root)
            else:
                messagebox.showerror("Error","Enter a valid 10 digit mobile number",parent=root)
                

    #-----variables---
    var_ref=StringVar()
    x=random.randint(1000,9999)
    var_ref.set(str(x))

    var_custname=StringVar()
    var_age=StringVar()
    var_gend=StringVar()
    var_mob=StringVar()
    var_email=StringVar()
    var_nat=StringVar()
    var_addr=StringVar()


    #--------------customer details frame----------
    lleft=LabelFrame(root,bd=1,relief=RIDGE,text="Customer Details",font=("times new roman",18,'bold'),padx=2,pady=5,bg="#fbf5e9")
    lleft.place(x=70,y=150,width=415,height=420)
    #-------labels and entry----------------------
    #customer ref
    lcustref=Label(lleft,text="Customer Ref No:-",font=("times new roman",12,'bold'),padx=2,pady=7,bg="#fbf5e9")
    lcustref.grid(row=0,column=0,sticky=W)

    enty_ref=ttk.Entry(lleft,textvariable=var_ref,width=29,font=("times new roman",13,'bold'),state="readonly")
    enty_ref.grid(row=0,column=1,padx=3)
    #customer name
    lcustname=Label(lleft,text="Customer Name :-",font=("times new roman",12,'bold'),padx=2,pady=7,bg="#fbf5e9")
    lcustname.grid(row=1,column=0,sticky=W)

    enty_name=ttk.Entry(lleft,textvariable=var_custname,width=29,font=("times new roman",13,'bold'))
    enty_name.grid(row=1,column=1)
    #Age
    lcustage=Label(lleft,text="Age:-",font=("times new roman",12,'bold'),padx=2,pady=7,bg="#fbf5e9")
    lcustage.grid(row=2,column=0,sticky=W)

    enty_age=ttk.Entry(lleft,textvariable=var_age,width=29,font=("times new roman",13,'bold'))
    enty_age.grid(row=2,column=1)
    #Gender
    lcustgend=Label(lleft,text="Gender:-",font=("times new roman",12,'bold'),padx=2,pady=7,bg="#fbf5e9")
    lcustgend.grid(row=3,column=0,sticky=W)

    combo_gend=ttk.Combobox(lleft,textvariable=var_gend,font=("times new roman",12,'bold'),width=30,state="readonly")
    combo_gend["value"]=("Male","Female","Other")
    combo_gend.current()
    combo_gend.grid(row=3,column=1)
    #Mobile no
    lcustmob=Label(lleft,text="Mobile no:-",font=("times new roman",12,'bold'),padx=2,pady=7,bg="#fbf5e9")
    lcustmob.grid(row=4,column=0,sticky=W)

    enty_mob=ttk.Entry(lleft,textvariable=var_mob,width=29,font=("times new roman",13,'bold'))
    enty_mob.grid(row=4,column=1)
    #Email
    lcustmail=Label(lleft,text="Email:-",font=("times new roman",12,'bold'),padx=2,pady=7,bg="#fbf5e9")
    lcustmail.grid(row=5,column=0,sticky=W)

    enty_mail=ttk.Entry(lleft,textvariable=var_email,width=29,font=("times new roman",13,'bold'))
    enty_mail.grid(row=5,column=1)
    #Nationality
    lcustnat=Label(lleft,text="Nationality:-",font=("times new roman",12,'bold'),padx=2,pady=7,bg="#fbf5e9")
    lcustnat.grid(row=6,column=0,sticky=W)

    combo_nat=ttk.Combobox(lleft,textvariable=var_nat,font=("times new roman",12,'bold'),width=30,state="readonly")
    combo_nat["value"]=("Indian","Non-indian")
    combo_nat.current()
    combo_nat.grid(row=6,column=1)

    #Address
    lcustaddr=Label(lleft,text="Address:-",font=("times new roman",12,'bold'),padx=2,pady=7,bg="#fbf5e9")
    lcustaddr.grid(row=7,column=0,sticky=W)



    enty_mai=ttk.Entry(lleft,textvariable=var_addr,width=29,font=("times new roman",13,'bold'))
    enty_mai.grid(row=7,column=1)

    #-----------btns-----------------
    btn_frame=Frame(lleft,bd=0,relief=RIDGE,bg="#fbf5e9")
    btn_frame.place(x=0,y=330,width=400,height=40)

    btnAdd=Button(btn_frame,text="Add",font=("times new roman",15,'bold'),bg="#050a30",fg="white",command=add_data,width=5,bd=0)
    btnAdd.grid(row=0,column=0,padx=15)

    btnupdate=Button(btn_frame,text="Update",font=("times new roman",15,'bold'),bg="#050a30",fg="white",command=update_data,bd=0)
    btnupdate.grid(row=0,column=1,padx=15)

    btnreset=Button(btn_frame,text="Reset",font=("times new roman",15,'bold'),bg="#050a30",fg="white",command=reset,bd=0)
    btnreset.grid(row=0,column=2,padx=15)

    btndel=Button(btn_frame,text="Delete",font=("times new roman",15,'bold'),bg="#050a30",fg="white",command=delete_data,bd=0)
    btndel.grid(row=0,column=3,padx=15)

    #--------------table frame--------------
    ltable=LabelFrame(root,bd=1,relief=RIDGE,text="View Details and Search",font=("times new roman",18,'bold'),padx=2,bg="#fbf5e9")
    ltable.place(x=490,y=150,width=860,height=420)

    lsearch=Label(ltable,text="Search By:",font=("times new roman",14,'bold'),bg="#fbf5e9")
    lsearch.grid(row=0,column=0,sticky=W)

    search_var=StringVar()
    combo_search=ttk.Combobox(ltable,textvariable=search_var,font=("times new roman",12,'bold'),width=22,state="readonly")
    combo_search["value"]=("Mobile","Refer No")
    combo_search.current()
    combo_search.grid(row=0,column=1,padx=4)

    txt_search=StringVar()
    txtsearch=ttk.Entry(ltable,textvariable=txt_search,width=20,font=("times new roman",13,'bold'))
    txtsearch.grid(row=0,column=2,padx=4)


    btnsearch=Button(ltable,text="Search",font=("times new roman",13,'bold'),bg="#050a30",fg="white",command=search,bd=0)
    btnsearch.grid(row=0,column=3,padx=9)

    btnreshowall=Button(ltable,text="Show all",font=("times new roman",13,'bold'),bg="#050a30",fg="white",command=fetch_data,bd=0)
    btnreshowall.grid(row=0,column=4,padx=6)

    #-----------show data table---------------------
    details_table=Frame(ltable,bd=2,relief=RIDGE)
    details_table.place(x=0,y=50,width=800,height=340)

    scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
    scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

    cust_details_table=ttk.Treeview(details_table,column=("Ref","Name","Age","Gender","mobile no","email","nationality","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_y.pack(side=RIGHT,fill=Y)

    scroll_x.config(command=cust_details_table.xview)
    scroll_y.config(command=cust_details_table.yview)

    cust_details_table.heading("Ref",text="Refer no")
    cust_details_table.heading("Name",text="Name")
    cust_details_table.heading("Age",text="Age")
    cust_details_table.heading("Gender",text="Gender")
    cust_details_table.heading("mobile no",text="mobile no")
    cust_details_table.heading("email",text="email")
    cust_details_table.heading("nationality",text="nationality")
    cust_details_table.heading("address",text="address")

    cust_details_table["show"]="headings"
    cust_details_table.column("Ref",width=100)
    cust_details_table.column("Name",width=100)
    cust_details_table.column("Age",width=100)
    cust_details_table.column("Gender",width=100)
    cust_details_table.column("mobile no",width=100)
    cust_details_table.column("email",width=100)
    cust_details_table.column("nationality",width=100)
    cust_details_table.column("address",width=100)

    cust_details_table.pack(fill=BOTH,expand=1)
    cust_details_table.bind("<ButtonRelease-1>",get_cursor)
    fetch_data()



















    root.mainloop()

    

def services_page():
    ser=Toplevel()
    ser.title("Services")
    ser.geometry("1366x768+0+0")
    my_img=PhotoImage(file="C:\\Users\\Krupa\\Downloads\\minimages\\ser.png")
    k=Label(ser,image=my_img).pack()

    book=PhotoImage(file="C:\\Users\\Krupa\\Downloads\\minimages\\book.png")
    b1=Button(ser,image=book,bd=0,bg="#482308",activebackground="#482308",cursor="hand2",command=addcustomer).place(x=220,y=390)

    checko=PhotoImage(file="C:\\Users\\Krupa\\Downloads\\minimages\\co.png")
    b2=Button(ser,image=checko,bd=0,bg="#482308",activebackground="#482308",cursor="hand2",command=checkout).place(x=40,y=495)


    feed=PhotoImage(file="C:\\Users\\Krupa\\Downloads\\minimages\\feed.png")
    b3=Button(ser,image=feed,bd=0,bg="#482308",activebackground="#482308",cursor="hand2",command=feedback).place(x=210,y=610)


    add=PhotoImage(file="C:\\Users\\Krupa\\Downloads\\minimages\\add.png")
    b4=Button(ser,image=add,bd=0,bg="#482308",activebackground="#482308",cursor="hand2",command=admin_add).place(x=590,y=390)


    check=PhotoImage(file="C:\\Users\\Krupa\\Downloads\\minimages\\check.png")
    b5=Button(ser,image=check,bd=0,bg="#482308",activebackground="#482308",cursor="hand2",command=admin_checking).place(x=490,y=510)
    ser.mainloop()

def aboutus_page():
    ab=Toplevel()
    ab.title("About us")
    ab.geometry("1366x760")

    m_img=PhotoImage(file="C:\\Users\\Krupa\\Downloads\\minimages\\about.png")
    k=Label(ab,image=m_img).pack()
    ab.mainloop()
def contactus_page():
    cn=Toplevel()
    cn.title("About us")
    cn.geometry("1366x760")

    m_img=PhotoImage(file="C:\\Users\\Krupa\\Downloads\\minimages\\contact.png")
    k=Label(cn,image=m_img).pack()
    cn.mainloop()


def home():
    root=Toplevel()
    root.title("Home page")
    root.geometry("1366x760")

    def logoutpage():
        res=messagebox.askokcancel("Confirmation","Are you sure you want to logout?",parent=root)
        if res==1:
            #root.destroy()
            roo=Toplevel()
            roo.title("Hotel Management System Using Python")
            roo.geometry('1370x760')
            my_img=ImageTk.PhotoImage(Image.open("C:\\Users\\Krupa\\Downloads\\minimages\\main.png"))
            my_l=Label(roo,image=my_img)
            my_l.pack()


                        
            signup=PhotoImage(file="C:\\Users\\Krupa\\Downloads\\minimages\\admin.png")
            eyebutto=Button(roo,image=signup,bd=0,bg="white",activebackground="white",cursor="hand2",command=admin_page)
            eyebutto.place(x=30,y=485)



            signin=PhotoImage(file="C:\\Users\\Krupa\\Downloads\\minimages\\user.png")
            eyebutto=Button(roo,image=signin,bd=0,bg="white",activebackground="white",cursor="hand2",command=signin_page)
            eyebutto.place(x=335,y=495)






            roo.mainloop()


    my_img=PhotoImage(file="C:\\Users\\Krupa\\Downloads\\minimages\\homefinal.png")
    k=Label(root,image=my_img).pack()

    home=PhotoImage(file="C:\\Users\\Krupa\\Downloads\\minimages\\HOMEC.png")
    b1=Button(root,image=home,bd=0,bg="white",activebackground="white",cursor="hand2",command=home).place(x=500,y=31)

    services=PhotoImage(file="C:\\Users\\Krupa\\Downloads\\minimages\\SERVICESC.png")
    b2=Button(root,image=services,bd=0,bg="white",activebackground="white",cursor="hand2",command=services_page).place(x=645,y=27)

    aboutus=PhotoImage(file="C:\\Users\\Krupa\\Downloads\\minimages\\ABOUTUSC.png")
    b3=Button(root,image=aboutus,bd=0,bg="white",activebackground="white",cursor="hand2",command=aboutus_page).place(x=810,y=15)

    logout=PhotoImage(file="C:\\Users\\Krupa\\Downloads\\minimages\\LOGOUTC.png")
    b4=Button(root,image=logout,bd=0,bg="white",activebackground="white",cursor="hand2",command=logoutpage).place(x=1180,y=23)


    contactus=PhotoImage(file="C:\\Users\\Krupa\\Downloads\\minimages\\CONTACTUSC.png")
    b5=Button(root,image=contactus,bd=0,bg="white",activebackground="white",cursor="hand2",command=contactus_page).place(x=1000,y=28)

    root.mainloop()

def forgot_adminpage():
    forg=Toplevel()
    forg.title("Forgot Page")
    forg.geometry("1370x760")
    forg.configure(bg='#fff')
    bgimg=PhotoImage(file="C:\\Users\\Krupa\\Downloads\\minimages\\ho17.png")
    Label(forg,image=bgimg,border=0,bg="white",activebackground="white").place(x=50,y=150)

    frame=Frame(forg,width=500,height=500,bg='#fff')
    frame.place(x=800,y=200)

    heading=Label(frame,text="Reset Password",fg="#57a1f8",bg="white",font=('Microsoft Yahei UI Light',23,"bold"))
    heading.place(x=65,y=5)

    def login_page():
        if user.get()=='' or code.get()=='' or cu.get=='':
            messagebox.showerror("Error","All fields are required",parent=forg)
        elif code.get()!=cu.get():
            messagebox.showerror("Error","New password and confirm password are not matching",parent=forg)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="binny219")
                mycursor=con.cursor()
            except:
                messagebox.showerror("Error","Connection is not established try again",parent=forg)
                return
            query="use userdata"
            mycursor.execute(query)
            query="select * from admindata where username=%s"
            mycursor.execute(query,(user.get()))
            row=mycursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid username",parent=forg)
            else:
                query="update admindata set password=%s where username=%s"
                mycursor.execute(query,(code.get(),user.get()))
                con.commit()
                con.close()
                messagebox.showinfo("Success","Password is reset,please login with new password",parent=forg)
                forg.destroy()
                admin_page()

    def hide():
        openeye.config(file="C:\\Users\\Krupa\\Downloads\\minimages\\eye2.png")
        u.config(show="*")
        eyebutton.config(command=show)
    def show():
        openeye.config(file="C:\\Users\\Krupa\\Downloads\\minimages\\e1.png")
        u.config(show='')
        eyebutton.config(command=hide)


    def hid():
        openey.config(file="C:\\Users\\Krupa\\Downloads\\minimages\\eye2.png")
        cu.config(show="*")
        eyebutto.config(command=sho)
    def sho():
        openey.config(file="C:\\Users\\Krupa\\Downloads\\minimages\\e1.png")
        cu.config(show='')
        eyebutto.config(command=hid)

    # user 
    def on_enter(e):
        user.delete(0,'end')
    def on_leave(e):
        name=user.get()
        if name=='':
            user.insert(0,'Username')
    user=Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11))
    user.place(x=30,y=80)
    user.insert(0,'Username')
    user.bind('<FocusIn>',on_enter)
    user.bind('<FocusOut>',on_leave)
    Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)
    # 
    def on_enter(e):
        code.delete(0,'end')
    def on_leave(e):
        name=code.get()
        if name=='':
            code.insert(0,'New Password')
    code=Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11))
    code.place(x=30,y=150)
    code.insert(0,'New Password')
    code.bind('<FocusIn>',on_enter)
    code.bind('<FocusOut>',on_leave)
    openeye=PhotoImage(file="C:\\Users\\Krupa\\Downloads\\minimages\\e1.png")
    eyebutton=Button(forg,image=openeye,bd=0,bg="white",activebackground="white",cursor="hand2",command=hide)
    eyebutton.place(x=1090,y=350)


    Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)
    #
    def on_enter(e):
        cu.delete(0,'end')
    def on_leave(e):
        if cu.get()=='':
            cu.insert(0,"Confirm Password")
    cu=Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11))
    cu.place(x=30,y=220)
    cu.insert(0,"Confirm Password")
    cu.bind("<FocusIn>",on_enter)
    #cu.bind("<FocusOut>",on_leave)

    Frame(frame,width=295,height=2,bg='black').place(x=25,y=247)
    openey=PhotoImage(file="C:\\Users\\Krupa\\Downloads\\minimages\\e1.png")
    eyebutto=Button(forg,image=openey,bd=0,bg="white",activebackground="white",cursor="hand2",command=hid)
    eyebutto.place(x=1090,y=420)

    Button(frame,width=40,pady=7,text='Submit',bg='#57a1f8',fg='white',border=0,command=login_page).place(x=35,y=320)


    forg.mainloop()

def forgot_page():
    forg=Toplevel()
    forg.title("Forgot Page")
    forg.geometry("1370x760")
    forg.configure(bg='#fff')
    bgimg=PhotoImage(file="C:\\Users\\Krupa\\Downloads\\minimages\\ho17.png")
    Label(forg,image=bgimg,border=0,bg="white",activebackground="white").place(x=50,y=150)

    frame=Frame(forg,width=500,height=500,bg='#fff')
    frame.place(x=800,y=200)

    heading=Label(frame,text="Reset Password",fg="#57a1f8",bg="white",font=('Microsoft Yahei UI Light',23,"bold"))
    heading.place(x=65,y=5)

    def login_page():
        if user.get()=='' or code.get()=='' or cu.get()=='':
            messagebox.showerror("Error","All fields are required",parent=forg)
        elif code.get()!=cu.get():
            messagebox.showerror("Error","New password and confirm password are not matching",parent=forg)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="binny219")
                mycursor=con.cursor()
            except:
                messagebox.showerror("Error","Connection is not established try again",parent=forg)
                return
            query="use userdata"
            mycursor.execute(query)
            query="select * from data where username=%s"
            mycursor.execute(query,(user.get()))
            row=mycursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid username",parent=forg)
            else:
                query="update data set password=%s where username=%s"
                mycursor.execute(query,(code.get(),user.get()))
                con.commit()
                con.close()
                messagebox.showinfo("Success","Password is reset,please login with new password",parent=forg)
                forg.destroy()
                signin_page()

    def hide():
        openeye.config(file="C:\\Users\\Krupa\\Downloads\\minimages\\eye2.png")
        u.config(show="*")
        eyebutton.config(command=show)
    def show():
        openeye.config(file="C:\\Users\\Krupa\\Downloads\\minimages\\e1.png")
        u.config(show='')
        eyebutton.config(command=hide)


    def hid():
        openey.config(file="C:\\Users\\Krupa\\Downloads\\minimages\\eye2.png")
        cu.config(show="*")
        eyebutto.config(command=sho)
    def sho():
        openey.config(file="C:\\Users\\Krupa\\Downloads\\minimages\\e1.png")
        cu.config(show='')
        eyebutto.config(command=hid)

    # user 
    def on_enter(e):
        user.delete(0,'end')
    def on_leave(e):
        name=user.get()
        if name=='':
            user.insert(0,'Username')
    user=Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11))
    user.place(x=30,y=80)
    user.insert(0,'Username')
    user.bind('<FocusIn>',on_enter)
    user.bind('<FocusOut>',on_leave)
    Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)
    # 
    def on_enter(e):
        code.delete(0,'end')
    def on_leave(e):
        name=code.get()
        if name=='':
            code.insert(0,'New Password')
    code=Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11))
    code.place(x=30,y=150)
    code.insert(0,'New Password')
    code.bind('<FocusIn>',on_enter)
    code.bind('<FocusOut>',on_leave)
    openeye=PhotoImage(file="C:\\Users\\Krupa\\Downloads\\minimages\\e1.png")
    eyebutton=Button(forg,image=openeye,bd=0,bg="white",activebackground="white",cursor="hand2",command=hide)
    eyebutton.place(x=1090,y=350)


    Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)
    #
    def on_enter(e):
        cu.delete(0,'end')
    def on_leave(e):
        if cu.get()=='':
            cu.insert(0,"Confirm Password")
    cu=Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11))
    cu.place(x=30,y=220)
    cu.insert(0,"Confirm Password")
    cu.bind("<FocusIn>",on_enter)
    #cu.bind("<FocusOut>",on_leave)

    Frame(frame,width=295,height=2,bg='black').place(x=25,y=247)
    openey=PhotoImage(file="C:\\Users\\Krupa\\Downloads\\minimages\\e1.png")
    eyebutto=Button(forg,image=openey,bd=0,bg="white",activebackground="white",cursor="hand2",command=hid)
    eyebutto.place(x=1090,y=420)

    Button(frame,width=40,pady=7,text='Submit',bg='#57a1f8',fg='white',border=0,command=login_page).place(x=35,y=320)


    forg.mainloop()


def signup_page():
    window=Toplevel()
    window.title("Sign up")
    window.geometry('1370x760')
    window.configure(bg="#fff")
    #window.resizable(False,False)

    def hide():
        openeye.config(file="C:\\Users\\Krupa\\Downloads\\minimages\\eye2.png")
        u.config(show="*")
        eyebutton.config(command=show)
    def show():
        openeye.config(file="C:\\Users\\Krupa\\Downloads\\minimages\\e1.png")
        u.config(show='')
        eyebutton.config(command=hide)

    def hid():
        openey.config(file="C:\\Users\\Krupa\\Downloads\\minimages\\eye2.png")
        cu.config(show="*")
        eyebutto.config(command=sho)
    def sho():
        openey.config(file="C:\\Users\\Krupa\\Downloads\\minimages\\e1.png")
        cu.config(show='')
        eyebutto.config(command=hid)
        
        

    def clear():
        user.delete(0,END)
        u.delete(0,END)
        cu.delete(0,END)


    def connect_database():
        if user.get()=='' or u.get()=='' or cu.get=='':
            messagebox.showerror("Error","All fields are required",parent=window)
        elif u.get()!=cu.get():
            messagebox.showerror("Error","Password Mismatch",parent=window)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="binny219")
                my_cur=con.cursor()
            except:
                messagebox.showerror("Error","Database connectivity issue,Please Try again",parent=window)
                return
            try:
                query='create database userdata'
                my_cur.execute(query)
                query="use userdata"
                my_cur.execute(query)
                query="create table data(username varchar(100),password varchar(20),confirmpass varchar(20))"
                my_cur.execute(query)
            except:
                my_cur.execute("use userdata")
            query="select * from data where username=%s"
            my_cur.execute(query,(user.get()))
            row=my_cur.fetchone()
            if row!=None:
                messagebox.showerror("Error","Username already exists",parent=window)
            else:   
                query="insert into data values(%s,%s,%s)"
                my_cur.execute(query,(user.get(),u.get(),cu.get()))
                con.commit()
                con.close()
                messagebox.showinfo("Success","Registration is successful",parent=window)
                signin_page()
            
      

    ########--------------------------------------------------------------

    img=ImageTk.PhotoImage(Image.open("C:\\Users\\Krupa\\Downloads\\minimages\\ho1.jpg"))
    Label(window,image=img,border=0,bg="white").place(x=50,y=150)

    frame=Frame(window,width=500,height=500,bg='#fff')
    frame.place(x=850,y=200)

    heading=Label(frame,text="Sign up",fg="#57a1f8",bg="white",font=('Microsoft Yahei UI Light',23,"bold"))
    heading.place(x=100,y=5)
    ####--------------------------------------------
    def on_enter(e):
        user.delete(0,'end')
    def on_leave(e):
        if user.get()=='':
            user.insert(0,"Username")
    user=Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11))
    user.place(x=30,y=80)
    user.insert(0,"Username")
    user.bind("<FocusIn>",on_enter)
    #user.bind("<FocusOut>",on_leave)

    Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)
    ##---------------------------------------------------

    def on_enter(e):
        u.delete(0,'end')
    def on_leave(e):
        if u.get()=='':
            u.insert(0,"Password")
    u=Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11))
    u.place(x=30,y=150)
    u.insert(0,"Password")
    u.bind("<FocusIn>",on_enter)
    #u.bind("<FocusOut>",on_leave)

    Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)
    openeye=PhotoImage(file="C:\\Users\\Krupa\\Downloads\\minimages\\e1.png")
    eyebutton=Button(window,image=openeye,bd=0,bg="white",activebackground="white",cursor="hand2",command=hide)
    eyebutton.place(x=1130,y=350)

    ###------------------------------------------------------
    def on_enter(e):
        cu.delete(0,'end')
    def on_leave(e):
        if cu.get()=='':
            cu.insert(0,"Confirm Password")
    cu=Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11))
    cu.place(x=30,y=220)
    cu.insert(0,"Confirm Password")
    cu.bind("<FocusIn>",on_enter)
    #cu.bind("<FocusOut>",on_leave)

    Frame(frame,width=295,height=2,bg='black').place(x=25,y=247)
    openey=PhotoImage(file="C:\\Users\\Krupa\\Downloads\\minimages\\e1.png")
    eyebutto=Button(window,image=openey,bd=0,bg="white",activebackground="white",cursor="hand2",command=hid)
    eyebutto.place(x=1130,y=420)


    ##------------------------------------------------
    Button(frame,width=39,pady=7,text="Sign Up",bg="#57a1f8",fg="white",border=0,command=connect_database).place(x=35,y=280)
    label=Label(frame,text="I have an account",fg="black",bg="white",font=('Microsoft Yahei UI Light',9))
    label.place(x=90,y=340)

    signin=Button(frame,width=6,text="Sign in",border=0,bg="white",cursor="hand2",fg="#57a1f8",command=signin_page)
    signin.place(x=200,y=340)


    window.mainloop()

    #root.destroy()
    #import signup
def signin_page():
    root=Toplevel()
    root.title("Login")
    root.configure(bg='#fff')
    root.geometry("1370x760")
    # root.resizable(False,False)

    def signin():
        username=user.get()
        password=code.get()

        if username=='' or password=='':
            messagebox.showerror("Error","All fields are required",parent=root)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="binny219")
                mycursor=con.cursor()
            except:
                messagebox.showerror("Error","Connection is not established try again",parent=root)
                return
            query="use userdata"
            mycursor.execute(query)
            query="select * from data where username=%s and password=%s"
            mycursor.execute(query,(user.get(),code.get()))
            row=mycursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid username or password",parent=root)
            else:
                messagebox.showinfo("Welcome","Login is successful",parent=root)
            #clear()
                home()
            
            

    img=ImageTk.PhotoImage(Image.open("C:\\Users\\Krupa\\Downloads\\minimages\\ho3.jpg"))
    Label(root,image=img,border=0,bg="white").place(x=50,y=80)

    frame=Frame(root,width=500,height=500,bg='#fff')
    frame.place(x=850,y=200)
    heading=Label(frame,text='Sign in',fg='#57a1f8',bg='white',font=('Microsoft Yahei UI Light',23,'bold'))
    heading.place(x=100,y=5)


    def hide():
        openeye.config(file="C:\\Users\\Krupa\\Downloads\\minimages\\eye2.png")
        code.config(show="*")
        eyebutton.config(command=show)
    def show():
        openeye.config(file="C:\\Users\\Krupa\\Downloads\\minimages\\e1.png")
        code.config(show='')
        eyebutton.config(command=hide)

    # user 
    def on_enter(e):
        user.delete(0,'end')
    def on_leave(e):
        name=user.get()
        if name=='':
            user.insert(0,'Username')
    user=Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11))
    user.place(x=30,y=80)
    user.insert(0,'Username')
    user.bind('<FocusIn>',on_enter)
    #user.bind('<FocusOut>',on_leave)
    Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)
    # 
    def on_enter(e):
        code.delete(0,'end')
    def on_leave(e):
        name=code.get()
        if name=='':
            code.insert(0,'Password')
    code=Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11))
    code.place(x=30,y=150)
    code.insert(0,'Password')
    code.bind('<FocusIn>',on_enter)
    #code.bind('<FocusOut>',on_leave)
    openeye=PhotoImage(file="C:\\Users\\Krupa\\Downloads\\minimages\\e1.png")
    eyebutton=Button(root,image=openeye,bd=0,bg="white",activebackground="white",cursor="hand2",command=hide)
    eyebutton.place(x=1130,y=350)
    forgot = Button(frame,width=20,text='Forgot Password?',border=0,bg='white',cursor='hand2',fg='#57a1f8',command=forgot_page)
    forgot.place(x=200,y=185)

    Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)
    #

    Button(frame,width=39,pady=7,text='Sign in',bg='#57a1f8',fg='white',border=0,command=signin).place(x=35,y=220)
    label=Label(frame,text="Don't have an account?",fg='black',bg='white',font=('Microsoft Yahei UI Light',9))
    label.place(x=75,y=270)

    sign_up = Button(frame,width=6,text='Sign-up',border=0,bg='white',cursor='hand2',fg='#57a1f8',command=signup_page)
    sign_up.place(x=215,y=270)


    root.mainloop()
def admin_page():
    root=Toplevel()
    root.title("Admin Login")
    root.configure(bg='#fff')
    root.geometry("1370x760")
    # root.resizable(False,False)

    def signin():
        username=user.get()
        password=code.get()

        if username=='' or password=='':
            messagebox.showerror("Error","All fields are required",parent=root)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="binny219")
                mycursor=con.cursor()
            except:
                messagebox.showerror("Error","Connection is not established try again",parent=root)
                return
            query="use userdata"
            mycursor.execute(query)
            query="select * from admindata where username=%s and password=%s"
            mycursor.execute(query,(user.get(),code.get()))
            row=mycursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Oops!! Seems like you are not an admin\n Try again!!",parent=root)
            else:
                messagebox.showinfo("Welcome","Login is successful",parent=root)
            #clear()
                home()
            
            

    img=ImageTk.PhotoImage(Image.open("C:\\Users\\Krupa\\Downloads\\minimages\\manager.png"))
    Label(root,image=img,border=0,bg="white").place(x=10,y=10)

    frame=Frame(root,width=500,height=500,bg='#fff')
    frame.place(x=850,y=230)
    heading=Label(frame,text='Sign in',fg='#57a1f8',bg='white',font=('Microsoft Yahei UI Light',23,'bold'))
    heading.place(x=100,y=5)


    def hide():
        openeye.config(file="C:\\Users\\Krupa\\Downloads\\minimages\\eye2.png")
        code.config(show="*")
        eyebutton.config(command=show)
    def show():
        openeye.config(file="C:\\Users\\Krupa\\Downloads\\minimages\\e1.png")
        code.config(show='')
        eyebutton.config(command=hide)

    # user 
    def on_enter(e):
        user.delete(0,'end')
    def on_leave(e):
        name=user.get()
        if name=='':
            user.insert(0,'Username')
    user=Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11))
    user.place(x=30,y=80)
    user.insert(0,'Username')
    user.bind('<FocusIn>',on_enter)
    #user.bind('<FocusOut>',on_leave)
    Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)
    # 
    def on_enter(e):
        code.delete(0,'end')
    def on_leave(e):
        name=code.get()
        if name=='':
            code.insert(0,'Password')
    code=Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11))
    code.place(x=30,y=150)
    code.insert(0,'Password')
    code.bind('<FocusIn>',on_enter)
    #code.bind('<FocusOut>',on_leave)
    openeye=PhotoImage(file="C:\\Users\\Krupa\\Downloads\\minimages\\e1.png")
    eyebutton=Button(root,image=openeye,bd=0,bg="white",activebackground="white",cursor="hand2",command=hide)
    eyebutton.place(x=1130,y=380)
    forgot = Button(frame,width=20,text='Forgot Password?',border=0,bg='white',cursor='hand2',fg='#57a1f8',command=forgot_adminpage)
    forgot.place(x=200,y=185)

    Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)
    #

    Button(frame,width=39,pady=7,text='Sign in',bg='#57a1f8',fg='white',border=0,command=signin).place(x=35,y=220)
    


    root.mainloop()

    #root.destroy()
    #import tk_login
def admin_add():
    root=Toplevel()
    root.title("Admin Login")
    root.configure(bg='#fff')
    root.geometry("1370x760")
    # root.resizable(False,False)

    def signin():
        username=user.get()
        password=code.get()

        if username=='' or password=='':
            messagebox.showerror("Error","All fields are required",parent=root)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="binny219")
                mycursor=con.cursor()
            except:
                messagebox.showerror("Error","Connection is not established try again",parent=root)
                return
            query="use userdata"
            mycursor.execute(query)
            query="select * from admindata where username=%s and password=%s"
            mycursor.execute(query,(user.get(),code.get()))
            row=mycursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Oops!! Seems like you are not an admin\n You cannot add rooms!!",parent=root)
            else:
                messagebox.showinfo("Welcome","You're an admin",parent=root)
            #clear()
                addroom()
            
            

    img=ImageTk.PhotoImage(Image.open("C:\\Users\\Krupa\\Downloads\\minimages\\manager.png"))
    Label(root,image=img,border=0,bg="white").place(x=10,y=10)

    frame=Frame(root,width=500,height=500,bg='#fff')
    frame.place(x=850,y=230)
    heading=Label(frame,text='Sign in',fg='#57a1f8',bg='white',font=('Microsoft Yahei UI Light',23,'bold'))
    heading.place(x=100,y=5)


    def hide():
        openeye.config(file="C:\\Users\\Krupa\\Downloads\\minimages\\eye2.png")
        code.config(show="*")
        eyebutton.config(command=show)
    def show():
        openeye.config(file="C:\\Users\\Krupa\\Downloads\\minimages\\e1.png")
        code.config(show='')
        eyebutton.config(command=hide)

    # user 
    def on_enter(e):
        user.delete(0,'end')
    def on_leave(e):
        name=user.get()
        if name=='':
            user.insert(0,'Username')
    user=Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11))
    user.place(x=30,y=80)
    user.insert(0,'Username')
    user.bind('<FocusIn>',on_enter)
    #user.bind('<FocusOut>',on_leave)
    Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)
    # 
    def on_enter(e):
        code.delete(0,'end')
    def on_leave(e):
        name=code.get()
        if name=='':
            code.insert(0,'Password')
    code=Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11))
    code.place(x=30,y=150)
    code.insert(0,'Password')
    code.bind('<FocusIn>',on_enter)
    #code.bind('<FocusOut>',on_leave)
    openeye=PhotoImage(file="C:\\Users\\Krupa\\Downloads\\minimages\\e1.png")
    eyebutton=Button(root,image=openeye,bd=0,bg="white",activebackground="white",cursor="hand2",command=hide)
    eyebutton.place(x=1130,y=380)
    forgot = Button(frame,width=20,text='Forgot Password?',border=0,bg='white',cursor='hand2',fg='#57a1f8',command=forgot_adminpage)
    forgot.place(x=200,y=185)

    Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)
    #

    Button(frame,width=39,pady=7,text='Sign in',bg='#57a1f8',fg='white',border=0,command=signin).place(x=35,y=220)
    


    root.mainloop()
def admin_checking():
    root=Toplevel()
    root.title("Admin Login")
    root.configure(bg='#fff')
    root.geometry("1370x760")
    # root.resizable(False,False)

    def signin():
        username=user.get()
        password=code.get()

        if username=='' or password=='':
            messagebox.showerror("Error","All fields are required",parent=root)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="binny219")
                mycursor=con.cursor()
            except:
                messagebox.showerror("Error","Connection is not established try again",parent=root)
                return
            query="use userdata"
            mycursor.execute(query)
            query="select * from admindata where username=%s and password=%s"
            mycursor.execute(query,(user.get(),code.get()))
            row=mycursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Oops!! Seems like you are not an admin\n You cannot check details!!",parent=root)
            else:
                messagebox.showinfo("Welcome","You're an admin",parent=root)
            #clear()
                checking()
            
            

    img=ImageTk.PhotoImage(Image.open("C:\\Users\\Krupa\\Downloads\\minimages\\manager.png"))
    Label(root,image=img,border=0,bg="white").place(x=10,y=10)

    frame=Frame(root,width=500,height=500,bg='#fff')
    frame.place(x=850,y=230)
    heading=Label(frame,text='Sign in',fg='#57a1f8',bg='white',font=('Microsoft Yahei UI Light',23,'bold'))
    heading.place(x=100,y=5)


    def hide():
        openeye.config(file="C:\\Users\\Krupa\\Downloads\\minimages\\eye2.png")
        code.config(show="*")
        eyebutton.config(command=show)
    def show():
        openeye.config(file="C:\\Users\\Krupa\\Downloads\\minimages\\e1.png")
        code.config(show='')
        eyebutton.config(command=hide)

    # user 
    def on_enter(e):
        user.delete(0,'end')
    def on_leave(e):
        name=user.get()
        if name=='':
            user.insert(0,'Username')
    user=Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11))
    user.place(x=30,y=80)
    user.insert(0,'Username')
    user.bind('<FocusIn>',on_enter)
    #user.bind('<FocusOut>',on_leave)
    Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)
    # 
    def on_enter(e):
        code.delete(0,'end')
    def on_leave(e):
        name=code.get()
        if name=='':
            code.insert(0,'Password')
    code=Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11))
    code.place(x=30,y=150)
    code.insert(0,'Password')
    code.bind('<FocusIn>',on_enter)
    #code.bind('<FocusOut>',on_leave)
    openeye=PhotoImage(file="C:\\Users\\Krupa\\Downloads\\minimages\\e1.png")
    eyebutton=Button(root,image=openeye,bd=0,bg="white",activebackground="white",cursor="hand2",command=hide)
    eyebutton.place(x=1130,y=380)
    forgot = Button(frame,width=20,text='Forgot Password?',border=0,bg='white',cursor='hand2',fg='#57a1f8',command=forgot_adminpage)
    forgot.place(x=200,y=185)

    Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)
    #

    Button(frame,width=39,pady=7,text='Sign in',bg='#57a1f8',fg='white',border=0,command=signin).place(x=35,y=220)
    


    root.mainloop()



signup=PhotoImage(file="C:\\Users\\Krupa\\Downloads\\minimages\\admin.png")
eyebutto=Button(root,image=signup,bd=0,bg="white",activebackground="white",cursor="hand2",command=admin_page)
eyebutto.place(x=30,y=485)



signin=PhotoImage(file="C:\\Users\\Krupa\\Downloads\\minimages\\user.png")
eyebutto=Button(root,image=signin,bd=0,bg="white",activebackground="white",cursor="hand2",command=signin_page)
eyebutto.place(x=335,y=495)






root.mainloop()
