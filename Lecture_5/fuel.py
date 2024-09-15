def main():
    # Get the fraction from user and convert to percentage
    fraction = input("Fraction: ")
    percentage = convert(fraction)
    
    # Display the fuel level based on percentage
    print(gauge(percentage))

def convert(fraction):
    while True:
        try:
            # Split the fraction by "/"
            fraction_parts = fraction.split("/")

            # Get the value of X and Y
            x, y = int(fraction_parts[0]), int(fraction_parts[1])

            # Check if y isn't zero
            if y == 0:
                raise ZeroDivisionError
            
            # Check if x is greater than y
            if x > y:
                raise ValueError
            
            # Calculate percentage
            percent = (x / y) * 100
            percent = round(percent)

            return percent

        except ValueError:
            print("Invalid input")
            fraction = input("Fraction: ")
        except ZeroDivisionError:
            print("Divide by zero isn't allowed")
            fraction = input("Fraction: ")

def gauge(percentage):
    # Return "E" if percentage is 1 or less
    if percentage <= 1:
        return "E"
    # Return "F" if percentage is 99 or above
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()
