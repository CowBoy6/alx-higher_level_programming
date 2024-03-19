import MySQLdb
import sys
A = sys.argv
db=MySQLdb.connect(host='localhost',user=str(A[1]), port=3306,passwd=str(A[2]),db=str(A[3]))