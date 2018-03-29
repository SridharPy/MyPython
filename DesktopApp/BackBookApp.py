import sqlite3

def connect():
    con = sqlite3.connect("books.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (ID integer Primary Key, Title text, Author text, Year integer, ISBN integer)")
    con.commit()
    con.close()

def insert(title="",author="",year="",isbn=""):
    con = sqlite3.connect("books.db")
    cur = con.cursor()
    cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)",(title,author,year,isbn)) # NULL tells python to sen auto incremented value for the firt column i.e. ID in book table
    con.commit()
    con.close()

def view():
    con = sqlite3.connect("books.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM book")
    rows = cur.fetchall()
    con.close
    return rows

def search(title,author,year,isbn):
    con = sqlite3.connect("books.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM book WHERE Title=? OR Author=? OR Year=? OR ISBN=?",(title,author,year,isbn))
    rows = cur.fetchall()
    con.close
    return rows

def delete(id):
    con = sqlite3.connect("books.db")
    cur = con.cursor()
    cur.execute("DELETE FROM book WHERE id=?",(id,)) #, is required after id for delete and update  is single argument is passed
    con.commit()
    con.close()

def update(id,title,author,year,isbn):
    con = sqlite3.connect("books.db")
    cur = con.cursor()
    cur.execute("UPDATE book SET Title=?, Author=?, Year=?, ISBN=? WHERE id=?",(title,author,year,isbn,id))
    con.commit()
    con.close()

#connect()
#insert("Many Masters Many Slaves","Dr Brian Weiss",1976,987545421)
#print(view())
#delete(5)
#update(3,"Bhaag Milkha","Milkha Singh",2014,42456735)
#print(search(author="Milkha Singh"))
#print(view())
