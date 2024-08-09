def fuel_percentage():
    while True:
        try:
            # Prompt user for fraction 
            fraction = input("Fraction: ")
            # Split the fraction by "/"
            fraction_parts = fraction.split("/")

            # Get the value of X and Y 
            x,y = int(fraction_parts[0]), int(fraction_parts[1])

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
            print("Invalid Input")
        except ZeroDivisionError:
            print("Divide by zero isn't allowed")

def main():
    percentage = fuel_percentage()

    # Print E if percentage is 1 or less 
    if percentage <= 1:
        print("E")
    # Print F if percentage is 99 or above 
    elif percentage >= 99:
        print("F")
    else:
        print(f"{percentage}%")

# main()

if __name__ == "__main__":
    main()




