from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import random
from tkinter import messagebox
import mysql.connector


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
                query="delete from eventtype where eventTypeId=%s"
                #query1 = "delete from event where eventTypeId=%s"
                value=(self.var_eventTypeId.get(),)
                my_cursor.execute(query,value)
                #my_cursor.execute(query1, value)
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




if __name__=="__main__":
    root=Tk()
    obj=EventTypeBooking(root)
    root.mainloop()