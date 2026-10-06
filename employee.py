
class Employee:
    def __init__(self, last_name, first_name, date_of_birth, contact_info):
        self.last_name = last_name
        self.first_name = first_name
        self.date_of_birth = date_of_birth
        self.contact_info = contact_info

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.date_of_birth} - {self.contact_info}"