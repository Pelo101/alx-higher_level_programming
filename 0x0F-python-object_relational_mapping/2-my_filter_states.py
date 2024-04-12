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

    name_arg = "SELECT * " \
               "FROM states " \
               "WHERE BINARY name = '{}'  " \
               "ORDER BY id ASC".format(sys.argv[4])

    cursor.execute(name_arg)

    states = cursor.fetchall()

    for row in states:
        print(row)

    cursor.close()
    mydb.close()
