from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import random
from event import EventManagementSystem
from userdetails import userdetails_win
from eventType import EventTypeBooking
from eventt import Eventt
from venue import Venuebooking
from ticket import Ticketbooking
from meal import Mealbooking



def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()

class Login_Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")
        self.root.config(background='#f0eae4')

        # self.bg=ImageTk.PhotoImage(file=r"C:\Users\tusha\PycharmProjects\Login\images\hans-isaacson-Dq6ErkQ_RxE-unsplash")
        #
        # lbl_bg=Label(self.root,image=self.bg)
        # lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame = Frame(self.root, bg="#f0eae4")
        frame.place(x=610, y=170, width=340, height=450)

        get_str = Label(frame, text="LOGIN", font=("verdana", 30, "bold"), fg="#334452", bg="#f0eae4")
        get_str.place(x=100, y=80)

        # label
        username = lbl = Label(frame, text="Username", font=("verdana", 15, "bold"), fg="#334452", bg="#f0eae4")
        username.place(x=40, y=150)

        self.user = ttk.Entry(frame, font=("verdana", 15, "bold"))
        self.user.place(x=40, y=180, width=270)

        password = lbl = Label(frame, text="Password", font=("verdana", 15, "bold"), fg="#334452", bg="#f0eae4")
        password.place(x=40, y=225)

        self.password = ttk.Entry(frame, font=("verdana", 15, "bold"))
        self.password.place(x=40, y=250, width=270)

        # loginButton
        loginBtn=Button(frame,command=self.login,text="Login", font=("verdana", 15, "bold"), bd=3, relief=RIDGE, fg="#334452", bg="white", activeforeground="white", activebackground="red")
        loginBtn.place(x=110, y=300, width=120, height=35)

        # registerButton
        registerBtn=Button(frame, text="Sign-up",command=self.register_window,font=("verdana", 10, "bold"), borderwidth=0, fg="#334452",bg="white", activeforeground="white", activebackground="black")
        registerBtn.place(x=90, y=350, width=160)

        # forgotPasswordButton
        fgPasswordBtn=Button(frame, text="Forgot Password",command=self.forgot_password_window, font=("verdana", 10, "bold"), borderwidth=0,fg="#334452", bg="white", activeforeground="white", activebackground="black")
        fgPasswordBtn.place(x=90, y=370, width=160)

    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)
        self.root.config(background='#f0eae4')

    def login(self):
        #ws=Tk()
        if self.user.get() == "" or self.password.get() == "":
            messagebox.showerror("Incorrect", "All fields are required")
        elif self.user.get() == "abcd" and self.password.get() == "efgh":
            #win.destroy()
            messagebox.showinfo("Success", "Welcome to Event Booking System")
        else:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="heythisistushar@123",
                database="Event-Booking"
            )
            my_cursor = conn.cursor()
            my_cursor.execute("select * from register where Username=%s and Password=%s",(
                                                                                            self.user.get(),
                                                                                            self.password.get()
            ))
            row=my_cursor.fetchall()
            if row!=None:
                messagebox.showerror("Error","Incorrect Username and Password")
            else:
                open_main=messagebox.askyesno("YesNo","Access is only for Admin")
                if open_main>0:
                    self.new_window=Toplevel(self.new_window)
                    self.app=EventManagementSystem(self.new_window)
                    #part2 38:35 to 43:00, we should copy the code from hotel mgmt system and paste here
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()

    #reset password
    def reset_pass(self):
        if self.SecretCode_entry.get()=="":
            messagebox.showerror("Error","Please enter the Secret Code",parent=self.root2)
        elif self.txt_newpass.get()=="":
            messagebox.showerror("Error","Please enter the new password",parent=self.root2)
        else:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="heythisistushar@123",
                database="Event-Booking"
            )
            my_cursor=conn.connect()
            qury=("select * from register where Username=%s and SecretCode=%s")
            vlaue=(self.user.get(),self.SecretCode_entry.get())
            my_cursor.execute(qury,vlaue)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter the correct secret code")
            else:
                query=("update register set Password=%s where Username=%s")
                value=(self.txt_newpass.get(),self.user.get())
                my_cursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your password has been reset",paretn=self.root2)
                self.root2.destroy()



    #forgot password
    def forgot_password_window(self):
        if self.user.get()=="":
            messagebox.showerror("Error","Please enter the username to reset the password")
        else:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="heythisistushar@123",
                database="Event-Booking"
            )
            my_cursor = conn.cursor()
            query= ("select * from register where Username=%s")
            value=(self.user.get())
            my_cursor.execute(query,(value,))
            row=my_cursor.fetchone()
            #print(row)

            if row==None:
                messagebox.showerror("Error","Please enter the valid username")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("340x450+610+170")

                l=Label(self.root2,text="Reset Password",font=("verdana", 25, "bold"), fg="#334452")
                l.place(x=0,y=16,relwidth=1)

                SecretCode = Label(self.root2, text="Enter secret code", font=("verdana", 17, "bold"), bg="#f0eae4",fg="#334452")
                SecretCode.place(x=40, y=130)

                self.SecretCode_entry = ttk.Entry(self.root2, font=("verdana", 20, "bold"))
                self.SecretCode_entry.place(x=50, y=180, width=257)

                new_password = Label(self.root2, text="Enter new password", font=("verdana", 17, "bold"), bg="#f0eae4",fg="#334452")
                new_password.place(x=40, y=230)

                self.txt_newpass = ttk.Entry(self.root2, font=("verdana", 20, "bold"))
                self.txt_newpass.place(x=50, y=280, width=257)

                btn=Button(self.root2,text="Reset",font=("verdana",15,"bold"),bg="#f0eae4",fg="#334452")
                btn.place(x=130,y=350)


