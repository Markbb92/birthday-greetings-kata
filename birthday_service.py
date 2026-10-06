from datetime import date

def is_leap(year):
    return((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0))

def is_today(date_of_birth):
    today = date.today()
    if (today.month == date_of_birth.month and today.day == date_of_birth.day):
        return True
    elif((today.month == 2 and today.day == 28) and (date_of_birth.month == 2 and date_of_birth.day == 29) and (is_leap(today.year) != True)):
        return True
    else:
        return False
        
def send_greetings(get_employees, deliver):
    employees = get_employees()
    for employee in employees:
        if is_today(employee.date_of_birth):
            deliver(employee.contact_info, "Happy Birthday!")

