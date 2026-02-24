def c_to_f(user_temp):
    calculate_c_to_f = (9 / 5) * (user_temp) + 32
    print(f"{calculate_c_to_f:.2f}")

def f_to_c(user_temp):
    calculate_f_to_c = (5 / 9) * (user_temp - 32)
    print(f"{calculate_f_to_c:.2f}")

def c_to_k(user_temp):
    calculate_c_to_k = user_temp + 273.15
    print(f"{calculate_c_to_k:.2f}")

def k_to_c(user_temp):
    calculate_k_to_c = user_temp - 273.15
    print(f"{calculate_k_to_c:.2f}")

try:
    user_temp = int(input("Enter temperature: "))
    print("""
        1. °C to °F
        2. °F to °C
        3. °C to  K
        4.  K to °C
    """)

    user_choice = input("Select one: ")
    if user_choice == "1":
        c_to_f(user_temp)
    elif user_choice == "2":
        f_to_c(user_temp)
    elif user_choice == "3":
        c_to_k(user_temp)
    elif user_choice == "4":
        k_to_c(user_temp)
    else:
        raise ValueError
except ValueError:
    print("Value Error")
except Exception as e:
    print(f"Oh Oh!\n{e}")