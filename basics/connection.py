# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 19:04:14 2020

@author: -
"""
import mysql.connector
myDB=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="asdf567@",
    database="studentDB"
    )
myCursor=myDB.cursor()
# sql="INSERT INTO details (name,age) values(%s,%s)"
# val=[
#      ('Peter',18),
#      ('Max',23),
#      ('Hannah',22),
#      ('Susan',17),
#      ('Richard',22),
#      ('William',34)
#      ]
# #
# # for values in val:
# myCursor.executemany(sql,val)
# myDB.commit()
# print(myCursor.rowcount,"record was inserted")



"""
sql="INSERT INTO details (name,age) values(%s,%s)"
val=("Kol",25)
myCursor.execute(sql,val)
myDB.commit()
print("1 record inserted,ID:",myCursor.lastrowid)
"""

myCursor.execute("SELECT * FROM details")
myresult=myCursor.fetchall()

for x in myresult:
    print(x)
    
"""
# sql="INSERT INTO details(name,age)VALUES(%s,%s)"
# val=("John",21)
# myCursor.execute(sql,val)
# myDB.commit()
# print(myCursor.rowcount,"record inserted")
# myCursor.execute("INSERT INTO details(name,age)VALUES(%s,%s)");

# myCursor.execute("INSERT VALUES INTO TABLE  details(name ,age) VALUES('rayan',21)");
"""
"""
    ->create table and show table
      myCursor.execute("CREATE TABLE details(name VARCHAR(255),age INTEGER(10))")
      
      myCursor.execute("SHOW TABLES")
for tb in myCursor:
    print(tb)
"""
"""
    ->create database 
     myCursor.execute("CREATE DATABASE studentDB")
"""

"""
    -> show the all databases  and print them
    myCursor.execute("SHOW DATABASES")
for  db in myCursor:
    print(db)
"""
