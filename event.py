from tkinter import*
from PIL import  Image,ImageTk
from datetime import datetime
from userdetails import userdetails_win
from eventType import EventTypeBooking
from eventt import Eventt
from venue import Venuebooking
from ticket import Ticketbooking
from meal import Mealbooking


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





if __name__ == '__main__':
    root=Tk()
    obj=EventManagementSystem(root)
    root.mainloop()
