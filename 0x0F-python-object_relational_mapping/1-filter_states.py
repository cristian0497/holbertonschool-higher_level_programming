#!/usr/bin/python3
""" Method """
import MySQLdb
from sys import argv


def function():
    """ fenction to query in MySql server db witn name start N"""
    try:
        query = MySQLdb.connect(host='localhost',
                                user=argv[1],
                                passwd=argv[2],
                                db=argv[3],
                                port=3306)
        cur = query.cursor()
        cur.execute("SELECT id, name FROM states WHERE name RLIKE '^N' ORDER BY\
        states.id ASC")
        cur2 = cur.fetchall()
        for result in cur2:
            print(result)

    except:
        pass
if __name__ == '__main__':
    function()
