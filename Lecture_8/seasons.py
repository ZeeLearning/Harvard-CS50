from datetime import date
import sys
import inflect

# Create an inflect engine instance
p = inflect.engine()


def main():
    dob = input("Date of Birth: ").strip()
    try:
        dob_date = parse_date(dob)  # Parse the date to ensure it's valid
    except ValueError:
        sys.exit("Invalid date")

    minutes = calculate_song_minutes(dob_date)  # Calculate minutes using song logic
    print(f"{p.number_to_words(minutes, andword='').replace('-', ' ')} minutes")


def parse_date(dob):
    """Parses and validates a date string in YYYY-MM-DD format."""
    year, month, day = map(int, dob.split("-"))
    return date(year, month, day)


def calculate_song_minutes(dob):
    """
    Calculates the total minutes since the date of birth,
    assuming 525,600 minutes per year (ignoring leap years).
    """
    today = date.today()
    if dob.year == today.year:  # If born in the current year, no full year has passed
        return 0

    years_diff = today.year - dob.year

    # Check if today's date has passed the birthdate in the current year
    if (today.month, today.day) < (dob.month, dob.day):
        years_diff -= 1

    # If exactly one year has passed
    if years_diff == 1:
        return 525600

    return years_diff * 525600  # Total minutes


if __name__ == "__main__":
    main()
