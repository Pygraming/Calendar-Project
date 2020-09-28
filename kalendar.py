from tkinter import *
from tkcalendar import *

root = Tk()
root.title("Pygraming")
root.iconbitmap("C:/Users/Marko/Desktop/calendar.ico")
root.geometry("580x500")

cal = Calendar(root, selectmode="day", year = 2020, month = 9, day = 3)
cal.pack(pady = 20, fill = "both", expand = True)

def grab_date():
    my_label.config(text = " You picked this date: \n" + cal.get_date())

my_button = Button(root, text = "Get Date", command = grab_date)
my_button.pack(pady = 20)

my_label = Label(root, text = "")
my_label.pack(pady = 20)


root.mainloop()
















