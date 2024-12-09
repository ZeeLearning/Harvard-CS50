def convert(text):
    # Replace ":)" with 🙂
    text = text.replace(":)", "🙂")
    
    # Replace ":(" with 🙁
    text = text.replace(":(", "🙁")

    text = text.replace("happy", "🙂")

    return text 

def main():
    # Get input from user 
    user_text = input('Please enter text: ')
    # Call convert function 
    converted_text = convert(user_text)
    # Print the result 
    print(converted_text)

# Call main 
if __name__ == "__main__":
    main()
