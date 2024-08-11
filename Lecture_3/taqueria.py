# Menu 
menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

# Intialize the total 
total = 0

try:
    while True:
        item = input("Item: "  )
        if not item in menu:
            continue
        total = total + menu[item]
        print(f"Total: ${format(total, ".2f")}")

# KeyError exception 
except KeyError:
    pass
# EOF error 
except EOFError:
    pass

