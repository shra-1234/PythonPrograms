import sqlite3
  
connection = sqlite3.connect('myapp.db') # file path
  
# create a cursor object from the cursor class
cur = connection.cursor()
  
# creating a list of items
  
multiple_columns = [(6, 'Pau', 32, 'Caliornia', 30000.00 ),
                    (7, 'Paus', 31, 'Caifornia', 20000.00 ),
                    (8, 'Patu', 30, 'Califrnia', 10000.00 )]
  
cur.executemany("INSERT INTO COMPANY VALUES (?,?,?,?,?)", multiple_columns)
  
# committing our connection
  
print('Command executed successfully!!!')
connection.commit()
  
# close our connection
connection.close()