class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Sign-Up")
        self.root.geometry("1600x900+0+0")
        self.root.config(background='#f0eae4')

        #variables
        self.var_name = StringVar()
        self.var_phone = StringVar()
        self.var_age = StringVar()
        self.var_username = StringVar()
        self.var_password = StringVar()
        self.var_secretCode = StringVar()

        #main frame
        frame=Frame(self.root,bg='#f0eae4')
        frame.place(x=360,y=110,width=800,height=550)

        register_lbl=Label(frame,text="Enter new user details",font=("verdana",30,"bold"),bg="#f0eae4",fg="#334452")
        register_lbl.place(x=160,y=50)

        #label and entry field
        name=Label(frame,text="Name",font=("verdana",20,"bold"),bg="#f0eae4",fg="#334452")
        name.place(x=100,y=120)

        self.name_entry=ttk.Entry(frame,textvariable=self.var_name,font=("verdana",20,"bold"))
        self.name_entry.place(x=500,y=120,width=250)

        phone = Label(frame, text="Phone", font=("verdana", 20, "bold"),bg="#f0eae4",fg="#334452")
        phone.place(x=100, y=170)

        self.phone_entry = ttk.Entry(frame,textvariable=self.var_phone,font=("verdana", 20, "bold"))
        self.phone_entry.place(x=500, y=170, width=250)

        age = Label(frame, text="Age", font=("verdana", 20, "bold"),bg="#f0eae4",fg="#334452")
        age.place(x=100, y=220)

        self.age_entry = ttk.Entry(frame,textvariable=self.var_age,font=("verdana", 20, "bold"))
        self.age_entry.place(x=500, y=220, width=250)

        Username = Label(frame, text="Username", font=("verdana", 20, "bold"),bg="#f0eae4",fg="#334452")
        Username.place(x=100, y=270)

        self.Username_entry = ttk.Entry(frame,textvariable=self.var_username,font=("verdana", 20, "bold"))
        self.Username_entry.place(x=500, y=270, width=250)

        Password = Label(frame, text="Password", font=("verdana", 20, "bold"),bg="#f0eae4",fg="#334452")
        Password.place(x=100, y=320)

        self.Password_entry = ttk.Entry(frame,textvariable=self.var_password,font=("verdana", 20, "bold"))
        self.Password_entry.place(x=500, y=320, width=250)

        SecretCode = Label(frame, text="Enter secret code", font=("verdana", 20, "bold"),bg="#f0eae4",fg="#334452")
        SecretCode.place(x=100, y=370)

        self.SecretCode_entry = ttk.Entry(frame,textvariable=self.var_secretCode,font=("verdana", 20, "bold"))
        self.SecretCode_entry.place(x=500, y=370, width=250)

        #confirm button
        btn=Button(frame,command=self.register_data,text="Confirm",font=("verdana",15,"bold"),borderwidth=5,fg="#334452", bg="white", activeforeground="white", activebackground="black")
        btn.place(x=100,y=460)

        #login button
        btn = Button(frame, text="Login Now", font=("verdana", 15, "bold"), borderwidth=5, fg="#334452", bg="white",activeforeground="white", activebackground="black")
        btn.place(x=220, y=460)

        #function declaration
    def register_data(self):
        if self.var_name.get() == "" or self.var_phone.get() == "" or self.var_age.get() == "" or self.var_username.get() == "" or self.var_password.get() == "" or self.var_secretCode.get() == "":
            messagebox.showerror("Error","Enter all fields")
        else:
            #messagebox.showinfo("Success","It has been registered")
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="heythisistushar@123",
                database="Event-Booking"
            )
            my_cursor = conn.cursor()
            query = ("select * from register where Username=%s")
            value = (self.var_username.get())
            my_cursor.execute(query,(value,))
            row = my_cursor.fetchone()
            if row != None:
                messagebox.showerror("Error","Username already exists,please try with another Username")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s)",(
                                                                                    self.var_name.get(),
                                                                                    self.var_phone.get(),
                                                                                    self.var_age.get(),
                                                                                    self.var_username.get(),
                                                                                    self.var_password.get(),
                                                                                    self.var_secretCode.get(),

                ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Registered Successfully")









class EventManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Event Management System")
        self.root.geometry("1550x800+0+0")
        self.root.config(background='#f0eae4')


        #title
        lbl_title=Label(self.root,text="TECHNICAL EVENT MANAGEMENT SYSTEM",font=("verdana",30,"bold"),bg="#f0eae4",fg="#334452",bd=4)
        lbl_title.place(x=0,y=140,width=1550,height=50)

        #main frame
        #main_frame=Frame(self.root,bd=4,relief=RIDGE)
        #main_frame.place(x=330,y=270,width=890,height=420)

        #menu
        #lbl_menu = Label(main_frame, text="MENU", font=("times new roman", 20, "bold"),bg="white", fg="black", bd=4)
        #lbl_menu.place(x=0, y=0, width=230)

        #button
        #btn_frame = Frame(self.root, bd=4, relief=RIDGE)
        #btn_frame.place(x=20, y=270, width=228, height=70)

        user_details=Button(self.root,text="USER DETAILS",command=self.user_details,width=17,font=("verdana",20,"bold"),bg="white",fg="#334452",bd=0,cursor="hand1")
        user_details.place(x=20,y=270,width=306,height=50)

        event_type = Button(self.root, text="EVENT TYPE",command=self.eventTypeBooking,width=17, font=("verdana", 20, "bold"),bg="white", fg="#334452", bd=0, cursor="hand1")
        event_type.place(x=20, y=330, width=306,height=50)

        event = Button(self.root, text="EVENT",command=self.eventBooking,width=17, font=("verdana", 20, "bold"),bg="white", fg="#334452", bd=0, cursor="hand1")
        event.place(x=20, y=390, width=306, height=50)

        venue = Button(self.root, text="VENUE", width=17,command=self.venueBooking,font=("verdana", 20, "bold"),  bg="white", fg="#334452", bd=0, cursor="hand1")
        venue.place(x=20, y=450, width=306, height=50)

        tickets = Button(self.root, text="TICKETS",command=self.ticketBooking,width=17, font=("verdana", 20, "bold"), bg="white", fg="#334452", bd=0, cursor="hand1")
        tickets.place(x=20, y=510, width=306, height=50)

        mealsBeverages = Button(self.root, text="MEALS/BEVERAGES",command=self.mealBooking,width=17, font=("verdana", 20, "bold"), bg="white", fg="#334452", bd=0, cursor="hand1")
        mealsBeverages.place(x=20, y=570, width=306, height=50)

        logout = Button(self.root, text="LOGOUT",command=self.logout,width=17, font=("verdana", 17, "bold"),  bg="white", fg="#334452", bd=0, cursor="hand1")
        logout.place(x=20, y=630, width=306, height=50)


    def user_details(self):
        self.new_window=Toplevel(self.root)
        self.app=userdetails_win(self.new_window)

    def eventTypeBooking(self):
        self.new_window=Toplevel(self.root)
        self.app=EventTypeBooking(self.new_window)

    def eventBooking(self):
        self.new_window = Toplevel(self.root)
        self.app = Eventt(self.new_window)

    def venueBooking(self):
        self.new_window=Toplevel(self.root)
        self.app = Venuebooking(self.new_window)

    def ticketBooking(self):
        self.new_window=Toplevel(self.root)
        self.app = Ticketbooking(self.new_window)

    def mealBooking(self):
        self.new_window=Toplevel(self.root)
        self.app = Mealbooking(self.new_window)

    def logout(self):
        self.root.destroy()


