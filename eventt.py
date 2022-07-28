from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import random
from tkinter import messagebox
import mysql.connector


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
                #query1="delete from venue where EventId=%s"
                #query2 = "delete from ticket where EventId=%s"

                value=(self.var_EventId.get(),)
                my_cursor.execute(query,value)
                #my_cursor.execute(query1, value)
                #my_cursor.execute(query2, value)

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




if __name__=="__main__":
    root=Tk()
    obj=Eventt(root)
    root.mainloop()