from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import random
from tkinter import messagebox
import mysql.connector


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
            #query2 = "delete from ticket where TicketId=%s"
            #query1 = "delete from meal where TicketId=%s"
            value = (self.var_eventId.get(),)
            value1 = (self.var_ticketId.get(),)
            my_cursor.execute(query, value)
            #my_cursor.execute(query1, value1)
            #my_cursor.execute(query2, value1)
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


if __name__=="__main__":
    root=Tk()
    obj=Ticketbooking(root)
    root.mainloop()