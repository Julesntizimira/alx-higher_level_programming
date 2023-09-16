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
            username=argv[1],
            password=argv[2],
            db=argv[3]
            )
    cursor = db.cursor()
    cursor.execute(""" SELECT cities.id, states.name, cities.name
                       FROM cities
                       INNER JOIN states
                       WHERE states.id = cities.state_id
                       ORDER BY cities.id""")
    rows = cursor.fetchall()
    for r in rows:
        print(r)
    cursor.close()
    db.close()