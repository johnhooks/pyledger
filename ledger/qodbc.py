from contextlib import contextmanager
from collections.abc import Iterator
from pyodbc import connect, Cursor
from .constants import connection_string

@contextmanager
def qbcursor() -> Iterator[Cursor]:
    """Aquire odbc curser to QODBC QuickBooks.
    """
    connection = connect(connection_string)
    cursor = connection.cursor()
    try:
        yield cursor
    finally:
        cursor.close()
        connection.close()
