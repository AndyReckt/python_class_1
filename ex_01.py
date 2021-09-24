import sys

i = input('What\'s ur mass? ')
if not i.isnumeric():
    sys.exit('This is not a number.')

mass = int(i)
unit = input('What\'s the unit? (kg/lbs)')

if unit.lower() == 'lbs':
    mass = 0.453592 * mass
    print('Ur mass in kg: ' + str(round(mass, 2)))
elif unit.lower() == 'kg':
    mass = mass * 2.20462
    print('Ur mass in lbs: ' + str(round(mass, 2)))
else:
    sys.exit('Wrong type of unit. (lbs, kg)')






