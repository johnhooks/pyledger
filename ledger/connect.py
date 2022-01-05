import pyodbc
from .constants import connection_string

def connect_qodbc():
    connection = pyodbc.connect(connection_string)
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM Check WHERE TxnDate >= {d '2022-01-04'}")

    for row in cursor.fetchall():
        print(row)

    cursor.close()

    connection.close()
