'''
Suppose that a machine sells bottles of Coca-Cola (Coke) for 50 cents and only accepts coins in these denominations: 
25 cents, 10 cents, and 5 cents.

In a file called coke.py, implement a program that prompts the user to insert a coin, one at a time, 
each time informing the user of the amount due. Once the user has inputted at least 50 cents, 
output how many cents in change the user is owed. Assume that the user will only input integers, 
and ignore any integer that isn’t an accepted denomination.
'''

# Accepted denomications 
accepted_coins = [25,10,5]
# Total cost of coke 
cost = 50 
# Inserted Amount 
total_amount = 0

while total_amount < cost:

    amount_due = cost - total_amount
    # Print amount due 
    print(f"Amount Due: {amount_due}")

    # Prompt user to insert coin 
    coin = int(input("Insert Coin: "))

    # Check if inserted coin is in accepted denomication 
    if coin in accepted_coins:
        total_amount += coin 
    else:
        break

    if total_amount >= 50:
        changed_owed = total_amount - cost

        print(f"Change Owed: {changed_owed}")