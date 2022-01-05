from typing import Annotated

ConnectionString = Annotated[str, "ODBO Connection String"]

connection_string: ConnectionString = "Driver=QRemote for QuickBooks;DSN=QuickBooks Data 64-Bit QRemote;"
