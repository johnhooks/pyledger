from pathlib import Path
import jsonschema

from .qodbc import qbcursor
from .jsonloader import jsonloader


def verify_account_list():
    accounts_schema_path = Path(__file__).parent / ".." / "schema" / "accounts-schema.json"
    accounts_schema = jsonloader(accounts_schema_path.resolve())

    accounts_data_path = Path(__file__).parent / ".." / "data" / "accounts.json"
    accounts_data = jsonloader(accounts_data_path.resolve())

    jsonschema.validate(instance=accounts_data, schema=accounts_schema)

    account_list = accounts_data["accounts"]

    ids_list = tuple(map(lambda account: account['ListId'], account_list))

    with qbcursor() as cursor:
        query = "SELECT FullName, ListId from Account WHERE ListId IN {}".format(ids_list)
        cursor.execute(query)

        for row in cursor.fetchall():
            (full_name, list_id) = row
            match = next(item for item in account_list if item["ListId"] == list_id and item["FullName"] == full_name)
            if (not match):
                raise Exception('Required account missing in QuickBooks')
