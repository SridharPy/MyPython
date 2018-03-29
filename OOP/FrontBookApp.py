from tkinter import *
from BackBookApp import Database # Importing Database Class from Backend Module

#Since this function is binded to listbox list1 widget this function gets speacial parameter called event
#This event parameter holds the information about type of the event
#This function is called on bt event on list1 by bind method but when we call it from delete_command we can't not pass args
#So it will error, as function needs 1 arg amd we are not passing it when we call from delete_command
#So to fix we set a global variable which will hold id value of selected item in the list 1 which will be used by delere_command
def get_selected_row(event):
    try:
        global selected_row
        #index = list1.curselection() it prints current postion of selection e.g. (4,) in tuple format
        index=list1.curselection()[0] #We want to pull first value from it
        selected_row=list1.get(index) #Gets all the values of teh index position in the list1 like below
        # (5, 'A Beautiful Mind', 'Knight N Shyamalan', 1996, 3565389454)
        #Populates entry boxes with selected item values from list1
        e1.delete(0,END)
        e1.insert(END,selected_row[1])
        e2.delete(0,END)
        e2.insert(END,selected_row[2])
        e3.delete(0,END)
        e3.insert(END,selected_row[3])
        e4.delete(0,END)
        e4.insert(END,selected_row[4])
    except IndexError:
        pass

win = Tk() #Creates Window

win.wm_title("Book Store")

#Create Class object
db=Database() # Here Database class creates an object instance ans stores in the variable db

#And this object instance is implicitly passed into the functions within the Database Class

# So we add self or any other word as first parameter in each function of Class

#Functions
def view_command():
    list1.delete(0,END)
    for row in db.view():
        list1.insert(END,row)

def search_command():
    list1.delete(0,END)
    for row in db.search(e1_title.get(),e2_author.get(),e3_year.get(),e4_isbn.get()):
        list1.insert(END,row)

def add_command():
    db.insert(e1_title.get(),e2_author.get(),e3_year.get(),e4_isbn.get())
    list1.delete(0,END) # Clear List
    list1.insert(END,(e1_title.get(),e2_author.get(),e3_year.get(),e4_isbn.get()))
    # Kept e_title.get(),e2_author.. etc within () to pass it as a single field to avoid newline

def delete_command():
    db.delete(selected_row[0]) #pull first value from list that is id field

def update_command():
    db.update(selected_row[0],e1_title.get(),e2_author.get(),e3_year.get(),e4_isbn.get())

#Labels
l1 = Label(win,text="Title")
l1.grid(row=0,column=0)

l2 = Label(win,text="Author")
l2.grid(row=0,column=2)

l3 = Label(win,text="Year")
l3.grid(row=1,column=0)

l4 = Label(win,text="ISBN")
l4.grid(row=1,column=2)

#Entry Text
e1_title = StringVar()
e1 = Entry(win,textvariable=e1_title)
e1.grid(row=0,column=1)

e2_author = StringVar()
e2 = Entry(win,textvariable=e2_author)
e2.grid(row=0,column=3)

e3_year = StringVar()
e3 = Entry(win,textvariable=e3_year)
e3.grid(row=1,column=1)

e4_isbn = StringVar()
e4 = Entry(win,textvariable=e4_isbn)
e4.grid(row=1,column=3)

#listbox
list1 = Listbox(win,height=7, width =45)
list1.grid(row=2,column=0, rowspan=6, columnspan=2) #rowspan and columns span are used for proper alignmnet of listbox else it till use all space and move rest of the widgets

#Scroll Bar
sb1 = Scrollbar(win)
sb1.grid(row=2,column=2,rowspan=6,columnspan=1) #rowspan and colspans for proper alignment

#Listbox and Scrollbar binding
list1.configure(yscrollcommand=sb1.set) #Binds Scrollbar to listbox on y axis or vertically
sb1.configure(command=list1.yview) #Binds yaxis or vertical of list to scrollbar

#Bind function is used for ListBox to get highlighted item in the GUI
#Bind is used to bind a funtion to a widget event
#bind takes 2 args, 1 for event type and 2nd for event function you want to bind the event to
#We write the get_selected_row function above to return the sleceted tuple items
list1.bind('<<ListboxSelect>>',get_selected_row)
#when we bind get_selected_row to List event python know this fucntionexpectes a parameter called event

#Buttons
b1 = Button(win,text="View All", width=12, command=view_command)
b1.grid(row=2, column=3)

b2 = Button(win,text="Search Entry", width=12, command=search_command)
b2.grid(row=3, column=3)

b3 = Button(win,text="Add Entry", width=12, command=add_command)
b3.grid(row=4, column=3)

b4 = Button(win,text="Update Selected", width=12, command=update_command)
b4.grid(row=5, column=3)

b5 = Button(win,text="Delete Selected",width=12, command=delete_command)
b5.grid(row=6, column=3)

b6 = Button(win,text="Close",width=12,command=win.destroy)
b6.grid(row=7, column=3)

win.mainloop() #Loops Window doesn't allow it to auto close
