import random

def try_user_choice():
    try:
        user_choice = input("User Choice(q to exit): ").lower()
        if not user_choice.isalpha() or user_choice not in {"rock", "paper", "scissors", "lizard", "spock", "q"}:
            raise ValueError
        else:
            return user_choice
    except ValueError:
        print("🙄Value Error:\nEnter a correct value as per the choices")
    except Exception as e:
        print(f"😪Error:\n{e}")

def checking(user_validated_choice, computer_choice, points):
    rules = {
        "rock": ["scissors", "lizard"],
        "paper": ["rock", "spock"],
        "scissors": ["paper", "lizard"],
        "lizard": ["spock", "paper"],
        "spock": ["scissors", "rock"]
    }
    if computer_choice in rules[user_validated_choice]:
        print("🎀You win! (+1) ")
        points += 1
    elif user_validated_choice == computer_choice:
        print("🤝Tie!")
    else:
        print("🎃You lose! (-1)")
        points -= 1

    return points


print("Rock | Paper | Scissors | Lizard | Spock")
print("""
👀Game Rules:
Scissors ✂️ cuts Paper 📄
Paper 📄 covers Rock 🪨
Rock 🗻 crushes Lizard 🦎
Lizard 🦎 poisons Spock 🖖
Spock 🖖 smashes Scissors ✂️
Scissors ✂️ decapitates Lizard 🦎
Lizard 🦎 eats Paper 📄
Paper 📄 disproves Spock 🖖
Spock 🖖 vaporizes Rock 🪨
Rock 🗻 crushes Scissors ✂️
""")
points = 10

while True:

    print("✨💖🎀👀🌷🎀🌷💌🕊️✨🦋💗🌸🍓✨🌸🦢💌✨🌙🕯️📖✨🕊️")
    choices = ["rock", "paper", "scissors", "lizard", "spock"]
    computer_choice = random.choice(choices)

    user_validated_choice = try_user_choice()
    if user_validated_choice == "q":
        print(f"Points: {points}")
        print("Goodbye!")
        break
    if user_validated_choice:
        print(f"Computer Choice: {computer_choice}")
        points = checking(user_validated_choice, computer_choice, points)
        print(f"Points: {points}")
        if points <= 0:
            print("Game Over!")
            break
        print("🌙💫🦢✨🌸🩰🎀🌷✨🩷🌸🎀🦋✨💖🍰🎀🌷🧁💖🎀🌷💌🕊️")
