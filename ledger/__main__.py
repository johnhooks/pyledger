from pathlib import Path
import json
import jsonschema
from stockholm import Money

from .connect import connect

# connect()

rate_schema_path = Path(__file__).parent / ".." / "schema" / "rate-schema.json"
rate_schema_file = open(rate_schema_path, "r")
rate_schema = json.load(rate_schema_file)

rate_data_path = Path(__file__).parent / ".." / "data" / "tax-rates-2022.json"
rate_data_file = open(rate_data_path, "r")
rate_data = json.load(rate_data_file)

jsonschema.validate(instance=rate_data, schema=rate_schema)

ssEmployee = Money(rate_data["federal"]["socialSecurityEmployee"])

print(ssEmployee)
