from pathlib import Path
from typing import Any, Dict, List
import jsonschema

from .jsonloader import jsonloader
from .qodbc import qbcursor

class Account():
    """A ledger account.
    """
    name: str
    list_id: str
    type: str

    def __init__(self, list_id: str, name: str,  type: str):
        self.list_id = list_id
        self.name = name
        self.type = type

    def __eq__(self, other):
        if not isinstance(other, Account):
            # don't attempt to compare against unrelated types
            return NotImplemented

        return self.list_id == other.list_id and self.name == other.name and self.type == other.type

    def __repr__(self):
        return 'Account("%s", "%s", "%s")' % (self.list_id, self.name, self.type)


def load() -> Dict[str, Account]:
    accounts_schema_path = Path(__file__).parent / ".." / "schema" / "accounts-schema.json"
    accounts_schema = jsonloader(accounts_schema_path.resolve())

    accounts_data_path = Path(__file__).parent / ".." / "data" / "accounts.json"
    accounts_data = jsonloader(accounts_data_path.resolve())

    jsonschema.validate(instance=accounts_data, schema=accounts_schema)

    accounts: Dict[Account] = {}

    for data in accounts_data["accounts"]:
        key = data['list_id']
        accounts[key] = Account(**data)

    return accounts

def verify(accounts: Dict[str, Account]) -> None:
    ids = tuple(map(lambda account: account.list_id, accounts.values()))

    with qbcursor() as cursor:
        query = "SELECT ListId, Name, AccountType from Account WHERE ListId IN {}".format(ids)
        cursor.execute(query)

        for (list_id, name, type) in cursor.fetchall():
            stored = accounts[list_id]
            loaded =  Account(list_id, name, type)
            if list_id in accounts and loaded == stored:
                continue
            raise Exception(f"Accounts don't match {loaded} {stored}")
