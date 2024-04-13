#!/usr/bin/python3
""" a script that lists all cities from the database hbtn_0e_4_usa"""

import MySQLdb
import sys

mydb = MySQLdb.connect(host="localhost",
                       port=3306,
                       user=sys.argv[1],
                       passwd=sys.argv[2],
                       db=sys.argv[3])

cursor = mydb.cursor()

cursor.execute("SELECT id, name  FROM cities ORDER BY id")

cities = cursor.fetchall()

for city in cities:
    print(city)

cursor.close()
mydb.close()
