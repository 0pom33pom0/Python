"""
import sqlite3
conn = sqlite3.connect (r"D:\w2\Suracha_python\week6.db")
c = conn.cursor()
c.execute ('''INSERT INTO users (id,fname,lname,email) VALUES (NULL,"ประหยัด","จันอังคาร","heedang@kkumail.com")''')
c.execute ('''INSERT INTO users VALUES (NULL,"B","B","B")''')
conn.commit()
conn.close()

import sqlite3
def insertTousers (fname,lname,email):
    try :
        conn = sqlite3.connect (r"D:\w2\Suracha_python\week6.db")
        c = conn.cursor()

        sql = '''INSERT INTO users (fname,lname,email) VALUES (?,?,?)'''
        data = (fname,lname,email)
        c.execute(sql,data)
        conn.commit()
        c.close()

    except sqlite3.Error as e:
        print('Failed to insert: ',e)
    finally:

        if conn:
            conn.close()

insertTousers('pom','mop','pom@kkumail.com')
insertTousers('ppp','ooo','mmm')

import sqlite3
conn = sqlite3.connect (r"D:\w2\Suracha_python\week6.db")
c = conn.cursor()
try:
    data = ('B','B','B'),('C','C','C'),('D','D','D')
    c.executemany('INSERT INTO users (fname,lname,email) VALUES (?,?,?)',data)
    conn.commit()
    c.close()
except sqlite3.Error as e:
    print(e)

finally:
    if conn:
        conn.close()

import sqlite3

conn = sqlite3.connect(r"D:\w2\Suracha_python\week6.db")
c = conn.cursor()

c.execute('''SELECT * FROM users''')

result = c.fetchmany()
print(result)

import sqlite3

conn = sqlite3.connect(r"D:\w2\Suracha_python\week6.db")
c = conn.cursor()

c.execute('SELECT * FROM users WHERE fname = "ประหยัด"')

result = c.fetchall().
for i in result:
    print(i)

import sqlite3
conn = sqlite3.connect(r"D:\w2\Suracha_python\week6.db")
c = conn.cursor()
c.execute(' DELETE FROM users ')
conn.commit()
c.close()
"""
import sqlite3
conn = sqlite3.connect(r"D:\w2\Suracha_python\week6.db")
try:
    c = conn.cursor()
    data = ('A','A','A')
    c.execute('INSERT INTO users(fname,lname,email) VALUES (?,?,?)',data)
    conn.commit()
    c.close()
except sqlite3.Error as e:
    print(e)

finally:
    if conn:
        conn.close()