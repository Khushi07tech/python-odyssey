inventory = {"apples": 10,
            "bananas" : 2,
            "mangoes" : 15,
            "peaches" : 1,
            "pomegranates" : 9}

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
    print("== INVENTORY ==")
    for key, value in inventory.items():
        print(f"{key} : {value}")
    print("============================")

def update_stock(inventory):
    user_item = input("Item: ").strip().lower()
    if user_item in inventory:
        user_quantity = int(input("Qty: "))
        if user_quantity < 0:
            print("Qty can't be negative")
        else:
            inventory.update({user_item : user_quantity})
            print("Updated!")
    else:
        print("Item not in inventory")

def new_item():
    user_new_item = input("New Item: ").strip().lower()
    if not user_new_item in inventory:
        user_new_qty = int(input("Qty: "))
        if user_new_qty < 0:
            print("Qty can't be negative")
        else:
            inventory[user_new_item] = user_new_qty
            print("Added!")
    else:
        print("Item already in inventory")

def check_3_units():
    print("=============================")
    print("Need to be restocked")
    for key, value in inventory.items():
        if value < 3:
            print(f"{key} : {value}")
    print("=============================")

select_option()
while True:
    selected_option = validate_user_option()

    if selected_option == "1":
        see_inventory()

    elif selected_option == "2":
        update_stock(inventory)

    elif selected_option == "3":
        new_item()

    elif selected_option == "4":
        check_3_units()

    elif selected_option == "5":
        break