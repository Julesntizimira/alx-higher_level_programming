#!/usr/bin/python3
'''
a script that lists all states from the database hbtn_0e_0_usa
'''
import MySQLdb


conn = MySQLdb.connect(
        host='localhost',
        port='3306',
        user='root',
        password='Gitarama@088',
        database='hbtn_0e_0_usa'
        )
cursor = conn.cursor()
cursor.execute("SELECT * FROM states ORDER BY states.id")

if __name__ == '__main__':
    for table in cursor:
        print(table)
