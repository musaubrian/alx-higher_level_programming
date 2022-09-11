#!/usr/bin/env python3

import MySQLdb
import sys


def list_states(username, password, db_name):
    """
    lists all the states in the database
    """
    db = MySQLdb.connect(
            host="localhost",
            user=username,
            passwd=password,
            db=db_name,
            port=3306
            )
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    list_states(username=username, password=password, db_name=db_name)
