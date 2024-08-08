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
        print(f"Amount Due: {cost}")
        break

    if total_amount >= 50:
        changed_owed = total_amount - cost

        print(f"Change Owed: {changed_owed}")