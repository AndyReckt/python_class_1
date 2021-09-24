import random
import sys

pkms = (
    {"name": "Marowak", "points": 3, "good": False},
    {"name": "Weezing", "points": 2, "good": False},
    {"name": "Virizion", "points": 3, "good": False},
    {"name": "Suicune", "points": 4, "good": False},
    {"name": "Uxie", "points": 3, "good": False},
    {"name": "Quagsire", "points": 5, "good": False},
    {"name": "Zebstrika", "points": 1, "good": False},
    {"name": "Spinda", "points": 1, "good": False},
    {"name": "Zapdos", "points": 2, "good": False},
    {"name": "Togekiss", "points": 4, "good": False},
    {"name": "Zarude", "points": 3, "good": True},
    {"name": "Poliwrath", "points": 2, "good": True},
    {"name": "Urshifu", "points": 3, "good": True},
    {"name": "Copperajah", "points": 4, "good": True},
    {"name": "Minun", "points": 3, "good": True},
    {"name": "Jirachi", "points": 5, "good": True},
    {"name": "Gliscor", "points": 1, "good": True},
    {"name": "Dusknoir", "points": 1, "good": True},
    {"name": "Rotom", "points": 2, "good": True},
    {"name": "Politoed", "points": 4, "good": True},
)  # tuple that contains all the available Pokemon to fight
starters = (
    {"life": 10, "penalty": 3, "bonus": 1, "name": "Bulbasaur"},
    {"life": 15, "penalty": 2, "bonus": 2, "name": "Charmander"},
    {"life": 20, "penalty": 1, "bonus": 3, "name": "Charizard"}
)  # tuple that contains all the available starters


def choose_difficulty():  # function that lets u choose the difficulty of the game
    while True:
        diff = input("Choose ur difficulty: (0 for easy, 1 for hard, 2 for challenge) ")
        if diff.lower() == '0' or diff.lower() == "easy" or diff.lower() == "e":
            return 0
        elif diff.lower() == '1' or diff.lower() == "hard" or diff.lower() == "h":
            return 1
        elif diff.lower() == '2' or diff.lower() == "challenge" or diff.lower() == "c":
            return 2
        else:
            print("Sorry but i cant understand this value...")


def chose_starter():  # function that lets u choose your starter for the game
    while True:
        start = input("Choose ur starter: (b for Bulbasaur, c for Charmander, ch for Charizard) ")
        if start.lower() == '0' or start.lower() == "Bulbasaur" or start.lower() == "b":
            return starters[0]
        elif start.lower() == '1' or start.lower() == "Charmander" or start.lower() == "c":
            return starters[1]
        elif start.lower() == '2' or start.lower() == "Charizard" or start.lower() == "ch":
            return starters[2]
        else:
            print("Sorry but i cant understand this value...")


def custom_name(pk):  # function that lets u choose a custom name for your pokemon
    r = input("Do you want to give a custom name to your pokemon? (y/n) ")
    while True:
        if r.lower() == 'y' or r.lower() == 'yes' or r.lower() == 'o' or r.lower() == 'oui':
            n = input("What will his new name be then? ")
            return n
        elif r.lower() == 'n' or r.lower() == 'no' or r.lower() == 'non':
            return pk
        else:
            print("Sorry but i cant understand this value...")


def encounter_pokemon(pokemon, round):
    wild = pkms[random.randint(0, len(pkms) - 1)]
    print(f"You encountered a {wild['name']}")

    if starter['ran'] == False:
        run = input("Do you want to run? (y/n)")
        while True:
            if run.lower() == 'y' or run.lower() == 'yes' or run.lower() == 'o' or run.lower() == 'oui' or run.lower() == 'x':
                starter['ran'] = True
                return
            elif run.lower() == 'n' or run.lower() == 'no' or run.lower() == 'non':
                break
            else:
                print("Sorry but i cant understand this value...")
    else:
        print(f"Since you ran last encounter, you will now loose {2 + wild['points']} life points")
        pokemon['life'] -= 2 + wild['points']
        starter['ran'] = False

    if wild['good']:
        print(f"You encountered a {wild['name']} which is a good pokemon, {pokemon['name']} will now gain {wild['points']} life points")
        pokemon['life'] += wild['points']
        print(f"{pokemon['name']} now has {pokemon['life']} life points.")
    elif pokemon['life'] <= wild['points']:
        print(f"You encountered a {wild['name']} which is a bad pokemon, {pokemon['name']} will now lose {wild['points']} life points")
        print(f"Unfortunately, {pokemon['name']} only has {pokemon['life']} life points, and died :(")
        sys.exit(f"You lost in {round} rounds")
    else:
        print(f"You encountered a {wild['name']} which is a bad pokemon, {pokemon['name']} will now lose {wild['points']} life points")
        pokemon['life'] -= wild['points']
        print(f"{pokemon['name']} now has {pokemon['life']} life points.")


def left_right():
    r = input("Which door do you want to open? (left/right)")
    while True:
        if r.lower() == 'l' or r.lower() == 'left' or r.lower() == 'g' or r.lower() == 'gauche':
            print("You chose the left door...")
            break
        elif r.lower() == 'r' or r.lower() == 'right' or r.lower() == 'd' or r.lower() == 'droite':
            print("You chose the right door...")
            break
        else:
            print("Sorry but i cant understand this value...")


def game(diff, pokemon):  # the main game function, that will run the game
    i = 0
    if diff == 0:
        rounds = 4
    elif diff == 1:
        rounds = 11
    else:
        rounds = 19
    while i <= rounds:
        i += 1
        left_right()
        encounter_pokemon(pokemon, i)
    sys.exit(f"Wow, you won!! {pokemon['name']} had {pokemon['life']} life points left. Congrats!!")


difficulty = choose_difficulty()  # choosing difficulty
starter = chose_starter()  # choosing starter
starter['name'] = custom_name(starter.get("name"))   # choosing starter name
starter['ran'] = False

game(difficulty, starter)  # starting the game
