import sqlite3

def create():
    khu = sqlite3.connect("tele1.db")
    cur = khu.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tele (id INTEGER PRIMARY KEY, name text,surname text,residentail text,mobile integer)")
    khu.commit()
    khu.close()

def insert(name,surname,resi,mobile):
    khu = sqlite3.connect("tele1.db")
    cur = khu.cursor()
    cur.execute("INSERT INTO tele VALUES (NULL,?,?,?,?)",(name,surname,resi,mobile))
    khu.commit()
    khu.close()

def display():
    khu = sqlite3.connect("tele1.db")
    cur = khu.cursor()
    cur.execute("SELECT * FROM tele")
    lol = cur.fetchall()
    khu.close()
    return lol

def search(name = "",surname = "",resi = "",mobile = ""):
    khu = sqlite3.connect("tele1.db")
    cur = khu.cursor()
    cur.execute("SELECT * FROM tele WHERE name = ? OR surname = ? OR residentail = ? OR mobile = ?",(name,surname,resi,mobile))
    lol = cur.fetchall()
    khu.close()
    return lol

def dele(id):
    khu = sqlite3.connect("tele1.db")
    cur = khu.cursor()
    cur.execute("DELETE FROM tele WHERE id = ?",(id,))
    khu.commit()
    khu.close()    

def update(id,name,surname,resi,mobile):
    khu = sqlite3.connect("tele1.db")
    cur = khu.cursor()
    cur.execute("UPDATE tele SET name = ?, surname = ?, residentail = ?, mobile = ? WHERE id = ?",(name,surname,resi,mobile,id))
    khu.commit()
    khu.close()   

create()
update(4,'mahakali','VAIHSNA','dadar',1234567890)
#insert('khushalii','Railbole','kalyan',8419979419)
#dele(7)
print(display())
#print(search(resi='kalyan'))