class userdetails_win:
    def __init__(self,root):
        self.root=root
        self.root.title("")
        self.root.geometry("888x382+350+298")
        self.root.config(background='#f0eae4')

        #variables
        self.var_name = StringVar()
        self.var_phone_number = StringVar()
        self.var_address = StringVar()
        self.var_dob = StringVar()
        self.var_username = StringVar()


        #title
        lbl_title = Label(self.root, text="ADD USER DETAILS", font=("verdana", 20, "bold"),bg="#f0eae4", fg="#334452", bd=0)
        lbl_title.place(x=300,y=0, width=300, height=35)

        #label frame
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="User Details",font=("verdana", 20, "bold"),bg="#f0eae4",fg="#334452",padx=2)
        labelframeleft.place(x=0,y=38,width=450,height=342)

        #labels and entries
        #name
        lbl_name_ref=Label(labelframeleft,text="Name",font=("verdana", 17, "bold"),bg="#f0eae4",fg="#334452",padx=2,pady=6)
        lbl_name_ref.grid(row=0,column=0,sticky=W)

        entry_name=ttk.Entry(labelframeleft,textvariable=self.var_name,width=24,font=("verdana", 17, "bold"))
        entry_name.grid(row=0,column=1)

        #phone number
        lbl_phone_ref = Label(labelframeleft, text="Phone Number", font=("verdana", 17, "bold"),bg="#f0eae4",fg="#334452", padx=2, pady=6)
        lbl_phone_ref.grid(row=1, column=0, sticky=W)

        entry_phone = ttk.Entry(labelframeleft,textvariable=self.var_phone_number, width=24, font=("verdana", 17, "bold"))
        entry_phone.grid(row=1, column=1)

        #address
        lbl_address_ref = Label(labelframeleft, text="Address", font=("verdana", 17, "bold"),bg="#f0eae4",fg="#334452", padx=2, pady=6)
        lbl_address_ref.grid(row=2, column=0, sticky=W)

        entry_address = ttk.Entry(labelframeleft,textvariable=self.var_address,width=24, font=("verdana", 17, "bold"))
        entry_address.grid(row=2, column=1)

        #date of birth
        lbl_dob_ref = Label(labelframeleft, text="Date of Birth", font=("verdana", 17, "bold"),bg="#f0eae4",fg="#334452", padx=2, pady=6)
        lbl_dob_ref.grid(row=3, column=0, sticky=W)

        entry_dob = ttk.Entry(labelframeleft,textvariable=self.var_dob,width=24, font=("verdana", 17, "bold"))
        entry_dob.grid(row=3, column=1)

        #username
        lbl_username_ref = Label(labelframeleft, text="Username", font=("verdana", 17, "bold"),bg="#f0eae4",fg="#334452", padx=2, pady=6)
        lbl_username_ref.grid(row=4, column=0, sticky=W)

        entry_username = ttk.Entry(labelframeleft,textvariable=self.var_username,width=24, font=("verdana", 17, "bold"))
        entry_username.grid(row=4, column=1)

        #buttons
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=2,y=250,width=435,height=40)

        btnCreate=Button(btn_frame,text="Create",command=self.add_data,font=("verdana", 13, "bold"),bg="white",fg="#334452",width=8)
        btnCreate.grid(row=0,column=0,padx=1)

        btnUpdate = Button(btn_frame, text="Update",command=self.update,font=("verdana", 13, "bold"), bg="white", fg="#334452", width=8)
        btnUpdate.grid(row=0, column=1, padx=1)

        btnDelete = Button(btn_frame, text="Delete",command=self.mdelete, font=("verdana", 13, "bold"), bg="white", fg="#334452", width=8)
        btnDelete.grid(row=0, column=2, padx=1)

        btnReset = Button(btn_frame, text="Reset",command=self.reset, font=("verdana", 13, "bold"), bg="white", fg="#334452",width=8)
        btnReset.grid(row=0, column=3, padx=1)

        #table frame search system
        Table_Frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details",font=("verdana", 20, "bold"),bg="#f0eae4",fg="#334452", padx=2)
        Table_Frame.place(x=453, y=38, width=430, height=342)

        lblSearchBy=Label(Table_Frame,font=("verdana", 15, "bold"),text="Search By",bg="#f0eae4",fg="#334452")
        lblSearchBy.grid(row=0,column=0,sticky=W,padx=7)

        self.search_var=StringVar()
        combo_Search=ttk.Combobox(Table_Frame,textvariable=self.search_var,font=("verdana", 13, "bold"),width=9,state="readonly")
        combo_Search["value"]=("Address","Username")
        combo_Search.current(0)
        combo_Search.grid(row=0,column=1)

        self.entry_Search=StringVar()
        entry_Search = ttk.Entry(Table_Frame,textvariable=self.entry_Search, width=10, font=("verdana", 13, "bold"))
        entry_Search.grid(row=0, column=2)

        #button
        btnSearch = Button(Table_Frame, text="Search",command=self.search, font=("verdana", 13, "bold"), bg="white",fg="#334452",width=11)
        btnSearch.grid(row=1, column=0, padx=1)

        btnShowAll = Button(Table_Frame, text="Show All",command=self.fetch_data, font=("verdana", 13, "bold"), bg="white",fg="#334452",width=11)
        btnShowAll.grid(row=1, column=1, padx=1)

        #show data table
        details_table=Frame(Table_Frame,bd=2,relief=RIDGE)
        details_table.place(x=10,y=90,width=410,height=215)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table, orient=VERTICAL)

        self.User_Details_Table=ttk.Treeview(details_table,column=("name","phone number","address","date of birth","username"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.User_Details_Table.xview)
        scroll_y.config(command=self.User_Details_Table.yview)

        self.User_Details_Table.heading("name",text="Name")
        self.User_Details_Table.heading("phone number", text="Phone Number")
        self.User_Details_Table.heading("address", text="Address")
        self.User_Details_Table.heading("date of birth", text="Date of Birth")
        self.User_Details_Table.heading("username", text="Username")

        self.User_Details_Table["show"]="headings"

        self.User_Details_Table.column("name",width=100)
        self.User_Details_Table.column("phone number",width=100)
        self.User_Details_Table.column("address",width=100)
        self.User_Details_Table.column("date of birth",width=100)
        self.User_Details_Table.column("username",width=100)

        self.User_Details_Table.pack(fill=BOTH,expand=1)
        self.User_Details_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_phone_number.get()=="" or self.var_username.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="heythisistushar@123",
                    database="Event-Booking"
                )
                my_cursor = conn.cursor()
                my_cursor.execute("insert into user_details values(%s,%s,%s,%s,%s)",(
                                                                                        self.var_name.get(),
                                                                                        self.var_phone_number.get(),
                                                                                        self.var_address.get(),
                                                                                        self.var_dob.get(),
                                                                                        self.var_username.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","User details has been added",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning","Something went wrong:{str(es)}",parent=self.root)

    def fetch_data(self):
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="heythisistushar@123",
            database="Event-Booking"
        )
        my_cursor = conn.cursor()
        my_cursor.execute("select * from user_details")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.User_Details_Table.delete(*self.User_Details_Table.get_children())
            for i in rows:
                self.User_Details_Table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        cursor_row=self.User_Details_Table.focus()
        content=self.User_Details_Table.item(cursor_row)
        row=content["values"]

        self.var_name.set(row[0]),
        self.var_phone_number.set(row[1]),
        self.var_address.set(row[2]),
        self.var_dob.set(row[3]),
        self.var_username.set(row[4]),

    def update(self):
        if self.var_phone_number.get()=="":
            messagebox.showerror("Error","Please enter the phone number",parent=self.root)
        else:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="heythisistushar@123",
                database="Event-Booking"
            )
            my_cursor = conn.cursor()
            my_cursor.execute("update user_details set Name=%s,PhoneNumber=%s,Address=%s,DateofBirth=%s where Username=%s",(
                                                                    self.var_name.get(),
                                                                    self.var_phone_number.get(),
                                                                    self.var_address.get(),
                                                                    self.var_dob.get(),
                                                                    self.var_username.get()
                              ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Updated","User Details has been updated successfully",parent=self.root)



    def mdelete(self):
        mdelete=messagebox.askyesno("Event Management System","Do you want to delete this User",parent=self.root)
        if mdelete>0:
                conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="heythisistushar@123",
                database="Event-Booking"
                )
                my_cursor = conn.cursor()
                query="delete from user_details where Username=%s"
                value=(self.var_username.get(),)
                my_cursor.execute(query,value)
        else:
            if not mdelete:
                return

        conn.commit()
        self.fetch_data()
        conn.close()

    def reset(self):
        self.var_name.set(""),
        self.var_phone_number.set(""),
        self.var_address.set(""),
        self.var_dob.set(""),
        self.var_username.set("")

    def search(self):
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="heythisistushar@123",
            database="Event-Booking"
        )
        my_cursor = conn.cursor()
        my_cursor.execute("select * from user_details where "+str(self.search_var.get())+" LIKE '%"+str(self.entry_Search.get())+"%'")
        row=my_cursor.fetchall()
        if len (row)!=0:
            self.User_Details_Table.delete(*self.User_Details_Table.get_children())
            for i in row:
                self.User_Details_Table.insert("",END,values=i)
            conn.commit()
        conn.close()

