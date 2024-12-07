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

    minutes = calculate_total_minutes(dob_date)  # Calculate total minutes accurately
    # Convert number to words and capitalize only the first word
    words = p.number_to_words(minutes, andword="")
    words = words[0].upper() + words[1:]  # Capitalize the first letter
    print(f"{words} minutes")


def parse_date(dob):
    """Parses and validates a date string in YYYY-MM-DD format."""
    year, month, day = map(int, dob.split("-"))
    return date(year, month, day)


def calculate_total_minutes(dob):
    """
    Calculates the total minutes from the date of birth to today,
    considering leap years.
    """
    today = date.today()
    days_difference = (today - dob).days  # Get total days difference
    return days_difference * 1440  # Convert days to minutes (1440 minutes in a day)


if __name__ == "__main__":
    main()
