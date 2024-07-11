# Greeting from user 
greeting = input("Greeting: ")

# Conditional logic 
if greeting.startswith("h") and greeting != "hello":
    print("$20")
elif greeting == "hello":
    print("$0")
else:
    print("$100")