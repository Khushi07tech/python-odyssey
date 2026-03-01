import random
import time

def hint (computer):
    if computer % 2 == 0:
        return "I thought of an even number!😉"
    elif computer % 2 == 1:
        return "I thought of an odd number!😉"
def t_sleep ():
    for x in range(2):
        print("⭐⭐⭐⭐⭐⭐")
        time.sleep(1)
def tens (computer, guess):
    if abs(computer - guess) <= 10:
        return "BUTTT... Omggg! You're so close😍🧠"
    else:
        return "BUTTT... Huhh! You're so far away😒😈"
def main ():
    #Introduction
    print ("👾Welcome to the grand number guessing game in python!🔢")
    name = input ("NAME: "). title ()

    print (f"Hello {name}!🙃 Ready to challenge me?👿 Let's jump straight into the game. Remember you have only 10 chances to guess the right answer!🧠. Collect special items to get extra attempts")
    time.sleep (0.5)
    for x in reversed (range (0, 4)):
        print (f"Starting in {x}⌛...")
        time.sleep (0.5)

    print ("Select a difficulty level")
    print ("💗A. Easy (1-50)")
    print ("💗B. Hard (1-100)")
    diff_level = input ("👉🏻Just type in A or B: "). upper ()

    while diff_level != "A" and diff_level != "B":
        print("Please type only 'A' or 'B'!")
        diff_level = input("🙄Type Again: ").upper()
    if diff_level == "A":
        lowest = 1
        highest = 50
    elif diff_level == "B":
        lowest = 1
        highest = 100

    computer = random.randint (lowest, highest)
    special_num = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
    specials = []
    guesses = 0
    score = 0
    total = 0
    attempts = 10
    is_running = True

    print ("***We are almost all set🎮***")
    time.sleep (2)

    #Starting the game
    while is_running:
        guess = (input ("Guess what did i thought: "))
        while not guess.isdigit ():
            print (f"Only Digits in the range {lowest} - {highest} are acceptable")
            guess = (input("Guess what did i thought: "))
        else:
            guess = int (guess)
            guesses += 1
            attempts -= 1
            time.sleep (1)

            if attempts == 0:
                print("SORRY. Game Over! You are out of attempts💀👽")
                is_running = False
            else:
                #Checking if the user collects special items
                if guess in special_num:
                        special_items = random.choice(["golden egg", "key", "map", "potion", "med", "tools"])
                        specials.append(special_items)
                        print(f"You've got a: {special_items}🥰")
                        attempts += 2
                        print (f"👻You've got two extra attempts.")
                        time.sleep(0.75)
                        print (f"👀Current inventory: {specials}")

                #If user's and computer's answer doesnt match
                if guess != computer:
                     if guess < lowest or guess > highest:
                         print ("Not in range😤")
                     elif (guess < computer):
                          print ("That was lesser")
                          print(tens (computer, guess))
                     elif guess > computer:
                          print ("That was higher")
                          print(tens (computer, guess))

                     #Giving the user the option to get a hint after 8 wrong guesses
                     if guesses > 8:
                         t_sleep()
                         hints = input("😁Want a hint?(Yes/No): "). lower ()
                         if hints == "yes":
                              print(hint(computer))
                         else:
                              pass

                 #If user's answer is correct
                elif guess == computer:
                    print ("Exactly! Woahhhh!!😱💗")
                    score += 1
                    time.sleep (1)
                    #the play again code
                    repeat = input ("🙈Wanna play Again? (Yes/No): "). lower ()
                    if not repeat == "yes":
                        time.sleep (2)
                        print ("okayyy then ba bye!👋🏼")
                        total += score
                        print (f"Your total score is {total}😌")
                        print (f"You guessed {guesses} times")
                        t_sleep ()
                        print (f"😍The unique items you collected were: {specials}")
                        t_sleep ()
                        is_running = False
                    else:
                        computer = random.randint (lowest, highest)
                        guesses = 0
                        specials = []
                        attempts = 10
                else:
                    print ("🙄May be u typed something invalid!!😑")
    #the loop exits forever
    print ("Thank You for playing with us!✨")

if __name__ == '__main__':
    main ()
