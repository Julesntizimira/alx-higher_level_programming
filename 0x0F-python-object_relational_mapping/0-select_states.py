#!/usr/bin/python3

import mysql.connector

conn = mysql.connector.connect(
        host='localhost',
        port='3306',
        user='root',
        password='Gitarama@088',
        database='hbtn_0e_0_usa'
        )
cursor = conn.cursor()
cursor.execute("SELECT id, name FROM states GROUP BY id ORDER BY id")
for table in cursor:
    print(table)
