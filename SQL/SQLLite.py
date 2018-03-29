import sqlite3

# The connection sqlite3.connect : lite.db db file is created if it doesn't exist else will connect if exists
def create_table():
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Store (Item text, Quantity integer, Price real )")
    conn.commit()
    conn.close()

def insert_table(itm,qty,prc):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO Store VALUES (?,?,?)",(itm,qty,prc))
    conn.commit()
    conn.close()

def view_table():
    con = sqlite3.connect("lite.db")
    cur1 = con.cursor()
    cur1.execute("Select * FROM store")
    rows = cur1.fetchall()
    con.close
    return rows

print("Enter Item Name : ")
i = str(input())
print("\nEnter Quantity : ")
q = int(input())
print("\nEnter Price : ")
p = float(input())

insert_table(i,q,p)

print(view_table())
