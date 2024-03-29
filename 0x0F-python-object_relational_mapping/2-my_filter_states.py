#!/usr/bin/python3
"""takes in an argument and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument."""

import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)

    cursor = db.cursor()
    cursor.execute(
        "SELECT * FROM states WHERE name LIKE BINARY '{}'"
        .format(sys.argv[4]))
    result = cursor.fetchall()
    for row in result:
        print(row)

    cursor.close()
    db.close()
