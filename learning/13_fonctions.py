names = ["Karima", "Margot", "Julien"]
numbers = [2, 5, 7, 8, 14]
squared = []


def greet_user(user):
    print(f"hello {user}")


def square(number):
    print(number ** 2)
    squared.append(number ** 2)


greet_user(input("Whats ur name"))
for name in names:
    greet_user(name)
for number in numbers:
    square(number)
print(squared)
