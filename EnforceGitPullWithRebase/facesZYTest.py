def convert(text):
    # Replace ":)" with 🙂
    text = text.replace(":)", "🙂")
    
    # Replace ":(" with 🙁
    text = text.replace(":(", "🙁")

    # Replace sad with 🙁
    text = text.replace("sad", "🙁")

    # Replace happy with 🙂
    text = text.replace("happy", "🙂")

    # Replace angry with 😡
    text = text.replace("angry", "😡")

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
