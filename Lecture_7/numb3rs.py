import re
import sys

def main():
    # Prompt user for an IPv4 address and validate it
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    # Regular expression for matching a valid IPv4 address
    pattern = r"^([0-9]{1,3}\.){3}[0-9]{1,3}$"
    
    # Check if the input matches the general structure of an IPv4 address
    if re.match(pattern, ip):
        # Split the IP into its four components
        octets = ip.split(".")
        
        # Check each part is between 0 and 255 and doesn't have leading zeros
        for octet in octets:
            if not 0 <= int(octet) <= 255 or (octet != "0" and octet.startswith("0")):
                return False
        return True
    return False

if __name__ == "__main__":
    main()
