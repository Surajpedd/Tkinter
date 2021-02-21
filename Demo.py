import mysql.connector
from tkinter import *
import tkinter.messagebox as Messagebox

# Function to Insert into the Database
def store():
    name = ne.get()
    age = ae.get()
    if len(name) == 0 and len(age) == 0:
        Messagebox.showwarning("Error","Data not Entered")
    else:
        mydb = mysql.connector.connect(host="localhost", user ="yourusername", passwd = "your password", database = "User")
        c = mydb.cursor()
        c.execute("INSERT INTO Info(Name,Age) VALUES(%s,%s)",(name,int(age)))
        mydb.commit()
        Messagebox.showinfo("Insert Status","Successfully Inserted")
        # to clear Entries of Name and Age for next Input
        # ne.delete(0,END)
        # ae.delete(0,END)
        
# creating the window
root = Tk() 
root.geometry("600x400")
root.title("MySQL and Tkinter in Python")
root.configure(bg = 'black')

nm = Label(root,text = "Enter your Name",font = ('arial 16 bold'),bg = 'black',fg = 'yellow')
nm.place(x = 10,y = 100)
ne = Entry(root,font = ('arial 16 bold italic'), width = 20,fg = 'blue')
ne.place(x = 250, y = 100)
ag = Label(root,text = "Enter your Age",font = ('arial 16 bold'),bg = 'black',fg = 'yellow')
ag.place(x = 10,y = 200)
ae = Entry(root,font = ('arial 16 bold italic'), width = 20,fg = 'blue')
ae.place(x = 250, y = 200)
ins = Button(root,text = "Click Me" , bg = "red",fg = "white",width = 20,height = 2,activebackground="green",command=store)
ins.place(x =200 , y = 300)
root.mainloop()
