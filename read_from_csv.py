from employee import Employee
from datetime import date as dt
import csv

def read_employees_from_csv(path):
    employees = []
    with open (path, newline="") as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            last_name = row[0].strip()
            first_name = row[1].strip()
            date_of_birth = dt.fromisoformat(row[2].strip())
            contact_info = row[3].strip()
            employee = Employee(last_name, first_name, date_of_birth, contact_info)
            employees.append(employee)
    return employees
