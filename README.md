# ledger

Quickbooks QODBO Accounting Tools

## QODBC

### QuickBooks Data Schema

[QODBC QuickBooks Interfaces USA](https://doc.qodbc.com/qodbc/usa/)

### QODBC Function List

[SQL Driver Function List](https://support.flexquarters.com/esupport/index.php?/Knowledgebase/Article/View/2343)

### Basic Python Example

[Example from QODBC](https://support.flexquarters.com/esupport/index.php?/Knowledgebase/Article/View/2738/0/qodbc-desktop-how-to-connect-to-qodbc-using-python)

```python
import pyodbc

# ODBO Connection String for connecting to a QODBC QRemote Server on a 64-Bit Machine.
connection_string = "Driver=QRemote for QuickBooks;DSN=QuickBooks Data 64-Bit QRemote;"

connection = pyodbc.connect(connection_string)
cursor = connection.cursor()

cursor.execute("SELECT Top 10 Name FROM Account")

for row in cursor.fetchall():
    print(row)

cursor.close()
connection.close()
```

### Changes to the basic configuration

- Change the IP Address to `127.0.0.1`
- **Did not change the default encryption password**

    I had problems when I did. I had to follow the steps in *Solution 2* under this [QODBC Knowledgebase post](https://support.flexquarters.com/esupport/index.php?/Knowledgebase/Article/View/2642/0/qodbc-desktop-troubleshooting---getting-wrong-client-encyptkey-setting-error) to get everything working.


### Date Comparision

- [Date Comparison SQL](https://stackoverflow.com/questions/25551628/trouble-with-qodbc-sql)
- [QODBC Knowledgebase - How are dates formatted in SQL queries](https://support.flexquarters.com/esupport/index.php?/Default/Knowledgebase/Article/View/2203/50/how-are-dates-formatted-in-sql-queries-when-using-the-quickbooks-generated-time-stamps)


### Create General Journal Entries

[QODBC Knowledgebase - How to create Journal Entries using QODBC](https://support.flexquarters.com/esupport/index.php?/Knowledgebase/Article/View/1618/0/qodbc-desktop-how-to-create-journal-entries-using-qodbc)

## Python Notes

### Standard Packages Used

- [datetime](https://docs.python.org/3/library/datetime.html)
- [decimal](https://docs.python.org/3/library/decimal.html)
- [pathlib](https://docs.python.org/3/library/pathlib.html)

    Example of creating a path relative to the current file

    ```python
    path = Path(__file__).parent / ".." / "dir" / "file.ext"
    path.resolve() # Will resolve the ".."
    ```

### 3rd Party Packages Used

- [stockholm](https://github.com/kalaspuff/stockholm)

    When using advanced string formatting, there can not be space at the end of the curly braces.

    ```python
    print(f"{money:.2f }") # This will throw "ValueError: Invalid format specifier"
    print(f"{money:.2f}")
    ```

- [jsonschema](https://github.com/Julian/jsonschema)
