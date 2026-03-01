import requests

url = "https://v2.jokeapi.dev/joke/Any"

def get_joke():
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error:\n{response.status_code}")
        return None

def print_joke(data):
    if data['type'] == "single":
        print(f"Category: {data['category']}")
        print(data["joke"])
    else:
        print(f"Category: {data['category']}")
        print(f"{data['setup']}")
        print(f"               {data['delivery']}")

data = get_joke()
print_joke(data)
print(data["jokes"])