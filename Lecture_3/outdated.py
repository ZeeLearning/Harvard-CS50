import datetime

# Months 
month = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def convert_date(d):
    # Format this date 9/8/1636
    try:
        format_date = datetime.datetime.strptime(d, "%m/%d/%Y")
        return format_date.strftime("%Y-%m-%d")
    except ValueError:
        pass 

    # Format this date September 8, 1636
    try:
        format_date = datetime.datetime.strptime(d, "%B %d, %Y")
        return format_date.strftime("%Y-%m-%d")
    except ValueError:
        pass 

while True:
    user_date = input("Date: ")
    # Call function convert_date(d)
    formatted_date = convert_date(user_date)

    if formatted_date:
        print(formatted_date)
        break
    else:
        continue