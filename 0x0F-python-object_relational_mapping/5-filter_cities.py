#!/usr/bin/python3
"""  script that takes in arguments and displays all values in the
     states table of hbtn_0e_0_usa where name matches the argument. """

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

    cursor.execute("SELECT  cities.name FROM cities \
                    INNER JOIN states ON cities.state_id=states.id \
                     WHERE states.name = %s", [sys.argv[4]])

    states = cursor.fetchall()

    i = ''

    for cities in states:
        i += ','.join(cities) + ', '

    print(i)

    cursor.close()
    mydb.close()
