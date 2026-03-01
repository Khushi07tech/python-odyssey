import random

def spin_row ():
    symbols = ['😊', '😂', '😘', '😒', '😜']
    return [random.choice(symbols) for _ in range (3)]
def print_row(row):
    print ("  |  ".join(row))
def give_payout (row, bet):
    if row [0] == row [1] == row [2]:
        if row [0] == '😊':
            return bet * 3
        elif row [0] == '😂':
            return bet * 4
        elif row [0] == '😘':
            return bet * 5
        elif row [0] == '😒':
            return bet * 6
        elif row [0] == '😜':
            return bet * 10
    return 0

def main ():
    balance = 100
    while balance > 0:
        print ("****************************")
        print ("Welcome to the Emoji Slot!")
        print (" Symbols: 😊 😂 😘 😒 😜 ")
        print ("****************************")
        print (f"Current balance: {balance}")
        bet = input ("Bet Amount: $")

        if not bet.isdigit ():
            print ("Please enter a valid amount")
            continue

        bet = int (bet)

        if bet > balance:
            print ("Insufficient Balance")
            continue

        if bet <=0:
            print ("Bet Amount can't be zero or less than zero")
            continue

        balance -= bet

        row = spin_row ()
        print ("Spinning...")
        print_row (row)

        payout = give_payout(row, bet)
        if payout > 0:
            print (f"You won ${payout}")
        else:
            print ("Sorry, you lose this round")

        balance += payout

        play_again = input ("Do you want to play again? (Y/N): "). upper ()
        if not play_again == "Y":
            break
    print (f"Game Over! Your balance is {balance}")
if __name__ == '__main__':
    main ()