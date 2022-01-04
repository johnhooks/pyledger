import pyodbc
from ledger.constants import connection_string

def connect():
    connection = pyodbc.connect(connection_string)
    cursor = connection.cursor()

    cursor.execute("SELECT Top 10 Name FROM Customer")

    for row in cursor.fetchall():
        print(row)

    cursor.close()

    connection.close()
