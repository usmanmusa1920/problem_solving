import cmath

# Quadratic equation
a = float(input('Enter a: '))
b = float(input('Enter b: '))
c = float(input('Enter c: '))

#  This will calculate the discriminant

d = (b ** 2) - (4 * a * c)

#  This will find two solution of negative and positive

soln1 = (-b-cmath.sqrt(d)) / (2 * a)
soln2 = (-b+cmath.sqrt(d)) / (2 * a)

print('The quadratic equation solution are {0} and {1}'.format(soln1,soln2))