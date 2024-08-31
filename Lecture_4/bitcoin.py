import sys
import requests

def get_bitcoin_price():
    try:
        # Make a request to api
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

        # Parse the json response 
        data = response.json()

        #print(data)

        # Extract the current price of bitcoin
        return float(data['bpi']['USD']['rate'].replace(',', ''))

    except requests.RequestException:
        sys.exit("Invalid response.")


def main():
    # Check user provides one and only one argument. 
    if len(sys.argv) == 2:
        #print(f"Length of command-line argument: {len(sys.argv)}")
        
        # Convert argument to float.
        try:
            num_bitcoins = float(sys.argv[1])

        except ValueError:
            sys.exit("command-line argument is not a number")

        # Call the function 
        bitcoin_price = get_bitcoin_price()
        # Total amount
        amount = num_bitcoins * bitcoin_price

        print(f"${amount:,.4f}")

    else:
        sys.exit("Missing command-line argument")


if __name__ == "__main__":
    main()
