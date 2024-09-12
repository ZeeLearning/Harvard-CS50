def main():
    greeting_message = input("Greeting: ")

    result = value(greeting_message)

    print(f"${result}")

def value(greeting):
    greeting_prize = [0, 20, 100]
    greeting = greeting.strip().lower()
    
    if greeting == "hello" or "hello" in greeting:
        return greeting_prize[0]
    
    elif greeting.startswith("h") and greeting != "hello":
        return greeting_prize[1]
    
    else: 
        return greeting_prize[2]
    
if __name__ == "__main__":
    main()