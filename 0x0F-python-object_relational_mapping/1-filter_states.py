#!/usr/bin/python3
""" Write a script that lists all states with a name
    starting with N (upper N) from the database hbtn_0e_0_usa """
import MySQLdb
import sys


if __name__ == "__main__":
    """ main function"""
    db = MySQLdb.connect(host="localhost", passwd=sys.argv[2],
                         user=sys.argv[1], db=sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id")
    data = cur.fetchall()
    for row in data:
        print(row)
    cur.close()
    db.close()
