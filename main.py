from read_from_csv import read_employees_from_csv
from birthday_service import send_greetings
from send_via_console import send_via_console

def get_employees_from_input_csv():
    return read_employees_from_csv("input.csv")

send_greetings(get_employees_from_input_csv,send_via_console)