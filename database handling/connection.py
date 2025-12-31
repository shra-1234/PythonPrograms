import sqlite3
conn=sqlite3.connect("myapp.db")
print('opened the db')

conn.execute("""
            CREATE TABLE COMPANY
            ( ID INT PRIMARY KEY NOT NULL,
             NAME TEXT NOT NULL,
             AGE INT NOT NULL,
             ADDRESS CHAR(50),
             SALARY INT)""")

print("Table created successfully");

conn.close()
