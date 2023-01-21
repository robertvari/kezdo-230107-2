import os

REWARDS = {
    "Chocolate bar": 10,
    "Cinema ticker": 30,
    "Travel ticker": 40
}

MIN = 1
MAX = 10

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
    pass

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