# Function to replace spaces with '...' 
def replace_space_with_dots(text):
    # Replace spaces with '...' 
    return text.replace(' ', '...')

# Get input text from user 
user_text = input()

# Call the function 
formatted_text = replace_space_with_dots(user_text)

# Print the result 
print(formatted_text)