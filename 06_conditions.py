# conditions
import sys

country = input('Where are you from')
age = int(input('Age?'))


if country == 'fr' and age >= 18:
    # code a indenter
    print('Welcome!')
elif country == 'us' and age >= 21:
    print('welcome u american kid')
elif age >= 18 and country != 'us':
    print('meh u can pass smh')
else:
    sys.exit('bye bye')

