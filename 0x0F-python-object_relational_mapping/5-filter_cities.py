#!/usr/bin/python3
'''
Write a script that lists all cities from the database hbtn_0e_4_usa
'''
import MySQLdb
from sys import argv

if __name__ == '__main__':
    db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3]
            )
    cursor = db.cursor()
    st_name = argv[4]
    cursor.execute(""" SELECT cities.name
                       FROM states
                       INNER JOIN cities
                       ON states.id = cities.state_id
                       WHERE states.name LIKE %s
                       ORDER BY cities.id """, (st_name,))
    rows = cursor.fetchall()
    for r in rows:
        print(r[0], end="")
        if r != rows[-1]:
            print(", ", end="")
        else:
            print()
    cursor.close()
    db.close()
