def expression_calculater(text):

    # Split expression 
    text_parts = text.split()
    
    # Assign text parts to x, y, and z respectively 
    x,y,z = int(text_parts[0]), text_parts[1], int(text_parts[2])

    #print(f"x = {x}, y = {y}, z = {z}")

    # Calculations based on the value of y 
    if y == "+":
        result = x + z 
    elif y == "-":
        result = x - z 
    elif y == "*":
        result = x * z
    else:
        if z == 0:
            raise ZeroDivisionError("Error: Division by 0 isn't allowed.")
        result = x / z

    return f"{result:.1f}"


# Get expression text from user 
expression = input("Expression: ")

try:

    # Call the function to perform calculation based on expression provided by a user
    result = expression_calculater(expression)
    print(result)

except ZeroDivisionError as e:
    print(e)


