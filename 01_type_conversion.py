name = input('Whats ur name')

print(name)

print(input('Name again?'))
birth_year = input("birthyear?")
# input renvoie tjr un str
print(type(birth_year))

# conversstion d'un str en int pour calculation puis reconversion en str pour l'afficher sur la console systeme
print("You are " + str(2021 - int(birth_year)) + " years old")





