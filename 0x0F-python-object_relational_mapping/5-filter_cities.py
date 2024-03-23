#!/usr/bin/python3
"""  Write a script that takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute("""Select cities.name  from cities inner join states
                 on cities.state_id= states.id
                 where states.name=%s""", (sys.argv[4], ))
    rows = cur.fetchall()
    ls = list(row[0] for row in rows)
    print(*ls, sep=", ")
    cur.close()
    db.close()
