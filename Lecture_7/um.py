import re
import sys

def main():
    print(count(input("Text: ")))

def count(s):

    # Define the pattern 
    pattern = r'\bum\b'

    matches = re.findall(pattern, s, re.IGNORECASE)

    # print(matches)

    return(len(matches))

if __name__ == "__main__":
    main()