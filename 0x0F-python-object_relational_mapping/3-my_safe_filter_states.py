#!/usr/bin/python3
import MySQLdb
import sys
""" script that takes in arguments and displays
all values in the states table of hbtn_0e_0_usa
where name matches the argument. But this time,
write one that is safe from MySQL injections!"""

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)

    cursor = db.cursor()

    cursor.execute(
        f"SELECT * FROM states WHERE name LIKE BINARY %s", (sys.argv[4], ))
    result = cursor.fetchall()
    for row in result:
        print(row)

    cursor.close()
    db.close()
