# Initialize an empty dictionary 
grocery = {}

try:
    while True:
        grocery_item = input()

        # Check if item is already in dictionary, then increments its count by 1 
        if grocery_item in grocery:
            grocery[grocery_item] += 1
        else:
            grocery[grocery_item] = 1
    
except EOFError:
    pass

# print(grocery)

for item in sorted(grocery):
    print(grocery[item], item.upper())
