import sqlite3
from tkinter import *

def view():
    con = sqlite3.connect("lite.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    t1.delete(1.0,END)
    t1.insert(END,rows)
    con.close()

def delete():
    con = sqlite3.connect("lite.db")
    cur = con.cursor()
    cur.execute("DELETE FROM store where item = ?",(e1_val.get(),))
    con.commit()
    con.close()
def insert():
    con = sqlite3.connect("lite.db")
    cur = con.cursor()
    cur.execute("INSERT INTO Store VALUES (?,?,?)",(e2_val.get(),e3_val.get(),e4_val.get()))
    con.commit()
    con.close()

win = Tk()
b1 = Button(win,text ="Show Data",command= view)
b1.grid(row = 0, column = 0 )

t1 = Text(win,height = 2, width = 60)
t1.grid(row =0, column = 1)

l1 = Label(win,text= "Item Name")
l1.grid(row =3, column =0)

e1_val = StringVar()
e1 = Entry(win,textvariable= e1_val)
e1.grid(row = 3, column = 1)

b2 = Button(win,text="Delete Item", command= delete)
b2.grid(row=3,column = 2)

l4 = Label(win, text = "Insert Data in Table")
l4.grid(row = 4, column = 1)

l2 = Label(win, text = "Item")
l2.grid(row = 5, column = 0)

e2_val= StringVar()
e2 = Entry(win,textvariable = e2_val)
e2.grid(row = 5, column = 1)

l3 = Label(win, text = "Quantity")
l3.grid(row = 6, column = 0)
e3_val= StringVar()
e3 = Entry(win,textvariable = e3_val)
e3.grid(row = 6, column = 1)

l3 = Label(win, text = "Price")
l3.grid(row = 7, column = 0)
e4_val= StringVar()
e4 = Entry(win,textvariable = e4_val)
e4.grid(row = 7, column = 1)

b2 = Button(win,text = "Insert Data", command = insert)
b2.grid(row = 8 , column = 1)


win.mainloop()
