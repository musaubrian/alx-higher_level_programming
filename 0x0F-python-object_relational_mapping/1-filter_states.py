#!/usr/bin/env python3

import sys
import MySQLdb


def filter_states(username, password, db_name):
    """
    lists states starting with `N`
    """
    db = MySQLdb.Connect(
            host="localhost",
            user=username,
            passwd=password,
            db=db_name,
            port=3306
            )
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states\
                   WHERE name LIKE 'N%' ORDER BY id ASC")
    rows = cursor.fetchall()
    for row in rows:
        if row[1][0] == "N":
            print(row)
    cursor.close()
    db.close()


if __name__ == "__main__":
    username = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]
    filter_states(username=username, password=passwd, db_name=db_name)
