import sys

persons = [
    {
        "name": "Virginia",
        "sex": "f",
        "age": 73,
        "hair": "red"
    },
    {
        "name": "William",
        "sex": "m",
        "age": 28,
        "hair": "brown"
    },
    {
        "name": "Richard",
        "sex": "m",
        "age": 54,
        "hair": "black"
    },
    {
        "name": "Rachel",
        "sex": "f",
        "age": 23,
        "hair": "blonde"
    },
    {
        "name": "Genevieve",
        "sex": "f",
        "age": 94,
        "hair": "black"
    },
]
# faire un qui estce (return le dico)
gender = input("is it a girl? (y/n)")
if gender.lower() == 'y':
    persons.pop(1)
    persons.pop(1)
else:
    persons.pop(0)
    persons.pop(2)
    persons.pop(2)
age = input("is that person above 50 yo (y/n)")
if age.lower() == 'y':
    for i in persons:
        if i.get("age") < 50:
            persons.remove(i)
    if gender == 'y':
        hair = input('Does that person have black hair? (y/n)')
        if hair.lower() == 'y':
            persons.pop(0)
        else:
            persons.pop(1)
elif gender.lower() == 'y':
    persons.pop(0)
    persons.pop(1)
else:
    persons.pop(1)
sys.exit(f"Your person is: {persons}")
