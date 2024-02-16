#!/usr/bin/python3
"""takes in the name of a state as an argument and
 lists all cities of that state,
 using the database hbtn_0e_4_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         database=sys.argv[3], port=3306)
    cursor = db.cursor()

    cursor.execute("""SELECT cities.name FROM cities
                   JOIN states ON states.id=cities.state_id
                WHERE states.name=%s""", (sys.argv[4],))

    result = cursor.fetchall()
    rows = list(row[0] for row in result)
    print(*rows, sep=", ")

    cursor.close()
    db.close()
