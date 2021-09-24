
i = input('What\'s ur mass? ')
while not i.isnumeric():
    i = input('This is not a number, what is your mass?')
mass = int(i)
unit = input('What\'s the unit? (kg/lbs)')


while unit.lower() != 'kg' and unit.lower() != 'lbs':
    unit = input('Wrong unit, what\'s the unit? (kg/lbs)')


if unit.lower() == 'lbs':
    mass = 0.453592 * mass
    print('Ur mass in kg: ' + str(round(mass, 2)))
elif unit.lower() == 'kg':
    mass = mass * 2.20462
    print('Ur mass in lbs: ' + str(round(mass, 2)))







