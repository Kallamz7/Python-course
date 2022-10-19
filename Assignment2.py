import cmath
# Volume of a Cone
print(f'Volume of a Cone')


def volume():
    return (pi * pow(r, 2) * h)/3


pi = 3.142
r = int(input(f'Enter your radius'))
h = int(input(f'\nEnter your height'))

my_volume = volume()
print(f'\nYour volume is: {my_volume}')

# Converting time in Years to seconds
print(f'\nConverting time from years to seconds')


def years():
    return t * 365 * 24 * 60 * 60


t = int(input(f'Enter your time in years'))
S = years()

print(f'\nYour Time in Seconds is: {S}')

# Solving Quadratic Equations using the Almighty formula
print(f'\nSolving Quadratic Equations using the Almighty formula')


def formula():
    x = cmath.sqrt(pow(b, 2)) - (4 * a * c)
    r1 = ((-b) - x) / (2 * a)
    r2 = ((-b) + x) / (2 * a)
    return r1, r2


a = int(input(f'Enter your value for a'))
b = int(input(f'\nEnter your value for b'))
c = int(input(f'\nEnter your value for c'))

my_formula = formula()

print(f'\nYour roots for x are: {my_formula}')
