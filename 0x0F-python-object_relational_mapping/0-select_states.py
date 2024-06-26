#!/usr/bin/python3
""" a script that lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
import sys

if __name__ == "__main__":

    mydb = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3])

    cursor = mydb.cursor()

    cursor.execute("SELECT *FROM states ORDER BY id")

    states = cursor.fetchall()

    for states in states:
        print(states)

    cursor.close()
    mydb.close()
