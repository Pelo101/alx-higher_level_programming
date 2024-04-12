#!/usr/bin/python3
"""  script that takes in an argument and displays all values in the
     states table of hbtn_0e_0_usa where name matches the argument."""

import sys
import MySQLdb

if __name__ == "__main__":

    mydb = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3])

    cursor = mydb.cursor()

    query = "SELECT * FROM states WHERE name LIKE BINARY %s"

    state_name  = (sys.argv[4],)

    cursor.execute(query, (state_name))

    states = cursor.fetchall()

    for row in states:
        print(row)

    cursor.close()
    mydb.close()
