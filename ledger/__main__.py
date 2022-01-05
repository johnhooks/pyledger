from pathlib import Path
import jsonschema
from stockholm import Money
from stockholm.currency import USD

from .connect import qodbc_cursor
from .jsonloader import jsonloader

with qodbc_cursor() as cursor:
    cursor.execute("SELECT * FROM Check WHERE TxnDate >= {d '2022-01-04'}")

    for row in cursor.fetchall():
        print(row)

# connect_qodbc()

rate_schema_path = Path(__file__).parent / ".." / "schema" / "rate-schema.json"
rate_schema = jsonloader(rate_schema_path.resolve())

rate_data_path = Path(__file__).parent / ".." / "data" / "tax-rates-2022.json"
rate_data = jsonloader(rate_data_path.resolve())

jsonschema.validate(instance=rate_data, schema=rate_schema)

ss_employer_rate = Money(rate_data["federal"]["socialSecurityEmployer"])
ss_employee_rate = Money(rate_data["federal"]["socialSecurityEmployee"])
med_employer_rate = Money(rate_data["federal"]["medicareEmployer"])
med_employee_rate = Money(rate_data["federal"]["medicareEmployee"])

payroll_amount = Money(6750, USD)

ss_employer_amount = ss_employer_rate * payroll_amount
ss_employee_amount = ss_employee_rate * payroll_amount

med_employer_amount = med_employer_rate * payroll_amount
med_employee_amount = med_employee_rate * payroll_amount

print(f"ss employer: {ss_employer_amount:.2f}")
print(f"ss employee: {ss_employee_amount:.2f}")
print(f"med employer: {med_employer_amount:.2f}")
print(f"med employee: {med_employee_amount:.2f}")
