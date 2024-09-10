def main():
    # Prompt user to enter a text 
    user_text = str(input("Input: "))
    word_no_vowels = shorten(user_text)

    print(f"Output: {word_no_vowels}")

def shorten(word):
    # List of Vowels
    vowels = ['A','E','I','O','U','a','e','i','o','u']
    # Define an empty string 
    output_text = ""

    # Loop through word
    for char in word:
        # Check if character is in list of vowels 
        if char in vowels:
            # Omitt the character
            output_text += ''
        else:
            output_text += char

        #print(f"Output: {output_text}")
    return output_text
    
if __name__ == "__main__":
    main()
