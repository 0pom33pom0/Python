import sqlite3
conn = sqlite3.connect(r"D:\w2\Suracha_python\w6\ex6.db")
c = conn.cursor()
c.execute('''CREATE TABLE pom (id integer PRIMARY KEY AUTOINCREMENT,
    name  varchar(60)  NOT NULL,
    email varchar(100) NOT NULL,
    sex   varchar(5)   NOT NULL,
    age   varchar(5)   NOT NULL,
    year  varchar(2)   NOT NULL)''')
conn.commit()
conn.close()
