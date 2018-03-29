from tkinter import *

def convert_func():
    pound = float(e1_var.get()) * 2.20462
    gram = float(e1_var.get()) * 1000
    ounce = float(e1_var.get()) * 35.274
    t1_pound.delete(1.0,END)
    t1_pound.insert(END,pound)
    t1_gram.delete(1.0,END)
    t1_gram.insert(END,gram)
    t1_ounce.delete(1.0,END)
    t1_ounce.insert(END,ounce)


w1 = Tk()
#Labels for all entry and text widgets
l1_var = StringVar()
l1 = Label(w1,textvariable= l1_var)
l1.grid(row=0,column=1)
l1_var.set("Kilograms")

l1 = Label(w1,text = "Pounds")
l1.grid(row=1,column=1)

l2 = Label(w1,text = "Grams")
l2.grid(row=1,column=2)

l3 = Label(w1,text= "Ounces")
l3.grid(row=1, column = 3)



#Entry widget for KG
e1_var = StringVar()
e1 = Entry(w1,textvariable=e1_var)
e1.grid(row=0,column=2)

#Button widget to perfrom conversion

b1 = Button(w1,text="Convert",command=convert_func)
b1.grid(row = 0 , column = 3)

#All text widgets to display converted values
t1_pound = Text(w1,height =1, width=10)
t1_pound.grid(row=2, column=1)

t1_gram = Text(w1,height =1, width = 10)
t1_gram.grid(row =2, column = 2)

t1_ounce = Text(w1,height=1,width = 10)
t1_ounce.grid(row=2,column = 3)

w1.mainloop()
