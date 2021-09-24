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


def chose_difficulty():  # function that lets u choose the difficulty of the game
    while True:
        diff = input("Choose ur difficulty: (0 for easy, 1 for hard, 2 for challenge) ")
        if diff.lower() == 0 or diff.lower() == "easy" or diff.lower() == "e":
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
            return {"life": 10, "penalty": 3, "bonus": 1, "name": "Bulbasaur"}
        elif start.lower() == '1' or start.lower() == "Charmander" or start.lower() == "c":
            return {"life": 15, "penalty": 2, "bonus": 2, "name": "Charmander"}
        elif start.lower() == '2' or start.lower() == "Charizard" or start.lower() == "ch":
            return {"life": 20, "penalty": 1, "bonus": 3, "name": "Charizard"}
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


difficulty = chose_difficulty()  # choosing difficulty
starter = chose_starter()  # choosing starter
starter['name'] = custom_name(starter.get("name"))   # choosing starter name

