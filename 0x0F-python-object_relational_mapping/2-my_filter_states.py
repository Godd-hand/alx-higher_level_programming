#!/usr/bin/python3


import MySQLdb
from sys import argv

<<<<<<< HEAD
'''
Script that lists all states from the database
'''
if __name__ == "__main__":
    cont = MySQLdb.connect(
        host="localhost", port=3306, user=argv[1],
        password=argv[2], database=argv[3])
    cursor = cont.cursor()
    cursor.execute(
            "SELECT * FROM states WHERE name LIKE"
            " '{:s}' ORDER BY id ASC".format(argv[4]))
    db = cursor.fetchall()
    for i in db:
        if i[1] == argv[4]:
            print(i)

=======
if __name__ == '__main__':
    list_with_name()
>>>>>>> b92ef454510af544579b6866effc72ab035fced1
