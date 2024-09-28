import csv
import sys

def main():
    # Check for the correct number of command-line arguments
    if len(sys.argv) <= 2:
        sys.exit("Too few command-line argument")
    
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line argument")

    elif len(sys.argv) == 3:
        # Get both files 
        input_file = sys.argv[1]
        output_file = sys.argv[2]

        try:
            # Open and read the input CSV file
            with open(input_file, mode='r', newline='') as infile:
                reader = csv.DictReader(infile)
                # Create a list to store processed rows
                rows = []
                
                # Process each row from input CSV
                for row in reader:
                    # Split the 'name' field into first and last names
                    first, last = row['name'].split(", ")[1], row['name'].split(", ")[0]
                    house = row['house']
                    rows.append({"first": first, "last": last, "house": house})

            # Open the output CSV file for writing
            with open(output_file, mode='w', newline='') as outfile:
                writer = csv.DictWriter(outfile, fieldnames=["first", "last", "house"])
                writer.writeheader()  # Write the header row
                writer.writerows(rows)  # Write the processed rows

        except FileNotFoundError:
            sys.exit(f"Could not read {input_file}")

if __name__ == "__main__":
    main()
