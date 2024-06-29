def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # Strip the $ sign 
    d = d.lstrip("$")
    d = float(d)
    print(d)
    return d


def percent_to_float(p):
    # Strip % sign
    p = p.rstrip("%")
    p = float(p)/100
    print(p)
    return p 

main()