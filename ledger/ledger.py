from pathlib import Path
from typing import Any, Dict, List
from dataclasses import dataclass
import jsonschema

from ledger.accounts import Account
from ledger.tax import Tax
from ledger.jsonloader import jsonloader
from ledger.qodbc import qbcursor


program_schema_path = Path(__file__).parent / ".." / "schema" / "program-schema.json"
program_schema = jsonloader(program_schema_path.resolve())


class AccountNotFound(Exception):
    pass


@dataclass
class ProgramData:
    """Class for holding the ledger program data."""
    accounts: Dict[str, Account]
    taxes: List[Tax]


def load(path: str) -> ProgramData:
    json_data = jsonloader(path)

    jsonschema.validate(instance=json_data, schema=program_schema)

    accounts: Dict[Account] = {}
    taxes: List[Tax] = map(lambda data: Tax(**data), json_data["taxes"])

    for data in json_data["accounts"]:
        key = data['list_id']
        accounts[key] = Account(**data)

    return ProgramData(accounts=accounts, taxes=taxes)


def verify():
    pass

def _verify_accounts(accounts: Dict[str, Account]) -> None:
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
