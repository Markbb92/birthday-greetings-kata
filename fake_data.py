from faker import Faker
from faker.providers import date_time, internet, person, phone_number

fake = Faker()
fake.add_provider(internet) # Provides the python file, or Module, with the ability to generate random email addresses or numerous other types of addresses per Faker documentation.
fake.add_provider(person) # Provides the python file, or Module, with the ability to generate random names or numerous other types of names per Faker documentation.
fake.add_provider(date_time) # Provides the python file, or Module, with the ability to generate random dates or numerous other types of dates per Faker documentation.
fake.add_provider(phone_number) # Provides the python file, or Module, with the ability to generate random phone numbers or numerous other types of phone numbers per Faker documentation.

with open("input_email.csv", "w") as f:
    f.write("last_name, first_name, date_of_birth, email\n")
    for _ in range(10000):
        f.write(
            f"{fake.last_name()}, {fake.first_name()}, {fake.date_of_birth()}, {fake.email()}\n"
        )


with open("input_sms.csv", "w") as f:
    f.write("last_name, first_name, date_of_birth, phone_number\n")
    for _ in range(10000):
        f.write(
            f"{fake.last_name()}, {fake.first_name()}, {fake.date_of_birth()}, {fake.phone_number()}\n"
        )


with open("input_telegram.csv", "w") as f:
    f.write("last_name, first_name, date_of_birth, telegram\n")
    for _ in range(10000):
        f.write(
            f"{fake.last_name()}, {fake.first_name()}, {fake.date_of_birth()}, {fake.slug()}\n"
        )
