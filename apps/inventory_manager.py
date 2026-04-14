import csv

file_path = "inventory.csv"

def load_from_csv():
    inventory = []
    try:
        with open(file_path, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                item = row[0]
                qty = int(row[1])
                inventory.append([item, qty])
    except FileNotFoundError:
        pass
    return inventory

def save_to_csv(inventory):
    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file)
        for row in inventory:
            writer.writerow(row)

def select_option():
    print("== INVENTORY MANAGER ==")
    print("1. See inventory")
    print("2. Update stock")
    print("3. New item")
    print("4. Check if <3 units")
    print("5. Quit")

def validate_user_option():
    try:
        user_option = input("Option(1-5): ")
        if not user_option.isdigit():
            raise ValueError
        else:
            return user_option
    except ValueError:
        print("Invalid value")
    except Exception as e:
        print(f"Error: {e}")

def see_inventory():
    print("============================")
    print("====== INVENTORY ======")
    try:
        with open(file_path, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                print(f"{row[0].capitalize():<15} : {row[1]}")
    except FileNotFoundError:
        print("File not found")
    print("============================")

def update_stock(inventory):
    user_item = input("Item: ").strip().lower()
    for item in inventory:
        if item[0] == user_item:
            try:
                user_quantity = int(input("Qty: "))

                if user_quantity < 0:
                    print("Qty can't be negative")
                else:
                    item[1] = user_quantity
                    save_to_csv(inventory)
                    print("Updated!")
                return
            except ValueError:
                print("Invalid input")
                return
    else:
        print("Item not in inventory")

def new_item(inventory):
    user_new_item = input("New Item: ").strip().lower()
    for item in inventory:
        if item[0] == user_new_item:
            print("Item already in inventory")
            return
    try:
        user_new_qty = int(input("Qty: "))
        if user_new_qty < 0:
            print("Qty can't be negative")
        else:
            inventory.append([user_new_item, user_new_qty])
            save_to_csv(inventory)
            print("Added!")
    except ValueError:
        print("Invalid input")

def check_3_units(inventory):
    print("=============================")
    print("Need to be restocked")
    for item in inventory:
        if item[1] < 3:
            print(f"{item[0]} : {item[1]}")
    print("=============================")


inventory = load_from_csv()

if not inventory:
    inventory = [["apples", 10],
                 ["bananas", 2],
                 ["mangoes", 15],
                 ["peaches", 1],
                 ["pomegranates", 9]]
    save_to_csv(inventory)


select_option()

while True:
    selected_option = validate_user_option()

    if selected_option is None:
        continue

    if selected_option == "1":
        see_inventory()

    elif selected_option == "2":
        update_stock(inventory)

    elif selected_option == "3":
        new_item(inventory)

    elif selected_option == "4":
        check_3_units(inventory)

    elif selected_option == "5":
        break