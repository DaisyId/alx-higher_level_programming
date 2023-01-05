#!/usr/bin/python3
"""
    Displays valies with name matches, injection resistant
"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], charset="utf8")

    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    rows = cur.fetchall()

    for row in rows:
        if row[1] == sys.argv[4]:
            print(row)

    cur.close()
    db.close()
