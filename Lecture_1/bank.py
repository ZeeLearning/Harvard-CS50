# Greeting from user 
greeting = input("Greeting: ")

# Apply space and case insensitivity
greeting = greeting.strip().lower()

prize_greeting = "hello"

# Conditional logic 
if greeting == "hello" or "hello" in greeting:
    print("$0")
elif greeting.startswith("h") and greeting != "hello":
    print("$20")
else:
    print("$100")

