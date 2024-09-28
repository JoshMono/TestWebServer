import sqlite3

def CreateTable():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("""CREATE TABLE users (
        first_name text,
        last_name text,
        age integer,
        email text
        )
    """)
    conn.commit()
    conn.close()

def AddRecord(f_name, l_name, age, email):
   conn = sqlite3.connect("database.db")
   c = conn.cursor()
   c.execute(F'''INSERT INTO users VALUES (
        "{f_name}",
        "{l_name}",
        "{age}",
        "{email}"
       )
   ''')
   conn.commit()
   conn.close()
   return print(f_name, l_name, age, email)

def FetchRecords():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("SELECT rowid, * FROM users")
    users = c.fetchall()
    conn.close()
    return users

def GetRecordFromID(id):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute(F"SELECT rowid, * FROM users WHERE rowid = {id}")
    user = c.fetchone()
    conn.close()
    return user

def UpdateRecord(id, f_name, l_name, age, email):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute(F"""UPDATE users SET 
    first_name = "{f_name}",
    last_name = "{l_name}",
    age = "{age}",
    email = "{email}"
    
    WHERE rowid = {id}
    """)
    conn.commit()
    conn.close()

def DeleteRecord(id):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute(F"""DELETE from users  
    WHERE rowid = {id}
    """)
    conn.commit()
    conn.close()
    
    

#conn = sqlite3.connect("database.db")
#c = conn.cursor()

#CreateTable(conn)
#FetchRecords(c)

#conn.commit()
#conn.close()
