import random
import sys

number = random.randint(1, 10)
lp = 3

# print(f'debug {number}')



while True:
    if lp == 0:
        print(f'You lost! the number was {number}')
        rest = input("wanna play again? (y/n)")
        if rest == 'y':
            lp = 3
            number = random.randint(1, 10)
        else:
            sys.exit("See you soon!")

    ii = input('Choose a number')

    while not ii.isnumeric():
        ii = input('This is not a number, choose a number')
    i = int(ii)

    if i == number:
        print('Good job! you found the correct number')
        rest = input("wanna play again? (y/n)")
        if rest == 'y':
            lp = 3
            number = random.randint(1, 10)
        else:
            sys.exit("See you soon!")

    elif i < number:
        lp -= 1
        print(f'The number you chose is too low! \n you have {lp} more try')

    else:
        lp -= 1
        print(f'The number you chose is too big! \n you have {lp} more try')
