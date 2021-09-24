course = "Python for beginners"

# declare un string
# variable devient un objet string
# objet = boite virtuelle comprenant des donnés
# actions permettant de manipuler les donnés
# actions = methodes
# methode = fonction dans un objet


print(course.upper())
if course.__contains__('for'):
    course.replace('for', '4')
print(course)
# .upper() retourne un string mais la modifie pas
# il faudrait