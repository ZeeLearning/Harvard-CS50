import re
import sys

def main():
     
     print(convert(input("Hours: ")))

def convert(s):
    # Define the regular expression pattern to match valid formats
    pattern = r"^(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)$"
    match = re.match(pattern, s)
    
    if not match:
        # If the input doesn't match any of the expected formats, raise a ValueError
        raise ValueError
    
    # Extract the components of the start time and end time
    start_hour, start_minute, start_period, end_hour, end_minute, end_period = match.groups()
    
    # Default minute to "00" if it's not provided
    start_minute = start_minute or "00"
    end_minute = end_minute or "00"
    
    # Convert extracted values to integers for hour and minute
    start_hour = int(start_hour)
    start_minute = int(start_minute)
    end_hour = int(end_hour)
    end_minute = int(end_minute)
    
    # Validate the hour and minute values
    if not (1 <= start_hour <= 12 and 0 <= start_minute < 60):
        raise ValueError
    if not (1 <= end_hour <= 12 and 0 <= end_minute < 60):
        raise ValueError
    
    # Convert start time to 24-hour format
    start_24 = to_24_hour_format(start_hour, start_minute, start_period)
    
    # Convert end time to 24-hour format
    end_24 = to_24_hour_format(end_hour, end_minute, end_period)
    
    # Return the formatted result
    return f"{start_24} to {end_24}"

def to_24_hour_format(hour, minute, period):
    """Convert 12-hour format to 24-hour format."""
    if period == "PM" and hour != 12:
        hour += 12
    elif period == "AM" and hour == 12:
        hour = 0
    
    return f"{hour:02}:{minute:02}"

if __name__ == "__main__":
    main()
