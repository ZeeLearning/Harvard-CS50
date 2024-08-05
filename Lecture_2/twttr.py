# List of Vowels
vowels = ['A','E','I','O','U','a','e','i','o','u']
# Prompt user to enter a text 
user_text = str(input("Input: "))
# Define an empty string 
output_text = ""

# Loop through text entered by user
for char in user_text:
    # Check if character is in list of vowels 
    if char in vowels:
        # Omitt the character
        output_text += ''
    else:
        output_text += char

print(f"Output: {output_text}")
