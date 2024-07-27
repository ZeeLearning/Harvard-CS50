def snake_case_converter(text):

    # Initialize an empty string, assuming that user provides text in camel case. 
    snake_case = ""

    # Loop through user provided text 
    for char in text:
        # If char is in upper case, convert that to lower case and add "_" before it
        if char.isupper():
            snake_case += "_" + char.lower()
        else:
            snake_case += char
    
    return snake_case

# Get text from user
camel = input("camelCase: ")
# Call function 
snake_case = snake_case_converter(camel)

print(snake_case)

