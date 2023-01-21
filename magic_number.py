import os, random

SHOP = {
    "Chocolate bar": 10,
    "Cinema ticker": 30,
    "Travel ticker": 40
}

MIN = 1
MAX = 10
REWARD = 10

# player variables
LIFES = 3
CREDITS = 0
PLAYER_NAME = None

# entry point
def main():
    # Start intro
    intro()

    # get player name and store it in PLAYER_NAME variable
    get_player_name()

    # start game
    game_loop()

def game_loop():
    global LIFES

    magic_number = 5
    player_guess = input("Your guess:")

    while player_guess != str(magic_number):
        LIFES -= 1

        if LIFES == 0:
            print("Wrong guess. The game is over :(")
            player_choice = get_if_want_to_play()

            if player_choice == "y":
                LIFES = 3
                game_loop()
            else:
                outro()
        
        print(f"Wrong guess but you have {LIFES} lifes left.")
        player_guess = input("Your guess:")

    claim_reward(magic_number, player_guess)

def claim_reward(magic_number, player_guess):
    global CREDITS

    clear_screen()

    if str(magic_number) == player_guess:
        CREDITS += REWARD
        print(f"Yess! {magic_number} was my number.")
        print(f"You won {REWARD} credits")
        print(f"Now you have {CREDITS} credits")

    player_choice = get_if_want_to_play()
    if player_choice == "y":
        game_loop()
    else:
        outro()


def get_if_want_to_play():
    result = input("Do you want to play again? (y/n)")
    return result

def get_player_name():
    global PLAYER_NAME
    PLAYER_NAME = input("What is your name?")

def intro():
    clear_screen()
    print("="*50, "MAGIC NUMBER", "="*50)
    print("In this game you have to guess a number I'm thinking of. The number must be between 1 and 10.")

def outro():
    clear_screen()
    print("See you later!")
    exit()

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


main()