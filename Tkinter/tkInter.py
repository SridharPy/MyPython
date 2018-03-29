#import tkinter
from tkinter import * #import all from tkinter this avoid typing tkinter.Tk()

#window = tkinter.Tk()
window = Tk()

def km_to_miles():
    miles = float(e1_val.get()) * 1.609344 #e1_val is the variable for entry text and get pulls the value enetered in the entry widget the value assigned to e1_val
    t1.delete(1.0,END) #Deletes previous values in text widget, else values witll append for every new conversion
    t1.insert(END,miles) #this inserts at end of Text widget the value of miles

"""For Widget help like for Button type in ipython from cmd and from tkinter import * and type Button? to get al paramteres for button"""
b1=Button(window,text='KM To Miles', command=km_to_miles) #Creates a button widget with name Execute, command will execute the whatever is supplieds
#b1.pack() #This will tie/pack button to window
b1.grid(row=0,column=0)#This is also used for tieing widget to Window but with grater flexibility like we can position button on row and window.

#Put a textbox or entry in Window
e1_val = StringVar()
e1=Entry(window,textvariable=e1_val) #Textvariable takes value entered and assign that value to e1_val variable which is a StringVar() datatype
e1.grid(row=0,column=1)

#Put a text Widget
t1=Text(window, height=2, width=30) #by default the size of text widget is very large we need to sepcify height and width in cells
t1.grid(row=0,column=2)

window.mainloop() #Required for window to no wuto close
