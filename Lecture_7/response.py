import validators

def main():
    email = input("What's your email address? ")

    # Call the validate_email function and print the result
    print(validate_email(email))

def validate_email(e):
    # Use validators.email to check if the email is valid
    if validators.email(e):
        return "Valid"
    else:
        return "Invalid"

if __name__ == "__main__":
    main()
