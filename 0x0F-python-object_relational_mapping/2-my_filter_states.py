#!/usr/bin/python3
""" Write a script that takes in an argument and displays all values
    in the states table of hbtn_0e_0_usawhere name matches the argument """
import MySQLdb
import sys


if __name__ == "__main__":
    """ main function"""
    db = MySQLdb.connect(host="localhost", passwd=sys.argv[2],
                         user=sys.argv[1], db=sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute(f"SELECT * FROM states WHERE name = '{sys.argv}'")
    data = cur.fetchall()
    for row in data:
        print(row)
    cur.close()
    db.close()
