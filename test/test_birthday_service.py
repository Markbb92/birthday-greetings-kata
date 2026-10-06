from datetime import date

from freezegun import freeze_time

from birthday_service import is_leap, is_today, send_greetings
from employee import Employee


# leap-year test

def test_is_leap_regular_leap_year():
    assert is_leap(2024) is True

def test_is_leap_non_leap_year():
    assert is_leap(2026) is False

def test_is_leap_century_not_leap():
    assert is_leap(2100) is False

def test_is_leap_400_year_is_leap():
    assert is_leap(2000) is True


# Current Date Tests

@freeze_time("2026-09-20")
def test_is_today_matches_month_and_day():
    assert is_today(date(2014, 9, 20)) is True

@freeze_time("2026-09-20")
def test_is_today_ignores_birth_year():
    assert is_today(date(1950, 9, 20)) is True

@freeze_time("2026-09-20")
def test_is_today_false_on_different_day():
    assert is_today(date(2014, 9, 21)) is False

@freeze_time("2026-09-20")
def test_is_today_false_on_different_month():
    assert is_today(date(2014, 10, 20)) is False

@freeze_time("2026-02-28")  # 2026 is not a leap year
def test_feb_29_birthday_greeted_on_feb_28_in_non_leap_year():
    assert is_today(date(2000, 2, 29)) is True

@freeze_time("2024-02-28")  # 2024 is a leap year
def test_feb_29_birthday_not_greeted_on_feb_28_in_leap_year():
    assert is_today(date(2000, 2, 29)) is False

@freeze_time("2024-02-29")
def test_feb_29_birthday_greeted_on_feb_29_in_leap_year():
    assert is_today(date(2000, 2, 29)) is True


# greetings sent checks

@freeze_time("2026-09-20")
def test_send_greetings_only_delivers_to_birthday_people():
    employees = [
        Employee("Bradley", "Marcus", date(2014, 9, 20), "marcus@example.com"),
        Employee("Doe", "John", date(1982, 10, 8), "john@example.com"),
    ]
    delivered = []

    def fake_get_employees():
        return employees

    def fake_deliver(contact_info, message):
        delivered.append((contact_info, message))

    send_greetings(fake_get_employees, fake_deliver)

    assert delivered == [("marcus@example.com", "Happy Birthday!")]