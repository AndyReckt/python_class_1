list = [27, 90, 'biker', 'habani']

yann = {  # Json
    "name": "yann",
    "polo": "noir",
    "age": 19,
    "hobbies": ['Harley davidson', "rassemblement motard", "FBF"],
    "like_indian": False,
}

print(yann.get("age"))
yann['hobbies'][2] = "Guitare"
print(yann)
yann.setdefault("birthdate", 2003)
print(yann)
print(yann.get("hobbies")[2])
print(yann.get("bday", "01/01/1965"))

yann["sexe"] = "m"

