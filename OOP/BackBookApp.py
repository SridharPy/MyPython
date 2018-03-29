import sqlite3

class Database:


    def __init__(self):
        self.con = sqlite3.connect("books.db")
        self.cur = self.con.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS book (ID integer Primary Key, Title text, Author text, Year integer, ISBN integer)")
        self.con.commit()
        #self.con.commit()
        #self.con.close()

    def view(self):
        self.cur.execute("SELECT * FROM book")
        rows = self.cur.fetchall()
        return rows

    def search(self,title,author,year,isbn):
        self.cur.execute("SELECT * FROM book WHERE Title=? OR Author=? OR Year=? OR ISBN=?",(title,author,year,isbn))
        rows = self.cur.fetchall()
        return rows

    def insert(self,title="",author="",year="",isbn=""):
        self.cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)",(title,author,year,isbn)) # NULL tells python to sen auto incremented value for the firt column i.e. ID in book table
        self.con.commit()


    def delete(self,id):
        self.cur.execute("DELETE FROM book WHERE id=?",(id,)) #, is required after id for delete and update  is single argument is passed
        self.con.commit()

    def update(self,id,title,author,year,isbn):
        self.cur.execute("UPDATE book SET Title=?, Author=?, Year=?, ISBN=? WHERE id=?",(title,author,year,isbn,id))
        self.con.commit()

    def __del__(self):
        self.con.close()

    #connect()
    #insert("Many Masters Many Slaves","Dr Brian Weiss",1976,987545421)
    #print(view())
    #delete(5)
    #update(3,"Bhaag Milkha","Milkha Singh",2014,42456735)
    #print(search(author="Milkha Singh"))
    #print(view())
