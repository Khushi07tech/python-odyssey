import requests
import time

base_url = "https://zenquotes.io/api"
def get_quote():
    url = f"{base_url}/random"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()[0]
    else:
        print("It's not you, it's us☹")
        print(f"😖Error: {response.status_code}")
        return None

def fetch_quotes (num_quotes):
    quote_list = []
    for _ in range(num_quotes):
        quote = get_quote()
        if quote:
            quote_list.append(quote)
    return quote_list

def print_quotes(quote):
        print(f"🔮Quote = {quote['q']}")
        print(f"✨Author = {quote['a']}")
        print("🎀✨🎆⭐👑💕" * 5)

def print_quote_list(quote_list, num_quotes):
    for q in quote_list:
        for key, value in q.items():
            if key == "h":
                continue
            else:
                print(f"{key} ~ {value}")
        print ()

    if len(quote_list) != num_quotes:
        print (f"You asked for {num_quotes} quotes but only {len(q)} were provided due to some problem.")

def get_user_input ():
    while True:
        try:
            num_quotes = int(input("Enter the number of quotes: "))
            if num_quotes <= 0 or num_quotes > 100:
                raise ValueError
            return num_quotes
        except ValueError:
            print ("Please enter a valid number between 1-100")

#=========== MAIN FLOW ===========
def main ():
    num_quotes = get_user_input()


    quotes = fetch_quotes(num_quotes)
    for quote in quotes:
        print_quotes(quote)
        time.sleep(2)

    see_quote_list = input("Want to see the quote's list(y/n): ").lower()
    if see_quote_list != "y" and see_quote_list != "n":
        print ("Invalid Input")
    elif see_quote_list == "n":
        print ("OKIEE!🎀")
    else:
        print_quote_list(quotes, num_quotes)

if __name__ == '__main__':
    main()