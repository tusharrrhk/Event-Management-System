from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector



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

        name_entry=ttk.Entry(frame,textvariable=self.var_name,font=("verdana",20,"bold"))
        name_entry.place(x=500,y=120,width=250)

        phone = Label(frame, text="Phone", font=("verdana", 20, "bold"),bg="#f0eae4",fg="#334452")
        phone.place(x=100, y=170)

        phone_entry = ttk.Entry(frame,textvariable=self.var_phone,font=("verdana", 20, "bold"))
        phone_entry.place(x=500, y=170, width=250)

        age = Label(frame, text="Age", font=("verdana", 20, "bold"),bg="#f0eae4",fg="#334452")
        age.place(x=100, y=220)

        age_entry = ttk.Entry(frame,textvariable=self.var_age,font=("verdana", 20, "bold"))
        age_entry.place(x=500, y=220, width=250)

        Username = Label(frame, text="Username", font=("verdana", 20, "bold"),bg="#f0eae4",fg="#334452")
        Username.place(x=100, y=270)

        Username_entry = ttk.Entry(frame,textvariable=self.var_username,font=("verdana", 20, "bold"))
        Username_entry.place(x=500, y=270, width=250)

        Password = Label(frame, text="Password", font=("verdana", 20, "bold"),bg="#f0eae4",fg="#334452")
        Password.place(x=100, y=320)

        Password_entry = ttk.Entry(frame,textvariable=self.var_password,font=("verdana", 20, "bold"))
        Password_entry.place(x=500, y=320, width=250)

        SecretCode = Label(frame, text="Enter secret code", font=("verdana", 20, "bold"),bg="#f0eae4",fg="#334452")
        SecretCode.place(x=100, y=370)

        SecretCode_entry = ttk.Entry(frame,textvariable=self.var_secretCode,font=("verdana", 20, "bold"))
        SecretCode_entry.place(x=500, y=370, width=250)

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



if __name__ == '__main__':
    root=Tk()
    app=Register(root)
    root.mainloop()