#!/usr/bin/python3
"""script that lists all states with a name starting with
N (upper N) from the database hbtn_0e_0_usa"""

import MySQLdb
import sys

if __name__ == '__main__':

    mydb = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3])

    cursor = mydb.cursor()

    cursor.execute("SELECT *FROM states WHERE BINARY name LIKE 'N%' ORDER BY id ASC")

    states = cursor.fetchall()

    for state in states:
        print(states)

    cursor.close()
    mydb.close()
