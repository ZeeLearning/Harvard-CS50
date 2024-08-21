import inflect

# Initialize an empty list 
names = []

eng = inflect.engine()

try:
    while True:
        name = input("Name: ")
        names.append(name)
except EOFError:
    pass 

# Use join to Inflect to format names.
message = eng.join(names)

# Print message with Adieu format
print(f"Adieu, adieu, to {message}")

