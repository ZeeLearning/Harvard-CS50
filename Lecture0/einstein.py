# Get value of Mass from user in kilograms 
mass = int(input("m: "))
# Speed of Light - # of Joules 
sol = int(300000000)

# Calculate Energy 
energy = int(mass * pow(sol, 2))

# Print the result
print(f"E: {energy}")