#******************************

class EventTypeBooking:
    def __init__(self,root):
        self.root=root
        self.root.title("")
        self.root.geometry("888x382+350+298")
        self.root.config(background='#f0eae4')
        #variables
        self.var_eventTypeId=StringVar()
        x=random.randint(1000,9999)
        self.var_eventTypeId.set(str(x))

        self.var_username=StringVar()
        self.var_eventTypeName=StringVar()
        self.var_phoneNumber=StringVar()

        #title
        lbl_title = Label(self.root, text="SELECT EVENT TYPE", font=("verdana",20, "bold"), bg="#f0eae4",fg="#334452", bd=0)
        lbl_title.place(x=300, y=0, width=300, height=35)

        # label frame
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Event Details", font=("verdana",20, "bold"),bg="#f0eae4",padx=2,fg="#334452")
        labelframeleft.place(x=0, y=38, width=450, height=342)

        #Username
        lbl_Username = Label(labelframeleft, text="Username", font=("verdana",17, "bold"),bg="#f0eae4",padx=2,pady=6,fg="#334452")
        lbl_Username.grid(row=0, column=0, sticky=W)

        entry_Username = ttk.Entry(labelframeleft,textvariable=self.var_username,width=7,font=("verdana", 20, "bold"))
        entry_Username.grid(row=0, column=1,sticky=W)

        #fetch data button
        btnFetchData = Button(labelframeleft,command=self.Fetch_username,text="Fetch", font=("verdana", 14, "bold"), bg="white", fg="#334452", width=5)
        btnFetchData.place(x=374,y=4)

        #EventTypeId
        lbl_EventTypeId = Label(labelframeleft, text="Event Type ID", font=("verdana",17, "bold"),bg="#f0eae4",padx=2,pady=6,fg="#334452")
        lbl_EventTypeId.grid(row=1, column=0, sticky=W)

        entry_EventTypeId = ttk.Entry(labelframeleft,textvariable=self.var_eventTypeId,width=15, font=("verdana", 20, "bold"),state="readonly")
        entry_EventTypeId.grid(row=1, column=1,sticky=W)

        #EventTypeName(combo box)
        lbl_EventTypeName = Label(labelframeleft, font=("verdana",17, "bold"), text="Event Type Name",bg="#f0eae4",fg="#334452")
        lbl_EventTypeName.grid(row=2, column=0, sticky=W)

        combo_EventTypeName = ttk.Combobox(labelframeleft,textvariable=self.var_eventTypeName,font=("verdana",15, "bold"),width=14, state="readonly")
        combo_EventTypeName["value"] = ("Seminars","Webinars","Workshop","Tech Expo")
        combo_EventTypeName.current(0)
        combo_EventTypeName.grid(row=2, column=1,sticky=W)

        #Phone number
        lbl_PhoneNumber = Label(labelframeleft, text="Phone Number", font=("verdana",17, "bold"),bg="#f0eae4",padx=2,pady=6,fg="#334452")
        lbl_PhoneNumber.grid(row=3, column=0, sticky=W)

        entry_PhoneNumber = ttk.Entry(labelframeleft,textvariable=self.var_phoneNumber,width=15, font=("verdana", 20, "bold"))
        entry_PhoneNumber.grid(row=3, column=1,sticky=W)


        #buttons
        btn_frame = Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=2, y=250, width=435, height=40)

        btnCreate = Button(btn_frame, text="Create",command=self.add_data,font=("verdana", 13, "bold"),bg="white", fg="#334452", width=8)
        btnCreate.grid(row=0, column=0, padx=1)

        btnUpdate = Button(btn_frame, text="Update",command=self.update,font=("verdana", 13, "bold"), bg="white", fg="#334452", width=8)
        btnUpdate.grid(row=0, column=1, padx=1)

        btnDelete = Button(btn_frame, text="Delete",command=self.mdelete,font=("verdana", 13, "bold"),bg="white", fg="#334452", width=8)
        btnDelete.grid(row=0, column=2, padx=1)

        btnReset = Button(btn_frame, text="Reset",command=self.reset,font=("verdana", 13, "bold"), bg="white", fg="#334452", width=8)
        btnReset.grid(row=0, column=3, padx=1)

        #table frame search system
        Table_Frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details",font=("verdana", 20, "bold"),bg="#f0eae4",padx=2,fg="#334452")
        Table_Frame.place(x=453, y=150, width=430, height=228)

        # show data table
        details_table = Frame(Table_Frame, bd=2, relief=RIDGE,bg="#f0eae4")
        details_table.place(x=9, y=8, width=410, height=180)

        scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)

        self.eventType_table = ttk.Treeview(details_table,column=("username", "eventTypeId", "eventTypeName", "phoneNumber"), xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.eventType_table.xview)
        scroll_y.config(command=self.eventType_table.yview)

        self.eventType_table.heading("username", text="Username")
        self.eventType_table.heading("eventTypeId", text="Event Type ID")
        self.eventType_table.heading("eventTypeName", text="Event Type Name")
        self.eventType_table.heading("phoneNumber", text="Phone Number")

        self.eventType_table["show"] = "headings"

        self.eventType_table.column("username", width=100)
        self.eventType_table.column("eventTypeId", width=100)
        self.eventType_table.column("eventTypeName", width=100)
        self.eventType_table.column("phoneNumber", width=100)

        self.eventType_table.pack(fill=BOTH, expand=1)
        self.eventType_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()


    def add_data(self):
        if self.var_username.get()=="" or self.var_eventTypeName.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="heythisistushar@123",
                    database="Event-Booking"
                )
                my_cursor = conn.cursor()
                my_cursor.execute("insert into eventtype values(%s,%s,%s,%s)",(
                                                                                self.var_username.get(),
                                                                                self.var_eventTypeId.get(),
                                                                                self.var_eventTypeName.get(),
                                                                                self.var_phoneNumber.get()



                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Event Type Booked",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning","Something went wrong:{str(es)}",parent=self.root)

    def fetch_data(self):
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="heythisistushar@123",
            database="Event-Booking"
        )
        my_cursor = conn.cursor()
        my_cursor.execute("select * from eventtype")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.eventType_table.delete(*self.eventType_table.get_children())
            for i in rows:
                self.eventType_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        cursor_row=self.eventType_table.focus()
        content=self.eventType_table.item(cursor_row)
        row=content["values"]

        self.var_username.set(row[0]),
        self.var_eventTypeId.set(row[1]),
        self.var_eventTypeName.set(row[2]),
        self.var_phoneNumber.set(row[3]),

    def update(self):
        if self.var_username.get()=="":
            messagebox.showerror("Error","Please enter the username",parent=self.root)
        else:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="heythisistushar@123",
                database="Event-Booking"
            )
            my_cursor = conn.cursor()
            my_cursor.execute("update eventtype set EventTypeName=%s,PhoneNumber=%s where EventTypeId=%s",(
                                                                    self.var_eventTypeName.get(),
                                                                    self.var_phoneNumber.get(),
                                                                    self.var_eventTypeId.get()
                              ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Updated","Event Type has been updated successfully",parent=self.root)


    def mdelete(self):
        mdelete=messagebox.askyesno("Event Management System","Do you want to delete this User",parent=self.root)
        if mdelete>0:
                conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="heythisistushar@123",
                database="Event-Booking"
                )
                my_cursor = conn.cursor()
                query="delete from eventtype where EventTypeId=%s"
                value=(self.var_eventTypeId.get(),)
                my_cursor.execute(query,value)
        else:
            if not mdelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    def reset(self):
        self.var_username.set(""),
        #self.var_eventTypeId.set("")
        #self.var_eventTypeName.set(""),
        self.var_phoneNumber.set("")

        x = random.randint(1000, 9999)
        self.var_eventTypeId.set(str(x))


    #All data fetch


    def Fetch_username(self):
        if self.var_username.get()=="":
            messagebox.showerror("Error","Please enter Username",parent=self.root)
        else:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="heythisistushar@123",
                database="Event-Booking"
            )
            my_cursor = conn.cursor()
            query=("select Name from user_details where Username=%s")
            value=(self.var_username.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            if row==None:
                messagebox.showerror("Error","This Username does not exist",parent=self.root)
            else:
                conn.commit()
                conn.close()

                showDataFrame=Frame(self.root,bd=4,relief=RIDGE,padx=2,bg="#f0eae4")
                showDataFrame.place(x=454,y=52,width=425,height=98)

                #name
                lblName=Label(showDataFrame,text="Name:",font=("verdana",11,"bold"),bg="#f0eae4",fg="#334452")
                lblName.place(x=0,y=0)

                lbl=Label(showDataFrame,text=row,font=("verdana",11,"bold"),bg="#f0eae4",fg="#334452")
                lbl.place(x=130,y=0)

                #phone number
                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="heythisistushar@123",
                    database="Event-Booking"
                )
                my_cursor = conn.cursor()
                query = ("select PhoneNumber from user_details where Username=%s")
                value = (self.var_username.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblPhoneNumber = Label(showDataFrame, text="Phone Number:", font=("verdana", 11, "bold"),bg="#f0eae4",fg="#334452")
                lblPhoneNumber.place(x=0, y=20)

                lbl2=Label(showDataFrame, text=row, font=("verdana", 11, "bold"),bg="#f0eae4",fg="#334452")
                lbl2.place(x=130, y=20)

                #address
                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="heythisistushar@123",
                    database="Event-Booking"
                )
                my_cursor = conn.cursor()
                query = ("select Address from user_details where Username=%s")
                value = (self.var_username.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblAddress = Label(showDataFrame, text="Address:", font=("verdana", 11, "bold"),bg="#f0eae4",fg="#334452")
                lblAddress.place(x=0, y=40)

                lbl3 = Label(showDataFrame, text=row, font=("verdana", 11, "bold"),bg="#f0eae4",fg="#334452")
                lbl3.place(x=130, y=40)

                #dateofbirth
                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="heythisistushar@123",
                    database="Event-Booking"
                )
                my_cursor = conn.cursor()
                query = "select DateofBirth from user_details where Username=%s"
                value = (self.var_username.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lbldob = Label(showDataFrame, text="Date of Birth:", font=("verdana", 11, "bold"),bg="#f0eae4",fg="#334452")
                lbldob.place(x=0, y=60)

                lbl4 = Label(showDataFrame, text=row, font=("verdana", 11, "bold"),bg="#f0eae4",fg="#334452")
                lbl4.place(x=130, y=60)


                #********************************

class Eventt:
    def __init__(self,root):
        self.root=root
        self.root.title("")
        self.root.geometry("888x382+350+298")
        self.root.config(background='#f0eae4')

        #variables
        self.var_EventId = StringVar()
        x = random.randint(1000, 9999)
        self.var_EventId.set(str(x))

        self.var_EventName = StringVar()
        self.var_Date = StringVar()
        self.var_Timings = StringVar()
        self.var_EventTypeId = StringVar()

        # title
        lbl_title = Label(self.root, text="SELECT EVENT", font=("verdana", 20, "bold"), bg="#f0eae4", fg="#334452",bd=0)
        lbl_title.place(x=300, y=0, width=300, height=35)

        # label frame
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Event Details", font=("verdana", 20, "bold"),bg="#f0eae4",fg="#334452",padx=2)
        labelframeleft.place(x=0, y=38, width=450, height=342)

        #EventId
        lbl_EventId = Label(labelframeleft, text="Event ID", font=("verdana", 17, "bold"),bg="#f0eae4",fg="#334452", padx=2, pady=6)
        lbl_EventId.grid(row=0, column=0, sticky=W)

        entry_EventId = ttk.Entry(labelframeleft,width=10,textvariable=self.var_EventId,font=("verdana", 20, "bold"),state="readonly")
        entry_EventId.grid(row=0, column=1, sticky=W)

        #EventName(combo box)
        lbl_EventName = Label(labelframeleft, font=("verdana", 17, "bold"),bg="#f0eae4",fg="#334452", text="Event Name")
        lbl_EventName.grid(row=1, column=0, sticky=W)

        combo_EventName = ttk.Combobox(labelframeleft,textvariable=self.var_EventName,font=("verdana", 15, "bold"), width=16, state="readonly")
        combo_EventName["value"] = ("Google Developer", "Robotics", "Scientific Research", "Ideathon")
        combo_EventName.current(0)
        combo_EventName.grid(row=1, column=1, sticky=W)

        #Date
        lbl_Date = Label(labelframeleft, text="Date", font=("verdana", 17, "bold"),bg="#f0eae4",fg="#334452", padx=2, pady=6)
        lbl_Date.grid(row=2, column=0, sticky=W)

        entry_Date = ttk.Entry(labelframeleft,textvariable=self.var_Date,width=10, font=("verdana", 20, "bold"))
        entry_Date.grid(row=2, column=1, sticky=W)

        #Timings(combo box)
        lbl_Timings = Label(labelframeleft, font=("verdana", 17, "bold"),bg="#f0eae4",fg="#334452",text="Timings")
        lbl_Timings.grid(row=3, column=0, sticky=W)

        combo_Timings = ttk.Combobox(labelframeleft,textvariable=self.var_Timings,font=("verdana", 15, "bold"), width=16, state="readonly")
        combo_Timings["value"] = ("5pm to 6pm", "6pm to 7pm ", "7pm to 8pm", "8pm to 9pm")
        combo_Timings.current(0)
        combo_Timings.grid(row=3, column=1, sticky=W)

        #EventTypeId
        lbl_EventTypeId = Label(labelframeleft, text="Event Type ID", font=("verdana", 17, "bold"),bg="#f0eae4",fg="#334452", padx=2, pady=6)
        lbl_EventTypeId.grid(row=4, column=0, sticky=W)

        entry_EventTypeId = ttk.Entry(labelframeleft,textvariable=self.var_EventTypeId,width=10, font=("verdana", 20, "bold"))
        entry_EventTypeId.grid(row=4, column=1, sticky=W)

        # buttons
        btn_frame = Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=2, y=250, width=435, height=40)

        btnCreate = Button(btn_frame, text="Create",command=self.add_data,font=("verdana", 13, "bold"),bg="white", fg="#334452", width=8)
        btnCreate.grid(row=0, column=0, padx=1)

        btnUpdate = Button(btn_frame, text="Update",command=self.update,font=("verdana", 13, "bold"),bg="white", fg="#334452", width=8)
        btnUpdate.grid(row=0, column=1, padx=1)

        btnDelete = Button(btn_frame, text="Delete",command=self.mdelete,font=("verdana", 13, "bold"),bg="white", fg="#334452", width=8)
        btnDelete.grid(row=0, column=2, padx=1)

        btnReset = Button(btn_frame, text="Reset",command=self.reset,font=("verdana", 13, "bold"), bg="white",fg="#334452", width=8)
        btnReset.grid(row=0, column=3, padx=1)

        # table frame search system
        Table_Frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details",font=("verdana", 20, "bold"),bg="#f0eae4",fg="#334452", padx=2)
        Table_Frame.place(x=453, y=37, width=430, height=340)

        details_table = Frame(Table_Frame, bd=2, relief=RIDGE)
        details_table.place(x=9, y=90, width=410, height=100)

        scroll_x = ttk.Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Table_Frame, orient=VERTICAL)

        self.eventType_table = ttk.Treeview(Table_Frame,column=("eventId", "eventName", "date", "timings","eventTypeId"),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.eventType_table.xview)
        scroll_y.config(command=self.eventType_table.yview)

        self.eventType_table.heading("eventId", text="Event ID")
        self.eventType_table.heading("eventName", text="Event Name")
        self.eventType_table.heading("date", text="Date")
        self.eventType_table.heading("timings", text="Timings")
        self.eventType_table.heading("eventTypeId", text="Event Type ID")

        self.eventType_table["show"] = "headings"

        self.eventType_table.column("eventId", width=100)
        self.eventType_table.column("eventName", width=100)
        self.eventType_table.column("date", width=100)
        self.eventType_table.column("timings", width=100)
        self.eventType_table.column("eventTypeId", width=100)

        self.eventType_table.pack(fill=BOTH, expand=1)
        self.eventType_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_EventId.get() == "" or self.var_EventTypeId.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="heythisistushar@123",
                    database="Event-Booking"
                )
                my_cursor = conn.cursor()
                my_cursor.execute("insert into event values(%s,%s,%s,%s,%s)", (
                                                                            self.var_EventId.get(),
                                                                            self.var_EventName.get(),
                                                                            self.var_Date.get(),
                                                                            self.var_Timings.get(),
                                                                            self.var_EventTypeId.get()

                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Event Booked", parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning", "Something went wrong:{str(es)}", parent=self.root)

    def fetch_data(self):
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="heythisistushar@123",
            database="Event-Booking"
        )
        my_cursor = conn.cursor()
        my_cursor.execute("select * from event")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.eventType_table.delete(*self.eventType_table.get_children())
            for i in rows:
                self.eventType_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        cursor_row=self.eventType_table.focus()
        content=self.eventType_table.item(cursor_row)
        row=content["values"]

        self.var_EventId.set(row[0]),
        self.var_EventName.set(row[1]),
        self.var_Date.set(row[2]),
        self.var_Timings.set(row[3]),
        self.var_EventTypeId.set(row[4]),

    def update(self):
        if self.var_EventTypeId.get()=="":
            messagebox.showerror("Error","Please enter the Event Type Id",parent=self.root)
        else:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="heythisistushar@123",
                database="Event-Booking"
            )
            my_cursor = conn.cursor()
            my_cursor.execute("update event set EventName=%s,Date=%s,Timings=%s where EventId=%s",(
                                                                                                    self.var_EventName.get(),
                                                                                                    self.var_Date.get(),
                                                                                                    self.var_Timings.get(),
                                                                                                    self.var_EventId.get()
                              ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Updated","Event has been updated successfully",parent=self.root)

    def mdelete(self):
        mdelete=messagebox.askyesno("Event Management System","Do you want to delete this User",parent=self.root)
        if mdelete>0:
                conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="heythisistushar@123",
                database="Event-Booking"
                )
                my_cursor = conn.cursor()
                query="delete from event where EventId=%s"
                value=(self.var_EventId.get(),)
                my_cursor.execute(query,value)
        else:
            if not mdelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    def reset(self):
        #self.var_EventId.set("")
        #self.var_EventName.set(""),
        self.var_Date.set(""),
        #self.var_Timings.set(""),
        self.var_EventTypeId.set("")

        x = random.randint(1000, 9999)
        self.var_EventId.set(str(x))

        #*************************************

class Venuebooking:
    def __init__(self,root):
        self.root=root
        self.root.title("")
        self.root.geometry("888x382+350+298")
        self.root.config(background='#f0eae4')

        #variables
        self.var_venueId = StringVar()
        x = random.randint(1000, 9999)
        self.var_venueId.set(str(x))

        self.var_eventId = StringVar()
        self.var_city = StringVar()
        self.var_address = StringVar()
        self.var_noOfTickets = StringVar()

        # title
        lbl_title = Label(self.root, text="ADD VENUE DETAILS", font=("verdana", 20, "bold"), bg="#f0eae4",fg="#334452", bd=0)
        lbl_title.place(x=300, y=0, width=320, height=35)

        # label frame
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Venue Details",font=("verdana", 20, "bold"), padx=2, bg="#f0eae4",fg="#334452")
        labelframeleft.place(x=0, y=38, width=450, height=342)

        # labels and entries
        # venue id
        lbl_venueId = Label(labelframeleft, text="Venue Id", font=("verdana", 17, "bold"),bg="#f0eae4",fg="#334452",padx=2, pady=6)
        lbl_venueId.grid(row=0, column=0, sticky=W)

        entry_venueId = ttk.Entry(labelframeleft,textvariable=self.var_venueId,width=15,font=("verdana", 17, "bold"))
        entry_venueId.grid(row=0, column=1,sticky=W)

        # event id
        lbl_eventId = Label(labelframeleft, text="Event Id", font=("verdana", 17, "bold"),bg="#f0eae4",fg="#334452",padx=2, pady=6)
        lbl_eventId.grid(row=1, column=0, sticky=W)

        entry_eventId = ttk.Entry(labelframeleft, width=15,textvariable=self.var_eventId,font=("verdana", 17, "bold"))
        entry_eventId.grid(row=1, column=1,sticky=W)

        # city
        lbl_city = Label(labelframeleft, text="City", font=("verdana", 17, "bold"),bg="#f0eae4",fg="#334452",padx=2, pady=6)
        lbl_city.grid(row=2, column=0, sticky=W)

        combo_city = ttk.Combobox(labelframeleft,textvariable=self.var_city,font=("verdana", 15, "bold"), width=16, state="readonly")
        combo_city["value"] = ("Bangalore", "Delhi", "Kolkata", "Mumbai")
        combo_city.current(0)
        combo_city.grid(row=2, column=1, sticky=W)

        # address
        lbl_address = Label(labelframeleft, text="Address", font=("verdana", 17, "bold"),bg="#f0eae4",fg="#334452",padx=2, pady=6)
        lbl_address.grid(row=3, column=0, sticky=W)

        combo_address = ttk.Combobox(labelframeleft,textvariable=self.var_address,font=("verdana", 15, "bold"), width=16, state="readonly")
        combo_address["value"] = ("High Street","J Villa","Corporation road")
        combo_address.current(0)
        combo_address.grid(row=3, column=1, sticky=W)

        #capacity
        lbl_noOfTickets = Label(labelframeleft, text="No. of Tickets", font=("verdana", 17, "bold"),bg="#f0eae4",fg="#334452",padx=2, pady=6)
        lbl_noOfTickets.grid(row=4, column=0, sticky=W)

        entry_noOfTickets = ttk.Entry(labelframeleft,textvariable=self.var_noOfTickets,width=15, font=("verdana", 17, "bold"))
        entry_noOfTickets.grid(row=4, column=1,sticky=W)

        # buttons
        btn_frame = Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=2, y=250, width=435, height=40)

        btnCreate = Button(btn_frame, text="Create",command=self.add_data,font=("verdana", 13, "bold"),bg="white", fg="#334452", width=8)
        btnCreate.grid(row=0, column=0, padx=1)

        btnUpdate = Button(btn_frame, text="Update",command=self.update,font=("verdana", 13, "bold"), bg="white", fg="#334452", width=8)
        btnUpdate.grid(row=0, column=1, padx=1)

        btnDelete = Button(btn_frame, text="Delete",command=self.mdelete,font=("verdana", 13, "bold"), bg="white", fg="#334452", width=8)
        btnDelete.grid(row=0, column=2, padx=1)

        btnReset = Button(btn_frame, text="Reset",command=self.reset,font=("verdana", 13, "bold"), bg="white",fg="#334452", width=8)
        btnReset.grid(row=0, column=3, padx=1)

        # table frame search system
        Table_Frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details",font=("verdana", 20, "bold"),bg="#f0eae4",fg="#334452",padx=2)
        Table_Frame.place(x=453, y=37, width=430, height=340)

        # show data table
        details_table = Frame(Table_Frame, bd=2, relief=RIDGE)
        details_table.place(x=9, y=3, width=410, height=302)

        scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)

        self.eventType_table = ttk.Treeview(details_table,column=("venueId", "eventId", "city", "address", "noOfTickets"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.eventType_table.xview)
        scroll_y.config(command=self.eventType_table.yview)

        self.eventType_table.heading("venueId", text="Venue ID")
        self.eventType_table.heading("eventId", text="Event ID")
        self.eventType_table.heading("city", text="City")
        self.eventType_table.heading("address", text="Address")
        self.eventType_table.heading("noOfTickets", text="No. of tickets")

        self.eventType_table["show"] = "headings"

        self.eventType_table.column("venueId", width=100)
        self.eventType_table.column("eventId", width=100)
        self.eventType_table.column("city", width=100)
        self.eventType_table.column("address", width=100)
        self.eventType_table.column("noOfTickets", width=100)

        self.eventType_table.pack(fill=BOTH, expand=1)
        self.eventType_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_eventId.get() == "" or self.var_noOfTickets.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="heythisistushar@123",
                    database="Event-Booking"
                )
                my_cursor = conn.cursor()
                my_cursor.execute("insert into venue values(%s,%s,%s,%s,%s)", (
                    self.var_venueId.get(),
                    self.var_eventId.get(),
                    self.var_city.get(),
                    self.var_address.get(),
                    self.var_noOfTickets.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Event Booked", parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning", "Something went wrong:{str(es)}", parent=self.root)

    def fetch_data(self):
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="heythisistushar@123",
            database="Event-Booking"
        )
        my_cursor = conn.cursor()
        my_cursor.execute("select * from venue")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.eventType_table.delete(*self.eventType_table.get_children())
            for i in rows:
                self.eventType_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self, event=""):
        cursor_row = self.eventType_table.focus()
        content = self.eventType_table.item(cursor_row)
        row = content["values"]

        self.var_venueId.set(row[0]),
        self.var_eventId.set(row[1]),
        self.var_city.set(row[2]),
        self.var_address.set(row[3]),
        self.var_noOfTickets.set(row[4]),

    def update(self):
        if self.var_noOfTickets.get()=="":
            messagebox.showerror("Error","Please enter the total Number of Tickets",parent=self.root)
        else:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="heythisistushar@123",
                database="Event-Booking"
            )
            my_cursor = conn.cursor()
            my_cursor.execute("update venue set City=%s,Address=%s,NoofTickets=%s where EventId=%s",(
                                                                    #self.var_venueId.get(),
                                                                    #self.var_eventId.get(),
                                                                    self.var_city.get(),
                                                                    self.var_address.get(),
                                                                    self.var_noOfTickets.get(),
                                                                    self.var_eventId.get()

                              ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Updated","Venue has been updated successfully",parent=self.root)

    def mdelete(self):
        mdelete=messagebox.askyesno("Event Management System","Do you want to delete this User",parent=self.root)
        if mdelete>0:
                conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="heythisistushar@123",
                database="Event-Booking"
                )
                my_cursor = conn.cursor()
                query="delete from venue where EventId=%s"
                value=(self.var_eventId.get(),)
                my_cursor.execute(query,value)
        else:
            if not mdelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    def reset(self):
        #self.var_venueId.set("")
        self.var_eventId.set(""),
        #self.var_city.set(""),
        #self.var_address.set(""),
        self.var_noOfTickets.set("")

        x = random.randint(1000, 9999)
        self.var_venueId.set(str(x))

        #*******************************

class Ticketbooking:
    def __init__(self,root):
        self.root=root
        self.root.title("")
        self.root.geometry("888x382+350+298")
        self.root.config(background='#f0eae4')

        #variables
        self.var_ticketId = StringVar()
        x = random.randint(1000, 9999)
        self.var_ticketId.set(str(x))

        self.var_eventId = StringVar()

        # title
        lbl_title = Label(self.root, text="TICKET DETAILS", font=("verdana", 20, "bold"), bg="#f0eae4",fg="#334452", bd=0)
        lbl_title.place(x=300, y=0, width=300, height=35)

        # label frame
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Tickets",font=("verdana", 20, "bold"), bg="#f0eae4",fg="#334452" ,padx=2)
        labelframeleft.place(x=0, y=38, width=450, height=342)

        # labels and entries
        # venue id
        lbl_ticketId = Label(labelframeleft, text="Ticket ID", font=("verdana", 17, "bold"), bg="#f0eae4",fg="#334452",padx=2, pady=6)
        lbl_ticketId.grid(row=0, column=0, sticky=W)

        entry_ticketId = ttk.Entry(labelframeleft, textvariable=self.var_ticketId, width=15,font=("verdana", 20, "bold"))
        entry_ticketId.grid(row=0, column=1, sticky=W)

        # event id
        lbl_eventId = Label(labelframeleft, text="Event ID", font=("verdana", 17, "bold"), bg="#f0eae4",fg="#334452",padx=2, pady=6)
        lbl_eventId.grid(row=1, column=0, sticky=W)

        entry_eventId = ttk.Entry(labelframeleft, width=15, textvariable=self.var_eventId,font=("verdana", 20, "bold"))
        entry_eventId.grid(row=1, column=1, sticky=W)

        # buttons
        btn_frame = Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=2, y=250, width=328, height=40)

        btnCreate = Button(btn_frame, text="Create", command=self.add_data, font=("verdana", 13, "bold"),bg="white", fg="#334452", width=8)
        btnCreate.grid(row=0, column=0, padx=1)

        #btnUpdate = Button(btn_frame, text="Update", command=self.update, font=("times new roman", 15, "bold"),bg="black", fg="white", width=8)
        #btnUpdate.grid(row=0, column=1, padx=1)

        btnDelete = Button(btn_frame, text="Delete", command=self.mdelete, font=("verdana", 13, "bold"),bg="white", fg="#334452", width=8)
        btnDelete.grid(row=0, column=1, padx=1)

        btnReset = Button(btn_frame, text="Reset", command=self.reset, font=("verdana", 13, "bold"), bg="white",fg="#334452", width=8)
        btnReset.grid(row=0, column=2, padx=1)

        # table frame search system
        Table_Frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details",font=("verdana", 20, "bold"),bg="#f0eae4",fg="#334452",padx=2)
        Table_Frame.place(x=453, y=37, width=430, height=340)

        # show data table
        details_table = Frame(Table_Frame, bd=2, relief=RIDGE)
        details_table.place(x=9, y=3, width=410, height=302)

        scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)

        self.eventType_table = ttk.Treeview(details_table,column=("ticketId", "eventId"),
                                            xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.eventType_table.xview)
        scroll_y.config(command=self.eventType_table.yview)

        self.eventType_table.heading("ticketId", text="Ticket ID")
        self.eventType_table.heading("eventId", text="Event ID")

        self.eventType_table["show"] = "headings"

        self.eventType_table.column("ticketId", width=100)
        self.eventType_table.column("eventId", width=100)

        self.eventType_table.pack(fill=BOTH, expand=1)
        self.eventType_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_eventId.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="heythisistushar@123",
                    database="Event-Booking"
                )
                my_cursor = conn.cursor()
                my_cursor.execute("insert into ticket values(%s,%s)", (
                    self.var_ticketId.get(),
                    self.var_eventId.get(),
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Event Booked", parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning", "Something went wrong:{str(es)}", parent=self.root)

    def fetch_data(self):
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="heythisistushar@123",
            database="Event-Booking"
        )
        my_cursor = conn.cursor()
        my_cursor.execute("select * from ticket")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.eventType_table.delete(*self.eventType_table.get_children())
            for i in rows:
                self.eventType_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    def get_cursor(self, event=""):
        cursor_row = self.eventType_table.focus()
        content = self.eventType_table.item(cursor_row)
        row = content["values"]

        self.var_ticketId.set(row[0]),
        self.var_eventId.set(row[1]),



    def mdelete(self):
        mdelete = messagebox.askyesno("Event Management System", "Do you want to delete this Ticket", parent=self.root)
        if mdelete > 0:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="heythisistushar@123",
                database="Event-Booking"
            )
            my_cursor = conn.cursor()
            query = "delete from ticket where EventId=%s"
            value = (self.var_eventId.get(),)
            my_cursor.execute(query, value)
        else:
            if not mdelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    def reset(self):
        #self.var_ticketId.set("")
        self.var_eventId.set(""),

        x = random.randint(1000, 9999)
        self.var_ticketId.set(str(x))

        #*******************

