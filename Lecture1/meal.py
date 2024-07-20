def main():
    time_expression = input("What time it is? ")
    #print(time_expression)
    
    # Call convert function
    hours = convert(time_expression)

    #print(hours)
    # Conditions 
    if 7 <= hours <= 8:
        print("breakfast time")
    elif 12 <= hours <= 13:
        print("lunch time")
    elif 18 <= hours < 19:
        print("dinner time")

def convert(expression):
    # Split by ":"
    expression = expression.split(":")

    # Assign split values to hours and minutes respectively
    hours,minutes = int(expression[0]), int(expression[1])

    minutes = float(minutes/60)

    return hours + minutes

if __name__ == "__main__":
    main()