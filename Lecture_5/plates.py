def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # All vanity plates must start with at least two letters.
    #print(s[0:2])
    if not s[0:2].isalpha():
        return False
    
    # Vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.
    if not (2 <= len(s) <= 6):
        return False
    
    # No periods, spaces, or punctuation marks are allowed.
    if not s[0:1].isalnum():
        return False
    
    # Numbers cannot be used in the middle of a plate; they must come at the end. 
    # For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. 

    num_found = False
    for i, char in enumerate(s):
        #print(f"i, {i}")
        #print(f"char, {char}")
        if char.isdigit():
            # The first number used cannot be '0'
            if char == '0' and not num_found:
                return False  
            num_found = True
        elif num_found:
             # A letter after a number is not allowed
            return False 
        
    return True
    
if __name__ == "__main__":
    main()


        
