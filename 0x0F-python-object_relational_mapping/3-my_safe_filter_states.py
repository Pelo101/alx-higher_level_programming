#!/usr/bin/python3
"""  script that takes in arguments and displays all values in the
     states table of hbtn_0e_0_usa where name matches the argument. """

import sys
import MySQLdb

mydb = MySQLdb.connect(
    host="localhost",
    port=3306,
    user=sys.argv[1],
    passwd=sys.argv[2],
    db=sys.argv[3])

cursor = mydb.cursor()

state_name = (sys.argv[4],)

query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"

cursor.execute(query, (state_name,))

states = cursor.fetchall()

for row in states:
    print(row)


cursor.close()
mydb.close()
