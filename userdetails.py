from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import random
from tkinter import messagebox
import mysql.connector


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



    def fetch_data(self):
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="heythisistushar@123",
            database="Event-Booking"
        )
        my_cursor = conn.cursor()
        my_cursor.execute("call find_all_users()")
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
                query=("delete from user_details where Username=%s")
                #query1=("delete from eventtype where Username=%s")
                #query2 = ("delete from event where Username=%s")
                #query3 = ("delete from ticket where Username=%s")
                value=(self.var_username.get(),)
                my_cursor.execute(query,value)
                #my_cursor.execute(query1, value)
                #my_cursor.execute(query2, value)
                #my_cursor.execute(query3,value)
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




if __name__=="__main__":
    root=Tk()
    obj=userdetails_win(root)
    root.mainloop()