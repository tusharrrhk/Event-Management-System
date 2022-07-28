from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import random
from tkinter import messagebox
import mysql.connector

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

if __name__=="__main__":
    root=Tk()
    obj=Venuebooking(root)
    root.mainloop()