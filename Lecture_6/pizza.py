import sys
import csv
from tabulate import tabulate

def main():
    if len(sys.argv) == 1:
        sys.exit("Too few command-line argument")

    elif len(sys.argv) > 2:
        sys.exit("Too many command-line argument")
        
    elif len(sys.argv) == 2:
        # Get the filename from command-line arguments
        filename = sys.argv[1]
        
        # Check if the file has a .csv extension
        if not filename.endswith(".csv"):
            sys.exit("Not a CSV file")
        try:
            # Try to open the CSV file
            with open(filename, newline='') as csvfile:
                reader = csv.reader(csvfile)
                # Convert the CSV reader object to a list to pass it to tabulate
                data = [row for row in reader]
                # Print the table using tabulate with the 'grid' format
                print(tabulate(data, headers="firstrow", tablefmt="grid"))
        
        except FileNotFoundError:
            sys.exit("File not found")

if __name__ == "__main__":
    main()
