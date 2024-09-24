import sys 

def count_lines_of_code(file_path):
    # Try to open the file and handle FileNotFoundError 
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        sys.exit("File does not exist.")

    # Initialize the line counter 
    line_counter = 0

    # Loop through each line in the file. 
    for line in lines:
        # Strip leading and trailing spaces 
        stripped_line = line.strip() 
        # Check line is not blank and is not a comment 
        if stripped_line and not stripped_line.startswith('#'):
            line_counter += 1 
    
    return line_counter

def main():
    # Check if file is provided 
    #print(len(sys.argv))
    if len(sys.argv) == 1:
        sys.exit("Too few command-line arguments")

    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    elif len(sys.argv) == 2:
        file_path = sys.argv[1]
        # check if file is a python file 
        if not file_path.endswith('.py'):
            sys.exit("Not a python file.")

        loc = count_lines_of_code(file_path)

        print(loc)

if __name__ == "__main__":
    main()