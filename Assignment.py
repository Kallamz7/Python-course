import cmath

# Volume of a Cone
print(f'Volume of a Cone')
pi = 3.142
r = int(input(f'Enter your radius'))
h = int(input(f'\nEnter your height'))

v = pi * pow(r, 2) * h/3

print(f'\nYour volume is: {v}')

# Converting time in Years to seconds
print(f'\nConverting time from years to seconds')
T = int(input(f'Enter your time in years'))

S = T * 365 * 24 * 60 * 60

print(f'\nYour Time in Seconds is: {S}')

# Solving Quadratic Equations using the Almighty formula
print(f'\nSolving Quadratic Equations using the Almighty formula')

a = int(input(f'Enter your value for a'))
b = int(input(f'\nEnter your value for b'))
c = int(input(f'\nEnter your value for c'))

x = cmath.sqrt(pow(b, 2)) - (4 * a * c)

r1 = ((-b) - x) / (2 * a)
r2 = ((-b) + x) / (2 * a)

print(f'\nYour roots for x are: {r1} and {r2}')
