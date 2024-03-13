'''
Cesar Riascos 
scripy description: config data base 
'''



#Import engine database package
import sqlite3

#Create a database connection (database name)
con = sqlite3.connect('market.db')

#creating cursor object 
cur = con.cursor()

#create user table
user_table = '''
    CREATE TABLE IF NOT EXISTS user 
        (id INTEGER PRIMARY KEY, 
        firtsname TEXT NOT NULL,
        lastname TEXT NOT NULL, 
        ident_number TEXT UNIQUE NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    );
'''

#Execute SQL (Query)
cur.execute(user_table)

#Save changes in database
con.commit()

#print("===== Database market has been created =====")