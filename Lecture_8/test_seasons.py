from seasons import parse_date, calculate_total_minutes
from datetime import date
import pytest


def test_parse_date_valid():
    assert parse_date("1999-01-01") == date(1999, 1, 1)
    assert parse_date("2000-01-01") == date(2000, 1, 1)


def test_calculate_total_minutes():
    # Adjusting the test cases for expected values with proper date calculations
    today = date.today()

    # Case 1: From Jan 1, 1999
    expected_minutes = ((today - date(1999, 1, 1)).days) * 1440
    assert calculate_total_minutes(date(1999, 1, 1)) == expected_minutes

    # Case 2: From Jan 1, 1998
    expected_minutes = ((today - date(1998, 1, 1)).days) * 1440
    assert calculate_total_minutes(date(1998, 1, 1)) == expected_minutes

    # Case 3: From Jan 1, 2023
    expected_minutes = ((today - date(2023, 1, 1)).days) * 1440
    assert calculate_total_minutes(date(2023, 1, 1)) == expected_minutes

    # Case 4: From Jan 1, 2000
    expected_minutes = ((today - date(2000, 1, 1)).days) * 1440
    assert calculate_total_minutes(date(2000, 1, 1)) == expected_minutes


if __name__ == "__main__":
    pytest.main()
