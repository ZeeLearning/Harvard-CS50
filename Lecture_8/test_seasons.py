from seasons import parse_date, calculate_song_minutes
from datetime import date
import pytest


def test_parse_date_valid():
    assert parse_date("1999-01-01") == date(1999, 1, 1)
    assert parse_date("2000-01-01") == date(2000, 1, 1)


def test_parse_date_invalid():
    with pytest.raises(ValueError):
        parse_date("2000/01/01")
    with pytest.raises(ValueError):
        parse_date("01-01-2000")
    with pytest.raises(ValueError):
        parse_date("invalid-date")


def test_calculate_song_minutes():
    assert calculate_song_minutes(date(1999, 1, 1)) == 525600  # 1 year
    assert calculate_song_minutes(date(1998, 1, 1)) == 1051200  # 2 years
    assert calculate_song_minutes(date(2023, 1, 1)) == 0  # Less than 1 year
    assert calculate_song_minutes(date(2000, 1, 1)) == 525600  # 1 year


if __name__ == "__main__":
    pytest.main()
