# Write a program of polynomial taking a power of 3 and 4.
#  formular = ax^4 + bx^3 - cx + d

def poly(a = input('Enter value of a: ') , b = input('Enter value of b: '), c = input('Enter value of c: '), d = input('Enter value of d: ')):

    pwr1 = 4
    pwr2 = 3

    print('Your equation look like this: ', a + 'x^' + str(pwr1) + ' + ' + b + 'x^' + str(pwr2) + ' - ' + c + 'x + ' + d)
    
    sol1 = eval(a) ** pwr1
    sol2 = eval(b) ** pwr2
    
    answr = (sol1 + sol2) - (eval(c) + eval(d))
    
    print('Tha answer of the polynomial equation (', a + 'x^' + str(pwr1) + ' + ' + b + 'x^' + str(pwr2) + ' - ' + c + 'x + ' + d, ') is', answr)
    
poly()