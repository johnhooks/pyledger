from pathlib import Path
import json
import jsonschema
from stockholm import Money

from .connect import connect

# connect()

path = Path(__file__).parent / ".." / "schema" / "rate-schema.json"
file = open(path, "r")
schema = json.load(file)

data = {"socialSecurityEmployer": "0.062", "socialSecurityEmployee": "0.062",
        "medicareEmployer": "0.0145", "medicareEmployee": "0.0145"}

jsonschema.validate(instance=data, schema=schema)

ssEmployee = Money(data["socialSecurityEmployee"])

print(ssEmployee)