class Mealbooking:
    def __init__(self,root):
        self.root=root
        self.root.title("")
        self.root.geometry("888x382+350+298")
        self.root.config(background='#f0eae4')

        #variables
        self.var_ticketId = StringVar()
        self.var_meal = StringVar()

        # title
        lbl_title = Label(self.root, text="MEALS/BEVERAGES", font=("verdana", 20, "bold"), bg="#f0eae4",fg="#334452", bd=0)
        lbl_title.place(x=300, y=0, width=300, height=35)

        # label frame
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Choose", font=("verdana", 20, "bold"),bg="#f0eae4",fg="#334452",padx=2)
        labelframeleft.place(x=0, y=38, width=450, height=342)

        # labels and entries
        # ticket id
        lbl_ticketId = Label(labelframeleft, text="Ticket ID", font=("verdana", 20, "bold"),bg="#f0eae4",fg="#334452" ,padx=2, pady=6)
        lbl_ticketId.grid(row=0, column=0, sticky=W)

        entry_ticketId = ttk.Entry(labelframeleft, textvariable=self.var_ticketId, width=12,font=("verdana", 20, "bold"))
        entry_ticketId.grid(row=0, column=1, sticky=W)

        # meals/bvgs id
        lbl_meal = Label(labelframeleft,text="Event Name",font=("verdana", 20, "bold"),bg="#f0eae4",fg="#334452")
        lbl_meal.grid(row=1, column=0, sticky=W)

        combo_meal = ttk.Combobox(labelframeleft, textvariable=self.var_meal, font=("verdana", 15, "bold"), width=15, state="readonly")
        combo_meal["value"] = ("Popcorn", "Burger", "Water", "Fruit Juice")
        combo_meal.current(0)
        combo_meal.grid(row=1, column=1, sticky=W)

        # buttons
        btn_frame = Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=2, y=250, width=435, height=40)

        btnCreate = Button(btn_frame, text="Create", command=self.add_data, font=("verdana", 13, "bold"),bg="white", fg="#334452", width=8)
        btnCreate.grid(row=0, column=0, padx=1)

        btnUpdate = Button(btn_frame, text="Update", command=self.update, font=("verdana", 13, "bold"),bg="white", fg="#334452", width=8)
        btnUpdate.grid(row=0, column=1, padx=1)

        btnDelete = Button(btn_frame, text="Delete", command=self.mdelete, font=("verdana", 13, "bold"),bg="white", fg="#334452", width=8)
        btnDelete.grid(row=0, column=2, padx=1)

        btnReset = Button(btn_frame, text="Reset", command=self.reset, font=("verdana", 13, "bold"), bg="white",fg="#334452", width=8)
        btnReset.grid(row=0, column=3, padx=1)

        # table frame search system
        Table_Frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details",font=("verdana", 20, "bold"),bg="#f0eae4",fg="#334452",padx=2)
        Table_Frame.place(x=453, y=37, width=430, height=340)

        # show data table
        details_table = Frame(Table_Frame, bd=2, relief=RIDGE)
        details_table.place(x=9, y=3, width=410, height=302)

        scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)

        self.eventType_table = ttk.Treeview(details_table, column=("ticketId", "meal"),
                                            xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.eventType_table.xview)
        scroll_y.config(command=self.eventType_table.yview)

        self.eventType_table.heading("ticketId", text="Ticket ID")
        self.eventType_table.heading("meal", text="Meals/Beverages")

        self.eventType_table["show"] = "headings"

        self.eventType_table.column("ticketId", width=100)
        self.eventType_table.column("meal", width=100)

        self.eventType_table.pack(fill=BOTH, expand=1)
        self.eventType_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_meal.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="heythisistushar@123",
                    database="Event-Booking"
                )
                my_cursor = conn.cursor()
                my_cursor.execute("insert into meal values(%s,%s)", (
                    self.var_ticketId.get(),
                    self.var_meal.get(),
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Event Booked", parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning", "Something went wrong:{str(es)}", parent=self.root)

    def fetch_data(self):
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="heythisistushar@123",
            database="Event-Booking"
        )
        my_cursor = conn.cursor()
        my_cursor.execute("select * from meal")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.eventType_table.delete(*self.eventType_table.get_children())
            for i in rows:
                self.eventType_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    def get_cursor(self, event=""):
        cursor_row = self.eventType_table.focus()
        content = self.eventType_table.item(cursor_row)
        row = content["values"]

        self.var_ticketId.set(row[0]),
        self.var_meal.set(row[1])

    def update(self):
        if self.var_meal.get()=="":
            messagebox.showerror("Error","Please enter the total Number of Tickets",parent=self.root)
        else:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="heythisistushar@123",
                database="Event-Booking"
            )
            my_cursor = conn.cursor()
            my_cursor.execute("update meal set Meal=%s where TicketId=%s",(
                                                                    #self.var_venueId.get(),
                                                                    #self.var_eventId.get(),
                                                                    self.var_meal.get(),
                                                                    self.var_ticketId.get(),
                              ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Updated","Meal has been updated successfully",parent=self.root)

    def mdelete(self):
        mdelete = messagebox.askyesno("Event Management System", "Do you want to delete this Ticket", parent=self.root)
        if mdelete > 0:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="heythisistushar@123",
                database="Event-Booking"
            )
            my_cursor = conn.cursor()
            query = "delete from meal where TicketId=%s"
            value = (self.var_ticketId.get(),)
            my_cursor.execute(query, value)
        else:
            if not mdelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    def reset(self):
        #self.var_ticketId.set("")
        self.var_ticketId.set(""),



if __name__ == "__main__":
    main()
