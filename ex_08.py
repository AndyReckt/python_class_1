import random

persons = [
    {"name": "Richard", "Money": 100},
    {"name": "Marie", "Money": 450},
    {"name": "Robert", "Money": 300},
    {"name": "Lea", "Money": 10},
    {"name": "Baptiste", "Money": -200},
    {"name": "Uriel", "Money": 800},
]

number = random.randint(1, 6) - 1
number2 = random.randint(1, 6) - 1
while number2 == number:
    number2 = random.randint(1, 6)
persons[number]["Money"] = persons[number]["Money"] + 1000
persons[number2]["Money"] = persons[number2]["Money"] + 500

print(f"The first winner is: {persons[number].get('name')}, their new balance is: {persons[number].get('Money')}")
print(f"The second winner is: {persons[number2].get('name')}, their new balance is: {persons[number2].get('Money')}")
